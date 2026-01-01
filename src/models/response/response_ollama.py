from typing import List
from src.core.base_response import BaseResponse



class ResponseOllamaModelList(BaseResponse):
    count: int
    models: List[str]



class ResponseOllamaPull(BaseResponse):
    model: str
    result: str
    


class ResponseOllamaError(BaseResponse):
    status: str = "error"
    message: str