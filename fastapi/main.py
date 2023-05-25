from fastapi import FastAPI, HTTPException
from typing import Union, List
from fastapi.encoders import jsonable_encoder
import models
from sqlalchemy import create_engine
from config import SQLALCHEMY_MARIA_URI
from maria_model import DataList
from sqlalchemy import select
from sqlalchemy.orm import Session

app = FastAPI()
engine = create_engine(SQLALCHEMY_MARIA_URI)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# 메소드에 파라미터로 선언할 경우(아래 q의 경우) request에 넘어오는 동일 이름 값에 자동 바인딩 됨
# Union[A, B] => A 아니면 B로 처리하라는 뜻, 자바 Optional 역할(FastApi에서는 = None로 처리되지만 개발 / 테스트 과정에서 인식시키기 위해 Union도 같이 사용)
# 또, 선언한 파라미터의 타입값으로 자동 validation 처리해줌
# 기본값 지정 안해주면 필수 입력 파라미터로 지정됨(아래 must_insert)
# 기본값 지정 안하는 파라미터들이 기본값 지정하는 파라미터들보다 앞에 있어야 함. 문법 오류남
@app.get("/products/{product_id}")
def get_item(product_id: int, must_insert: str, q: Union[str, None] = None):
    return {"product_id": product_id, "must_insert": must_insert, "q": q}

# jsonable_encoder는 Model 데이터를 json 형식으로 변환시켜줌
@app.put("/products/{product_id}")
def put_item(product_id: int, product: models.Product):
    return {"product_name": product.name, "product_id": product_id, "product": jsonable_encoder(product)}

# enum(열거형) 형식으로 처리 가능
@app.get("/enum/str/{enum_value}")
def get_enum_str(enum_value: models.StrEnumModel):
    if enum_value is models.StrEnumModel.apple:
        return {"enum_value": enum_value, "message": "It's Apple!"}
    if enum_value is models.StrEnumModel.banana:
        return {"enum_value": enum_value, "message": "It's Banana!"}
    if enum_value is models.StrEnumModel.melon:
        return {"enum_value": enum_value, "message": "It's Melon!"}
    return {"enum_value": enum_value, "message": "It's not in Enum!"}

@app.get("/enum/int/{enum_value}")
def get_enum_str(enum_value: models.IntEnumModel):
    if enum_value is models.IntEnumModel.first:
        return {"enum_value": enum_value, "message": "1st!"}
    if enum_value is models.IntEnumModel.second:
        return {"enum_value": enum_value, "message": "2nd!"}
    if enum_value is models.IntEnumModel.third:
        return {"enum_value": enum_value, "message": "3rd!"}
    return {"enum_value": enum_value, "message": "It's not in Enum!"}

# 경로(/)가 포함된 인자값도 처리 가능
@app.get("/paths/{req_path:path}")
def get_paths(req_path: str):
    return {"req_path" : req_path}

'''
# 2.0이상 버전의 sqlalchemy에서 Row 형식이 아닌 Model 형식 데이터를 반환받기 위해 session.execute 대신 session.scalars를 사용한다
@app.get("/datas/{data_id}", response_model=models.DataList)
def get_datas(data_id: int):
    with Session(engine) as session:
        stmt = select(DataList).where(DataList.dataNo == data_id)
        result = session.scalars(stmt).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return result

@app.get("/datas", response_model=List[models.DataList])
def get_datas():
    with Session(engine) as session:
        stmt = select(DataList).order_by(DataList.dataNo)
        result = session.scalars(stmt).all()
    if result is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return result
'''