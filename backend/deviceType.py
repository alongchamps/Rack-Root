from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import Optional
from .database import get_db, DeviceType
from .validation_deviceType import DeviceTypeCreate, DeviceTypeResponse, DeviceTypeUpdate

# reading
def read_all_device_types(request: Request, db: Session = Depends(get_db), ):
    db_items = db.query(DeviceType)
    return db_items

def read_device_type(dev_id: int, db: Session = Depends(get_db)):
    db_item = db.query(DeviceType).filter(DeviceType.id == dev_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="A device with that ID was not found")

    return db_item

def get_valid_device_id( deviceTypeId: Optional[int] = None, db: Session = Depends(get_db) ) -> int:
    if deviceTypeId is None:
        raise HTTPException(status_code=400, detail="Device type ID is required")
    
    deviceType = db.query(DeviceType).filter(DeviceType.id == deviceTypeId).first()
    if deviceType is None:
        raise HTTPException(status_code=400, detail="Invalid device ID")
    return deviceTypeId

# creating
def create_device_type(deviceType: DeviceTypeCreate, db: Session = Depends(get_db)):
    db_item = DeviceType(**deviceType.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Updating
def update_device_type(dev_id: int, devUpdate: DeviceTypeUpdate, db: Session = Depends(get_db)):
    itemsAffected = db.query(DeviceType).filter(DeviceType.id == dev_id).update(dict(**devUpdate.model_dump()))
    db.commit()
    return itemsAffected

## Deleting
def delete_device_type(dev_id: int, db: Session = Depends(get_db)):
    db_delete = db.query(DeviceType).filter(DeviceType.id == dev_id).delete(synchronize_session="auto")
    db.commit()

    if db_delete == 0:
        raise HTTPException(status_code=404, detail="A device with that ID was not found")

    return 0
