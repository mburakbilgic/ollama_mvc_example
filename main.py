# main.py
from fastapi import FastAPI

from src.controllers import controller_rag, controller_health, controller_log, controller_ollama

application = FastAPI()

application.include_router(controller_rag.router)
application.include_router(controller_health.router)
application.include_router(controller_log.router)
application.include_router(controller_ollama.router)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(application, host="0.0.0.0", port=13456)
    
# TODO: ALL
# 1. bütün yapıların response ve request mimarisiyle koşmasını sağlamak (log, ollama bunların bütün view/controller yapısı req resp ile çalışır hale getirilecek)
# DeepEval (bu arkadaşla promptlarınız, KB, ve üretilen yada gönderilen ctx[content] analizlerini yapar)
# Promptfoo (bu arkadaşla model dosyalarını hız ve güvenlik açısından test eder)
# Azure - prompt flow 