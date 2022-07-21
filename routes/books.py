from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
import app


books = Blueprint('books', __name__)
conexion = MySQL(app)

@books.route('/books_other')
def test_book():
    return "Solo es una prueba exitosa!"

@books.route('/books', methods=['GET'])
def list_courses():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM book"
        cursor.execute(sql)
        data_result = cursor.fetchall()
        books = []
        for data in data_result:
            book = {'isbn':data[0], 'title':data[1], 'year_published':data[2], 'category_id': data[3]}
            books.append(book)
        return jsonify({'msg': 'List of books', 'books':books})
    except Exception as ex:
        return "Error"


@books.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    try:
        cursor = conexion.connection.cursor()
        #sql = "SELECT * FROM book WHERE isbn=%d" % isbn
        sql = "SELECT * FROM book WHERE isbn='{0}'".format(isbn)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None:
            book = {'isbn':data[0], 'title':data[1], 'year_published':data[2], 'category_id': data[3]}
            return jsonify({'msg': 'Books founded', 'book': book})
        else:
            return jsonify({'msg': 'Books does not founded'})
    except Exception as ex:
        return jsonify({'msg': 'Error'})


@books.route('/books', methods=['POST'])
def create_book():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO book (isbn, title, year_published, category_id)
                 VALUES ('{0}', '{1}', '{2}', '{3}')""".format(
                    request.json['isbn'],
                    request.json['title'], 
                    request.json['year_published'],
                    request.json['category_id'])
        cursor.execute(sql)
        conexion.connection.commit() # confirm insert the new record
        
        #print(request.json)
        return jsonify({'msg': 'New book was registered'})
    except:
        return jsonify({'msg': 'Error'})


@books.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM book WHERE isbn = '{0}'".format(isbn)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'msg': 'The book was deleted.'})
    except:
        return jsonify({'msg': 'Error'})


@books.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE book SET 
                    title = '{0}', 
                    year_published = '{1}', 
                    category_id = '{2}'
                WHERE isbn = '{3}'
                """.format(
                    request.json['title'], 
                    request.json['year_published'],
                    request.json['category_id'],
                    isbn
                )
        cursor.execute(sql)
        conexion.connection.commit() # confirm insert the new record
        return jsonify({'msg': 'The book was updated'})
    except:
        return jsonify({'msg': 'Error'})