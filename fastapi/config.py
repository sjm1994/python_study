maria_db = {
    'user': 'testuser',
    'password': 'test!%40#$',
    'host': 'localhost',
    'port': 3306,
    'database': 'testdb'
}

SQLALCHEMY_MARIA_URI = f"mariadb+mariadbconnector://{maria_db['user']}:{maria_db['password']}@{maria_db['host']}:{maria_db['port']}/{maria_db['database']}?charset=utf8"