class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Qwerty.123'
    MYSQL_DB = 'library'


config = {
    'development': DevelopmentConfig
}