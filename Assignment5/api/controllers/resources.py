from sqlalchemy.orm import Session
from api.models.models import Resource
from api.models.schemas import ResourceCreate, ResourceUpdate

def create_resource(db: Session, resource: ResourceCreate):
    db_resource = Resource(item=resource.item, amount=resource.amount)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_all_resources(db: Session):
    return db.query(Resource).all()

def get_resource(db: Session, resource_id: int):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def update_resource(db: Session, resource_id: int, resource: ResourceUpdate):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if db_resource:
        db_resource.item = resource.item
        db_resource.amount = resource.amount
        db.commit()
        db.refresh(db_resource)
    return db_resource

def delete_resource(db: Session, resource_id: int):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if db_resource:
        db.delete(db_resource)
        db.commit()
    return db_resource
