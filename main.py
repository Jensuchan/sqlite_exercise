from fastapi import FastAPI, File, UploadFile, Request
from pydantic import BaseModel
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from sqlalchemy.orm import Session
import os
from api.classification import classfication
from datetime import datetime
import uuid
from sqlalchemy import create_engine

import models, database


app = FastAPI()
app.mount("/image", StaticFiles(directory="image"))

print(app.version)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root():
    return FileResponse('index.html')


templates = Jinja2Templates(directory="templates")  



@app.post("/image")
async def upload_image(file: UploadFile):
    UPLOAD_DIR = "./image"
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    content = await file.read()
    filename = file.filename
    filesize = len(content)
    
    random_uuid = str(uuid.uuid4())
    print(random_uuid)
    save_filename = random_uuid+"_"+filename

    with open(os.path.join(UPLOAD_DIR, save_filename), "wb") as fp:
        fp.write(content)


    image = models.Image(uuid=random_uuid, save_dir=UPLOAD_DIR, img_category=None, img_name=filename, img_size=filesize)

    DATABASE_URL = "sqlite:///image.db"
    metadata = database.MetaData()



    #DB
    # engine = create_engine(DATABASE_URL, echo=True)
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # Base.metadata.create_all(bind=engine)
    # db = SessionLocal()
    # db = get_db()
    # db.add(image)
    # db.commit()
    # db.close()







    # if not os.path.exists(UPLOAD_DIR):
    #     os.makedirs(UPLOAD_DIR)


    # content = await file.read()
    # with open(os.path.join(UPLOAD_DIR, save_filename), "wb") as fp:
    #     fp.write(content)



    #image = Image(uuid= random_uuid, img_category=None, save_dir=folder_name, img_name=filename, img_size=file.size)

    # with open(os.path.join(target_dir, filename), "wb") as fp:
    #     fp.write(content)


    response = RedirectResponse(url=f"/success?save_filename={save_filename}", status_code=303)

    return response

@app.get("/success")
async def upload_success(request: Request, save_filename: str):  
    return templates.TemplateResponse("class.html", {"request": request, "save_filename": save_filename})

@app.get("/classif")
async def classify_image():
    return classfication()


