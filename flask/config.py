maria_db = {
    'user': 'testuser',
    'password': 'testpass!%40#$',
    'host': 'localhost',
    'port': 3306,
    'database': 'testdb'
}

SQLALCHEMY_MARIA_URI = f"mysql+mysqlconnector://{maria_db['user']}:{maria_db['password']}@{maria_db['host']}:{maria_db['port']}/{maria_db['database']}?charset=utf8"

postgre_db = {
    'user': 'testuser',
    'password': 'testpass!!!!##',
    'host': 'localhost',
    'port': 5432,
    'database': 'testdb'
}

SQLALCHEMY_POSTGRE_URI = f"postgresql+psycopg2://{postgre_db['user']}:{postgre_db['password']}@{postgre_db['host']}:{postgre_db['port']}/{postgre_db['database']}"

SQLALCHEMY_BINDS = {
    'postgre': SQLALCHEMY_POSTGRE_URI
}