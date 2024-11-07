from sqlalchemy.orm import Session
from api.models.models import Recipe
from api.models.schemas import RecipeCreate, RecipeUpdate

def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(sandwich_id=recipe.sandwich_id, resource_id=recipe.resource_id, amount=recipe.amount)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_all_recipes(db: Session):
    return db.query(Recipe).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def update_recipe(db: Session, recipe_id: int, recipe: RecipeUpdate):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe:
        db_recipe.sandwich_id = recipe.sandwich_id
        db_recipe.resource_id = recipe.resource_id
        db_recipe.amount = recipe.amount
        db.commit()
        db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe
