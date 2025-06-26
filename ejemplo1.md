---
title: "Desarrollo de LLM Autohosteados y Endpoints Privados para RAG"
author: "Facundo Gilles"
date: 2025-06-25
theme: Amurmaple
output:
  beamer_presentation:
    slide_level: 2
    incremental: true
    keep_tex: true
    sidebar: true
header-includes:
  - \usepackage{amsmath}
  - \usepackage{graphicx}
  - \usepackage{listings}
  - \usepackage{hyperref}
  - \useoutertheme{miniframes}
  - \setbeamertemplate{navigation symbols}{}
  - \colorlet{ochre}{black!30!yellow!70!}
---

# Fase 1: Infraestructura de Ejecución

## Objetivo
Garantizar que el modelo se ejecute en tu propia infraestructura, sin enviar inputs a terceros.

## Pasos
- **Adquisición de hardware (local o GPU cloud privada)**
  - Ej.: RTX 4090, A100, H100
  - Alternativas: Paperspace, Lambda Labs, OVHcloud
- **Configuración del entorno base**
  - OS: Ubuntu 22.04
  - Docker + NVIDIA Container Toolkit
  - Instalación de: `transformers`, `vllm`, `llama.cpp`, `text-generation-webui`, `exllama`
- **Modelo**
  - Descargar: Mistral 7B, LLaMA 3, DeepSeek, Falcon
  - Conversión opcional a GGUF, AWQ, Exllama

# Fase 2: Vector Store + Recuperación Local

## Objetivo
Mantener todo el pipeline RAG bajo control propio.

## Pasos
- **Ingesta y chunking de documentos**
  - Herramientas: `langchain`, `llama-index`, `haystack`
  - Fragmentación: 200–500 tokens por chunk
- **Indexación**
  - Vector store: `FAISS`, `Weaviate`, `Qdrant`, `Chroma`
  - Embeddings locales: `all-MiniLM`, `bge-small`, `nomic-embed-text`
- **Orquestación**
  - Backend en FastAPI, Flask o LangServe:
    - Recibe consulta
    - Recupera contexto relevante
    - Arma prompt y lo pasa al modelo

# Fase 3: Servir el Modelo por Endpoint Privado

## Objetivo
Exponer un endpoint de inferencia sin salir de la red propia.

## Pasos
- **Servidor de inferencia**
  - Usar `vllm`, `llama.cpp`, `text-generation-inference`, `Exllama Server`
  - Exponer API HTTP o WebSocket
- **Aislamiento de red**
  - Red privada LAN o túnel cifrado (WireGuard, Tailscale)
  - Evitar exposición de puertos sin autenticación
- **Contenedores (opcional)**
  - Dockerizar cada componente
  - Orquestar con `docker-compose` o Kubernetes

# Fase 4: Auditoría y Seguridad

## Objetivo
Garantizar que ningún dato salga del entorno controlado.

## Pasos
- **Firewall**
  - Bloqueo estricto de tráfico saliente no necesario
- **Logs y monitoreo**
  - Registro de accesos e inferencias
- **Validación del aislamiento**
  - Herramientas: `tcpdump`, `nethogs`, `iftop`

# Resultado

- Todos los datos (documentos, vectores, contexto) permanecen en tu infraestructura.
- La inferencia se realiza sin compartir inputs con servicios externos.
- Seguridad reforzada por aislamiento de red, monitoreo y control de tráfico.

