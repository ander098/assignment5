from sqlalchemy.orm import Session
from api.models.models import Order
from api.models.schemas import OrderCreate, OrderUpdate

def create_order(db: Session, order: OrderCreate):
    db_order = Order(customer_name=order.customer_name, description=order.description)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_all_orders(db: Session):
    return db.query(Order).all()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def update_order(db: Session, order_id: int, order: OrderUpdate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db_order.customer_name = order.customer_name
        db_order.description = order.description
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
