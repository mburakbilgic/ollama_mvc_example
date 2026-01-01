[Fork this repository](https://github.com/mburakbilgic/ollama_mvc_example/fork)

# Ollama + FastAPI MVC Example (LLM & RAG)

## TÜRKÇE

Bu proje, **LLM tabanlı servislerin FastAPI üzerinde MVC (Model–View–Controller) mimarisi ile nasıl tasarlanabileceğini** göstermek amacıyla hazırlanmış **eğitsel bir örnek uygulamadır**.

Proje, bir kurs kapsamında öğrencilerin:

- LLM servislerini **backend mimarisiyle doğru şekilde konumlandırmasını**
- RAG (Retrieval Augmented Generation) akışını
- Request / Response ayrımını
- Worker katmanları ile iş mantığının soyutlanmasını
- Loglama, health-check ve environment kontrolü gibi **gerçek dünya ihtiyaçlarını**

net bir şekilde görebilmesi için geliştirilmiştir.

Bu repository **production-ready bir ürün değil**, **öğretici bir referans mimari** olarak tasarlanmıştır.

## Amaçlar

- FastAPI üzerinde **katmanlı mimari** öğretmek  
- LLM entegrasyonunu controller seviyesinden ayırmak  
- RAG sistemlerinin temel yapı taşlarını göstermek  
- Ollama üzerinden **local-first LLM kullanımını** örneklemek  
- Sağlam request / response sözleşmeleri oluşturmak  


## Mimari Genel Bakış

```
Client
  │
  ▼
Controller (API Layer)
  │
  ▼
View (Response Mapping)
  │
  ▼
Worker (Business Logic)
  │
  ▼
LLM / RAG / System Services
```
### Katmanlar

- **Controllers**
  - API endpoint tanımları
  - Request doğrulama
- **Models**
  - Pydantic Request / Response şemaları
- **Views**
  - Response mapping ve formatlama
- **Workers**
  - LLM çağrıları
  - RAG işlemleri
  - Health & Log işlemleri
- **Core**
  - Registry yapıları
  - Base sınıflar
- **Data**
  - Knowledge Base (Markdown)

## LLM & RAG Yapısı

- **Ollama** local LLM runtime olarak kullanılır
- Embedding işlemleri:
  - `nomic-embed-text`
- Generation:
  - Primary model: `steamdj/llama3.1-cpu-only`
  - Fallback model: `qwen2.5:0.5b-instruct`
- Retrieval:
  - cosine similarity
  - `sklearn NearestNeighbors`

## Sağlık ve Sistem Kontrolleri

- Servis erişilebilirlik kontrolü
- Ollama model durumu
- Log dosyası varlığı
- Environment & requirements doğrulaması
- Otomatik `pip install -r requirements.txt`

## Çalıştırma

```bash
pip install -r requirements.txt
python -m main
```

### API:
http://localhost:13456/

### Swagger
http://localhost:13456/docs

## Notlar

- Bu proje eğitim amaçlıdır
- Güvenlik, rate-limit ve auth içermez
- Büyük KB’ler için optimize edilmemiştir
- Async streaming örneği içermez (bilinçli olarak)

## Kimin İçin?

- Backend geliştiriciler
- LLM sistemleri öğrenen mühendisler
- FastAPI mimarisi öğrenmek isteyenler
- RAG sistemlerini ilk kez kuranlar

---
---

## ENGLISH

This project is an **educational example application** designed to demonstrate **how LLM-based services can be architected using the MVC (Model–View–Controller) pattern on top of FastAPI**.

The project was developed within the scope of a course to allow students to clearly understand:

- How to **properly position LLM services within a backend architecture**
- The Retrieval Augmented Generation (RAG) workflow
- The separation of Request / Response responsibilities
- Abstraction of business logic through Worker layers
- **Real-world requirements** such as logging, health checks, and environment validation

This repository is **not a production-ready product**, but rather a **teaching-oriented reference architecture**.

## Goals

- Teach **layered architecture** on FastAPI  
- Decouple LLM integration from the controller layer  
- Demonstrate the core building blocks of RAG systems  
- Showcase **local-first LLM usage** via Ollama  
- Establish robust request / response contracts  

## Architecture Overview
```
Client
  │
  ▼
Controller (API Layer)
  │
  ▼
View (Response Mapping)
  │
  ▼
Worker (Business Logic)
  │
  ▼
LLM / RAG / System Services
```

### Layers

- **Controllers**
  - API endpoint definitions
  - Request validation
- **Models**
  - Pydantic Request / Response schemas
- **Views**
  - Response mapping and formatting
- **Workers**
  - LLM calls
  - RAG operations
  - Health & Log operations
- **Core**
  - Registry structures
  - Base classes
- **Data**
  - Knowledge Base (Markdown)

## LLM & RAG Structure

- **Ollama** is used as the local LLM runtime
- Embedding operations:
  - `nomic-embed-text`
- Generation:
  - Primary model: `steamdj/llama3.1-cpu-only`
  - Fallback model: `qwen2.5:0.5b-instruct`
- Retrieval:
  - Cosine similarity
  - `sklearn NearestNeighbors`

## Health & System Checks

- Service availability check
- Ollama model status
- Log file existence
- Environment & requirements validation
- Automatic `pip install -r requirements.txt`

## Running the Project

```bash
pip install -r requirements.txt
python -m main
```

### API:
http://localhost:13456/

### Swagger
http://localhost:13456/docs

## Notes
- This project is intended for educational purposes
- No authentication, rate limiting, or security hardening is included
- Not optimized for large-scale knowledge bases
- Async streaming examples are intentionally omitted

## Who Is This For?
- Backend developers
- Engineers learning LLM systems
- Developers exploring FastAPI architecture
- Practitioners building their first RAG systems

[Fork this repository](https://github.com/mburakbilgic/ollama_mvc_example/fork)
