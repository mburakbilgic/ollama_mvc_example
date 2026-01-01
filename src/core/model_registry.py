## REQUESTS
from src.models.request.request_rag import (
    RequestEmbedding,
    RequestRAG,
    RequestAnswer
)

from src.models.request.request_ollama import (
    RequestOllamaPull
)

from src.models.request.request_log import (
    RequestLogList,
    RequestLogLevelSet
)

from src.models.request.request_health import (
    RequestsHealthService
)

## RESPONSES
from src.models.response.response_rag import (
    ResponseEmbedding,
    ResponseRAG,
    ResponseAnswer
)

from src.models.response.response_ollama import (
    ResponseOllamaModelList,
    ResponseOllamaPull,
    ResponseOllamaError
)

from src.models.response.response_log import (
    ResponseLogList,
    ResponseLogLevelSet,
    ResponseLogError
)

from src.models.response.response_health import (
    ResponseHealthService,
    ResponseHealthDependencies,
    ResponseHealthEnvironment,
    ResponseHealthAutofix,
    ResponseHealthFull
)


class ModelRegistry:
    RequestEmbedding = RequestEmbedding    
    RequestRAG = RequestRAG
    RequestAnswer = RequestAnswer
    RequestOllamaPull = RequestOllamaPull
    RequestLogList = RequestLogList
    RequestLogLevelSet = RequestLogLevelSet
    RequestsHealthService = RequestsHealthService
    
    ResponseEmbedding = ResponseEmbedding
    ResponseRAG = ResponseRAG
    ResponseAnswer = ResponseAnswer
    ResponseOllamaModelList = ResponseOllamaModelList
    ResponseOllamaPull = ResponseOllamaPull
    ResponseOllamaError = ResponseOllamaError
    ResponseLogList = ResponseLogList
    ResponseLogLevelSet = ResponseLogLevelSet
    ResponseLogError = ResponseLogError
    ResponseHealthService = ResponseHealthService
    ResponseHealthDependencies = ResponseHealthDependencies
    ResponseHealthEnvironment = ResponseHealthEnvironment
    ResponseHealthAutofix = ResponseHealthAutofix
    ResponseHealthFull = ResponseHealthFull