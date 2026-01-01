from typing import List
from src.core.base_response import BaseResponse



class ResponseEmbedding(BaseResponse):
    embeddings: List[List[float]]



class ResponseRAG(BaseResponse):
    rags: List[str]
    ctx_rows: List[str]



class ResponseAnswer(BaseResponse):
    answers: str
    context: List[str]
