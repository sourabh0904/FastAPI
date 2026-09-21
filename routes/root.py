from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix = "",
    tags = ["Root"],
)

@router.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"Hello": "World"}