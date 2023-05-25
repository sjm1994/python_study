from flask import Flask, render_template
from config import SQLALCHEMY_MARIA_URI, SQLALCHEMY_POSTGRE_URI, SQLALCHEMY_BINDS
import json
from postgre_models import db, Keywords
from maria_models import DataList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_MARIA_URI
app.config["SQLALCHEMY_BINDS"] = SQLALCHEMY_BINDS
db.init_app(app)


@app.route('/', methods=['GET'])
def calculateKeyword():
    DataLists = DataList.query.order_by(DataList.dataNo).all()
    dataOne = DataLists[0]
    print(dataOne.dataNo)

    KeywordLists = Keywords.query.order_by(Keywords.id).all()
    keywordOne = KeywordLists[0]
    print(keywordOne.id)

    return render_template('index.html', data=SQLALCHEMY_BINDS)
    

if __name__ == '__main__':
    app.run(debug=True)