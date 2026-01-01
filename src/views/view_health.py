from src.core.model_registry import ModelRegistry as MR



async def resp_health_service(result):
    return MR.ResponseHealthService(**result)

async def resp_health_dependencies(result):
    return MR.ResponseHealthDependencies(**result)

async def resp_health_environment(result):
    return MR.ResponseHealthEnvironment(**result)

async def resp_health_autofix(result):
    return MR.ResponseHealthAutofix(**result)

async def resp_health_full(result):
    return MR.ResponseHealthFull(**result)