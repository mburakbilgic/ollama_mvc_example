import src
from fastapi import APIRouter
from src.views.view_health import (
    resp_health_service,
    resp_health_dependencies,
    resp_health_environment,
    resp_health_autofix,
    resp_health_full
)
from src.core.worker_registry import WorkerRegistry
from src.core.model_registry import ModelRegistry as MR

router = APIRouter(prefix="/health", tags=["health"])
worker = WorkerRegistry.health



@router.post("/service")
async def health_service(req: MR.RequestsHealthService):
    try:
        result = worker.func_service_check(req.host, req.port)
        return await resp_health_service(result)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}
    
@router.get("/dependencies")
async def health_dependencies():
    try:
        result = worker.func_dependencies_check()
        return await resp_health_dependencies(result)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}
    
@router.get("/environment")
async def health_environment():
    try:
        result = worker.func_environment_check()
        return await resp_health_environment(result)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}
    
@router.post("/environment/autofix")
async def health_environment_autofix():
    try:
        result = worker.func_environment_autofix()
        return await resp_health_autofix(result)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}


@router.post("/") # /health (prefix)
async def health_full(req: MR.RequestsHealthService):
    try:
        result = worker.func_full_check(req.host, req.port)
        return await resp_health_full(result)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}