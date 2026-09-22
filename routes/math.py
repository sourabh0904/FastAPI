from fastapi import APIRouter , status , HTTPException , Depends
from pydantic import BaseModel , Field
from dependencies import verify_api_key

class NumberInput(BaseModel):
    a:int = Field(..., description="First number to be added and positive", json_schema_extra={"example": 5}, gt=0)        # Direct example passing is not supported in pydantic v1, so using json_schema_extra to provide example for OpenAPI documentation
    b:int = Field(..., description="Second number to be added and positive", json_schema_extra={"example": 10}, gt=0)

class AddResult(BaseModel): 
    result: int

class UpdateResult(BaseModel):
    a: int
    b: int

class DeleteResult(BaseModel):
    message: str


router = APIRouter(
    prefix="/math",
    tags=["Math"],
    dependencies=[Depends(verify_api_key)]
)

@router.post("/add" , response_model=AddResult , status_code=status.HTTP_200_OK )
def add_numbers(numbers: NumberInput):
    return AddResult(result=numbers.a + numbers.b)

@router.put("/update" , response_model=UpdateResult , status_code=status.HTTP_200_OK)
def update_numbers(numbers: NumberInput):
    return UpdateResult(a=numbers.a, b=numbers.b)

@router.delete("/delete" ,response_model=DeleteResult, status_code=status.HTTP_200_OK)
def delete_numbers(numbers: NumberInput):
    return DeleteResult(message=f"Deleted numbers: a={numbers.a}, b={numbers.b}")