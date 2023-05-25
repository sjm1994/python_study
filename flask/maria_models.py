# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class DataList(db.Model):
    __tablename__ = 'data_list'

    dataNo = db.Column(db.String(20), primary_key=True, nullable=False, index=True, info='DATA 번호')
    dataKeyword = db.Column(db.String(20), info='DATA 키워드')
    useYn = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue(), info='DATA 사용여부')

