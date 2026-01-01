from pydantic import BaseModel



class BaseRequest(BaseModel):
    
    class Config:
        extra: "forbid"
