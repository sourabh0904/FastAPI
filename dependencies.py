import os
from dotenv import load_dotenv
from fastapi import Header , HTTPException

load_dotenv()
API_KEY= os.getenv("API_KEY")

def verify_api_key(x_api_key: str = Header(...)):
    """Verify the provided API key against the expected value.""" 
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")