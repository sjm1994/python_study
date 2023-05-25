# FLASK

[flask docs](https://flask.palletsprojects.com/en/2.3.x/)

flask 기본 웹 구성 및 다중 DB 연결 테스트용 소스입니다.

## 사용 모듈

### flask 프레임워크
`pip install Flask`

### db 연결 처리용 모듈(flask용)
`pip install Flask-SQLAlchemy`

### mysql(mariadb) 연결용 모듈
`pip install mysql-connector-python`

### postgre 연결용 모듈
`pip install psycopg2`

### 기존 DB에서 모델을 추출하고 싶을 때 사용
`pip install flask-sqlacodegen`

`flask-sqlcodegen "sql접속정보" --flask > 추출파일명.py`