## database 는 실제로 엔진 연결하는 파일

from sqlalchemy import create_engine, text, Table, MetaData
from sqlalchemy.orm import sessionmaker, Session
from models import *

DATABASE_URL = "sqlite:///image.db"
metadata = MetaData()

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def print_image_data():
#     with Session(engine) as session:
#         image_data_items = session.query().all()
#         for item in image_data_items:
#             print("")

##name = main 일때만 배쉬에서 작동함
# if __name__ == "__main__":
#     print_image_data()