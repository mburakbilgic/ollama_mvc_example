from src.core.base_request import BaseRequest


class RequestsHealthService(BaseRequest):
    host: str = "127.0.0.1"
    port: int = 13456
