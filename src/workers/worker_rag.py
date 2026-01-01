import os
import src
import numpy as np
from typing import List, Tuple
from sklearn.neighbors import NearestNeighbors
from src.core.base_worker import BaseWorker



class RagWorker(BaseWorker):
    
    def __init__(self):
        super().__init__()
        self.ollama = src.ollama        
        self.KB_DOCS = self._load_kb()
        if not self.KB_DOCS:
            raise RuntimeError("Knowledge Base is empty or could not be loaded.")
        self.knn = None
        self.emb = None
        
    # ----- INERNAL UTILS ----- #    
    def _load_kb(self) -> List[str]:
        path = src.KB_PATH
        
        if not os.path.exists(path):
            src.logger.error(f"KB file not found: {path}")
            return []
        
        if src.KB_FORMAT == "md":
            return self._load_md(path)
        
        raise ValueError(f"Unsupported KB_FORMAT: {src.KB_FORMAT}")
    
    def _load_md(self, path:str) -> List[str]:
        docs = []
        
        with open (path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    docs.append(line)
        
        return docs
        
    def _l2norm(self, x: np.ndarray) -> np.ndarray:
        return x / (np.linalg.norm(x, axis=1, keepdims=1) + 1e-12)
    
    def _build_index(self):
        vectors = []
        
        for doc in self.KB_DOCS:
            vec = self.ollama.embed(src.EMBED_MODEL, doc)
            vectors.append(vec)
        
        emb = self._l2norm(np.array(vectors, dtype=np.float32))
        
        knn = NearestNeighbors(
            n_neighbors=min(3, len(self.KB_DOCS)),
            metric="cosine"
        )
        
        knn.fit(emb)
        
        return knn, emb
    
    def _ensure_index(self):
        if self.knn is None:
            self.knn, self.emb = self._build_index()
            
    # ----- PUBLIC WORKER METHODS ----- #
    def func_emb_gen_tr(self, texts: List[str]) -> List[List[float]]:
        """ 
        Batch embedding helper (Worker-level loop)
        """
        vectors = []
        
        for text in texts: # ["bir", "cümleyi", "bizler", "için", "parçalıyor"]
            vec = self.ollama.embed(src.EMBED_MODEL, text)
            vectors.append(vec)
        
        emb = self._l2norm(np.array(vectors, dtype=np.float32))
        
        return emb.tolist()

    def func_rag_gen_tr(self, text:str, k:int) -> List[str]:
        self._ensure_index()
        
        qv_raw = self.ollama.embed(src.EMBED_MODEL, text)
        qv = self._l2norm(np.array([qv_raw], dtype=np.float32))
        
        _, idx = self.knn.kneighbors(qv, n_neighbors=min(k, len(self.KB_DOCS)))
        return [self.KB_DOCS[i] for i in idx[0]]
    
    def func_answer_gen_tr(
        self,
        text:str,
        target_lang:str,
        k:int,
        temperature:float
    ) -> Tuple[str, List[str]]:        
        ctx = self.func_rag_gen_tr(text, k)        
        prompt = (
            "Context:\n-" + 
            "\n- ".join(ctx) +
            f"\n\nTranslate to {target_lang}:\n{text}"
        )
        
        try:
            out = self.ollama.generate(
                src.PRIMARY_LLM,
                prompt,
                temperature
            )
            if not out.strip():
                raise RuntimeError("Empty Response")
        except Exception:
            out = self.ollama.generate(
                src.FALLBACK_LLM,
                prompt, 
                temperature
            )
            
        return out.strip(), ctx
    
    
