from src.core.model_registry import ModelRegistry as MR



async def resp_tr_generator_embedding(embeddings):
    return MR.ResponseEmbedding(embeddings=embeddings)


async def resp_tr_generator_rag(rags, ctx_rows):
    return MR.ResponseRAG(rags=rags, ctx_rows=ctx_rows)


async def resp_tr_generator_answer(answer, context):
    return MR.ResponseAnswer(answers=answer, context=context)