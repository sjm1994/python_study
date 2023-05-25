from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import FetchedValue
import datetime

class Base(DeclarativeBase):
    pass

class DataList(Base):
    __tablename__ = "data_list"

    dataNo: Mapped[int] = mapped_column(primary_key=True, info='Data 번호')
    dataKeyword: Mapped[str] = mapped_column(info='Data 키워드')
    useYn: Mapped[str] = mapped_column(server_default=FetchedValue(), info='data 사용여부')