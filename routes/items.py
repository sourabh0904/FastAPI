from fastapi import APIRouter, HTTPException , status, Depends
from sqlmodel import Session , select
from database import get_session
from models import Item, ItemCreate , ItemUpdate
from typing import List

router = APIRouter(
    prefix='/items',
    tags=["Items"]
)

#create 
@router.post('/' , response_model = Item , status_code = status.HTTP_201_CREATED)
def create_item(item: ItemCreate, session: Session = Depends(get_session)):
    db_item = Item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

#ReadAll

@router.get("/" , response_model=List[Item])
def get_items(session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    return items

# READ ONE                                       
@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
                                                                 
# UPDATE                                                       
@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemUpdate, session: Session = Depends(get_session)):                               
    item = session.get(Item, item_id)                          
    if not item:                                               
        raise HTTPException(status_code=404, detail="Item not found")                                                        
    for key, value in item_data.dict(exclude_unset=True).items():                    
        setattr(item, key, value)                      
    session.add(item)                                          
    session.commit()                                           
    session.refresh(item)                                      
    return item                                                
                                                                 
# DELETE                                                       
@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
def delete_item(item_id: int, session: Session = Depends(get_session)):                                         
    item = session.get(Item, item_id)                          
    if not item:                                               
        raise HTTPException(status_code=404, detail="Item not found")                                                        
    session.delete(item)                               
    session.commit()                                           
    return {"message": f"Item {item_id} deleted"} 