from fastapi import FastAPI , status , HTTPException
from pydantic import BaseModel , Field

#pydantic models for request and respones bodies
class NumberInput(BaseModel):
    a:int = Field(..., description="First number to be added and positive", example=5 , gt=0)
    b:int = Field(..., description="Second number to be added and positive", example=10 , gt=0)

class AddResult(BaseModel): 
    result: int

class UpdateResult(BaseModel):
    a: int
    b: int

class DeleteResult(BaseModel):
    message: str

app = FastAPI()


@app.get("/" , status_code=status.HTTP_200_OK)
async def read_root():
    return {"Hello": "World"}

# @app.get("/about")
# def get_about():
#     return {'message' : 'about API'}


@app.post("/add" , response_model=AddResult , status_code=status.HTTP_200_OK)
def add_numbers(numbers: NumberInput):
    return AddResult(result=numbers.a + numbers.b)


@app.get("/about/{name}" , status_code=status.HTTP_200_OK)
def get_about(name: str):
    if not name.isalpha():
        raise HTTPException(status_code=400, detail="Name must contain only alphabetic characters.")
    return {"message": f"Hello, {name}!"}

@app.put("/update" , response_model=UpdateResult , status_code=status.HTTP_200_OK)
def update_numbers(numbers: NumberInput):
    return UpdateResult(a=numbers.a, b=numbers.b)

@app.delete("/delete" ,response_model=DeleteResult, status_code=status.HTTP_200_OK)
def delete_numbers(numbers: NumberInput):
    return DeleteResult(message=f"Deleted numbers: a={numbers.a}, b={numbers.b}")

    