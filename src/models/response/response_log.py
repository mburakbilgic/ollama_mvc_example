from typing import List
from src.core.base_response import BaseResponse



class ResponseLogList(BaseResponse):
    level: str
    count: int
    logs: List[str]



class ResponseLogLevelSet(BaseResponse):
    level: str
    message: str



class ResponseLogError(BaseResponse):
    status: str = "error"
    error: str
