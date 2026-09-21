from fastapi import APIRouter , status , HTTPException

router = APIRouter(
    prefix="/general",
    tags=["General"]
)

@router.get("/about/{name}" , status_code=status.HTTP_200_OK )
def get_about(name: str):
    if not name.isalpha():
        raise HTTPException(status_code=400, detail="Name must contain only alphabetic characters.")
    return {"message": f"Hello, {name}!"}