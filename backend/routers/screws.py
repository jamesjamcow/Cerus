import uuid 
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session
from db.database import get_db, SessionLocal
from schemas.project import ProjectBase, ScrewCreate, ScrewResponse, ScrewUpdate, ProjectCreate, ScrewCreate
from models.project import Project, Screw


router = APIRouter( prefix="/screws", tags=["screws"] )

@router.get("/{screw_id}", response_model=ScrewResponse)
def get_screw(screw_id: int, db: Session = Depends(get_db)):
    screw = db.query(Screw).filter(Screw.id == screw_id).first()
    if not screw:
        raise HTTPException(status_code=404, detail="Screw not found")
    return screw

@router.post("/", response_model=ScrewResponse)
def create_screw(request:ScrewCreate, db: Session = Depends(get_db)):
    new_screw = Screw(
        id=str(uuid.uuid4()),
        project_id=request.project_id,
        name=request.name,
        length=request.length,
        diameter=request.diameter,
        typeOfHead=request.typeOfHead,
        amount=0
    )
    db.add(new_screw)
    db.commit()
    return new_screw