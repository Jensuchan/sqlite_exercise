## models 는 객체들의 정보 (table에 대해 구성하는 파일)
## 여러테이블들의 외래키설정도 여기서 해야함
## Pydantic은 데이터 검증과 설정 관리를 위한 Python 라이브러리로,
## Python 타입 힌팅을 사용하여 데이터의 검증, 직렬화, 문서화를 간편하게해준다


from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import ForeignKey, DateTime
import datetime
import uuid

#img_no_(file_name)
# 1_dog.jpg

Base = declarative_base()


class Image(Base):
    __tablename__ = "image"

    uuid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    img_category = Column(String, nullable=True)
    save_dir = Column(String, nullable=False)
    img_name = Column(String, nullable=False)
    img_size = Column(Integer)

    def __init__(self, uuid, img_category, save_dir, img_name, img_size):
        self.uuid = uuid
        self.img_category = img_category
        self.save_dir = save_dir
        self.img_name = img_name
        self.img_size = img_size


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     password = Column(String)

#     def __init__(self, name, fullname, password):
#         self.name = name
#         self.fullname = fullname
#         self.password = password

#         def __repr__(self):
#             return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)
        

print(Image.__table__)
print(Image.__mapper__)

