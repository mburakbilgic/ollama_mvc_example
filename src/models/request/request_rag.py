from pydantic import Field
from typing import List
from src.core.base_request import BaseRequest



class RequestEmbedding(BaseRequest):
    texts: List[str] = Field(..., min_items=1)



class RequestRAG(BaseRequest):
    text: str
    k: int = Field(3, ge=1, le=10)



class RequestAnswer(BaseRequest):
    text: str
    target_lang: str = "Turkish"
    k: int = 3
    temperature: float = 0.2
