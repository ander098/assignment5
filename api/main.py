from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.models.schemas import Sandwich, SandwichCreate, SandwichUpdate, Resource, ResourceCreate, ResourceUpdate
from api.controllers import sandwiches, resources

app = FastAPI()


@app.post("/sandwiches/", response_model=Sandwich)
def create_sandwich(sandwich: SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create_sandwich(db, sandwich)

@app.get("/sandwiches/", response_model=list[Sandwich])
def get_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.get_all_sandwiches(db)

@app.get("/sandwiches/{sandwich_id}", response_model=Sandwich)
def get_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.get_sandwich(db, sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=Sandwich)
def update_sandwich(sandwich_id: int, sandwich: SandwichUpdate, db: Session = Depends(get_db)):
    return sandwiches.update_sandwich(db, sandwich_id, sandwich)

@app.delete("/sandwiches/{sandwich_id}", status_code=204)
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwiches.delete_sandwich(db, sandwich_id)


@app.post("/resources/", response_model=Resource)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return resources.create_resource(db, resource)

@app.get("/resources/", response_model=list[Resource])
def get_resources(db: Session = Depends(get_db)):
    return resources.get_all_resources(db)

@app.get("/resources/{resource_id}", response_model=Resource)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.get_resource(db, resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.put("/resources/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, resource: ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update_resource(db, resource_id, resource)

@app.delete("/resources/{resource_id}", status_code=204)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.delete_resource(db, resource_id)
