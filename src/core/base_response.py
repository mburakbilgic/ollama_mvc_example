from pydantic import BaseModel



class BaseResponse(BaseModel):
    
    class Config:
        extra: "ignore"
