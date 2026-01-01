from src.core.base_request import BaseRequest
from typing import Optional



class RequestLogList(BaseRequest):
    level: Optional[str] = None
    

class RequestLogLevelSet(BaseRequest):
    level: str