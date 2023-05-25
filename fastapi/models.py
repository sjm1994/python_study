from typing import Union
from pydantic import BaseModel
from enum import Enum, IntEnum
from pydantic import BaseModel
import datetime

class Product(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class StrEnumModel(str, Enum):
    apple = "apple"
    banana = "banana"
    melon = "melon"

# 열거형에서 int 처리하기 위해 IntEnum 사용 필요
class IntEnumModel(IntEnum):
    first = 1
    second = 2
    third = 3

class DataList(BaseModel):
    subjectNo: int
    dataKeyword: str = None
    useYn: str = None

    class Config:
    	orm_mode = True