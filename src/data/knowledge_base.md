# RAG Benchmark Knowledge Base

## 1. Terminology Glossary

### Machine Learning

**English:** machine learning\
**Turkish:** makine öğrenimi

Machine learning refers to computational methods that allow systems to
learn patterns from data without being explicitly programmed. In
benchmarking contexts, ML models are evaluated based on accuracy,
latency, robustness, and resource usage.

### Large Language Model (LLM)

Large Language Models are neural networks trained on vast text corpora
to generate, translate, summarize, and reason over language.

------------------------------------------------------------------------

## 2. Translation & Style Rules

-   Always use **formal Turkish**
-   Avoid colloquial language
-   Maintain technical accuracy
-   Preserve original meaning

------------------------------------------------------------------------

## 3. Brand & Product Naming Policy

-   **Do NOT translate brand names**
-   Examples:
    -   OpenAI → OpenAI
    -   NVIDIA → NVIDIA
    -   Ollama → Ollama

------------------------------------------------------------------------

## 4. Benchmarking Principles

### Reproducibility

All benchmark results must be reproducible using: - Fixed model
versions - Fixed prompts - Fixed datasets

### Fair Comparison

-   Same hardware class
-   Same context window
-   Same temperature & decoding parameters

------------------------------------------------------------------------

## 5. RAG-Specific Evaluation Criteria

### Retrieval Quality

-   Precision@K
-   Context relevance
-   Redundancy avoidance

### Generation Quality

-   Faithfulness to retrieved context
-   Hallucination resistance
-   Language consistency

------------------------------------------------------------------------

## 6. Health & System Checks

-   CUDA availability must be detected
-   CPU-only fallback must be supported
-   Disk-based KB sources (MD, CSV, SQL) must be validated

------------------------------------------------------------------------

## 7. Knowledge Base Source Policy

Supported KB formats: - Markdown (.md) - CSV - SQL databases (read-only)

Each document chunk must: - Be self-contained - Avoid ambiguous
references - Be deterministic

------------------------------------------------------------------------

## 8. Safety & Guardrails

-   Never fabricate benchmark results
-   If context is insufficient, respond with uncertainty
-   Do not invent performance metrics

------------------------------------------------------------------------

## 9. Prompt Construction Rules

-   Context must be explicitly injected
-   No hidden system assumptions
-   Deterministic ordering of context chunks

------------------------------------------------------------------------

## 10. Intended Usage

This knowledge base is designed for: - RAG benchmarking - LLM evaluation
tooling - Academic & engineering comparison studies

It is NOT intended for: - End-user conversational chatbots - Creative
writing - Open-ended speculation

------------------------------------------------------------------------
