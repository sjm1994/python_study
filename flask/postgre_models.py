# coding: utf-8
from maria_models import db
from sqlalchemy.dialects.postgresql import TEXT, JSONB, UUID, BIT
from sqlalchemy.types import Text

class Keywords(db.Model):
    __tablename__ = 'keywords'
    __bind_key__ = 'postgre'

    id = db.Column(UUID, primary_key=True)
    keyword = db.Column(db.Text, unique=True)
    created_date = db.Column(db.DateTime(True), server_default=db.FetchedValue())