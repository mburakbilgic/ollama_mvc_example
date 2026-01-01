import src
from fastapi import APIRouter
from src.views.view_rag import (
    resp_tr_generator_embedding,
    resp_tr_generator_rag,
    resp_tr_generator_answer
)
from src.core.worker_registry import WorkerRegistry
from src.core.model_registry import ModelRegistry as MR

router = APIRouter(prefix="/gen", tags=["gen"])
worker = WorkerRegistry.rag


@router.post("/embedding/tr") 
async def tr_generator_embedding(req: MR.RequestEmbedding):
    try:
        embeddings = worker.func_emb_gen_tr(req.texts)
        return await resp_tr_generator_embedding(embeddings)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}


@router.post("/rag/tr")
async def tr_generator_rag(req: MR.RequestRAG):
    try:
        ctx = worker.func_rag_gen_tr(req.text, req.k)
        return await resp_tr_generator_rag(ctx, ctx)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}


@router.post("/translator/tr")
async def tr_generator_answer(req: MR.RequestAnswer):
    try:
        answer, ctx = worker.func_answer_gen_tr(
            req.text,
            req.target_lang,
            req.k,
            req.temperature
        )
        return await resp_tr_generator_answer(answer, ctx)
    except Exception as e:
        src.logger.error(str(e))
        return {"error": str(e)}
