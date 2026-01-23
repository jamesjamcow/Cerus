from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    screws = relationship("Screw", back_populates="project")

class Screw(Base):
    __tablename__ = "screws"

    id = Column(String, primary_key=True, index=True)
    project_id = Column(String, ForeignKey("projects.id"), index = True, nullable=True)
    name = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=True, default=0)
    typeOfHead = Column(String, nullable=False)
    project = relationship("Project", back_populates="screws") 
