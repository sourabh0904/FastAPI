from fastapi import FastAPI
# from pydantic import BaseModel , Field
from routes.root import router as root_router
from routes.general import router as general_router
from routes.math import router as math_router
from fastapi.middleware.cors import CORSMiddleware

#pydantic models for request and respones bodies
# class NumberInput(BaseModel):
#     a:int = Field(..., description="First number to be added and positive", example=5 , gt=0)
#     b:int = Field(..., description="Second number to be added and positive", example=10 , gt=0)

# class AddResult(BaseModel): 
#     result: int

# class UpdateResult(BaseModel):
#     a: int
#     b: int

# class DeleteResult(BaseModel):
#     message: str

app = FastAPI(
    title="MY API (FastAPI)" , 
    openapi_tags=[{
        "name" : "Root" , 
        "description" : "Root endpoint for the API"
    },
    {
        "name" : "Math" ,
        "description" : "Mathematical operations"
    },
    {
        "name" : "General" ,
        "description" : "General endpoints"
    }
    ]

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# app = FastAPI()
app.include_router(root_router)
app.include_router(general_router)
app.include_router(math_router)


# @app.get("/" , status_code=status.HTTP_200_OK , tags=["Root"])
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/about")
# def get_about():
#     return {'message' : 'about API'}


# @app.post("/add" , response_model=AddResult , status_code=status.HTTP_200_OK , tags= ["Math"])
# def add_numbers(numbers: NumberInput):
#     return AddResult(result=numbers.a + numbers.b)


# @app.get("/about/{name}" , status_code=status.HTTP_200_OK , tags=["General"])
# def get_about(name: str):
#     if not name.isalpha():
#         raise HTTPException(status_code=400, detail="Name must contain only alphabetic characters.")
#     return {"message": f"Hello, {name}!"}

# @app.put("/update" , response_model=UpdateResult , status_code=status.HTTP_200_OK , tags=["Math"])
# def update_numbers(numbers: NumberInput):
#     return UpdateResult(a=numbers.a, b=numbers.b)

# @app.delete("/delete" ,response_model=DeleteResult, status_code=status.HTTP_200_OK , tags=["Math"])
# def delete_numbers(numbers: NumberInput):
#     return DeleteResult(message=f"Deleted numbers: a={numbers.a}, b={numbers.b}")