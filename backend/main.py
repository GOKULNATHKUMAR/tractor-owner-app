import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tractor Owner App")

@app.get("/")
def root():
    return {"message": "Backend running successfully"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/owners", response_model=schemas.OwnerResponse)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_owner = models.Owner(**owner.dict())
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

@app.get("/owners", response_model=list[schemas.OwnerResponse])
def get_owners(db: Session = Depends(get_db)):
    return db.query(models.Owner).all()