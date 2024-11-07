from sqlalchemy.orm import Session
from api.models.models import Sandwich
from api.models.schemas import SandwichCreate, SandwichUpdate

def create_sandwich(db: Session, sandwich: SandwichCreate):
    db_sandwich = Sandwich(sandwich_name=sandwich.sandwich_name, price=sandwich.price)
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def get_all_sandwiches(db: Session):
    return db.query(Sandwich).all()

def get_sandwich(db: Session, sandwich_id: int):
    return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

def update_sandwich(db: Session, sandwich_id: int, sandwich: SandwichUpdate):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db_sandwich.sandwich_name = sandwich.sandwich_name
        db_sandwich.price = sandwich.price
        db.commit()
        db.refresh(db_sandwich)
    return db_sandwich

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
    return db_sandwich
