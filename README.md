# SpaceData Triage API

API desenvolvida para a disciplina de Secure DevOps Tools & Cloud Computing da Global Solution 2026.

## Objetivo

O SpaceData Triage simula uma camada de triagem de dados espaciais, classificando leituras de sensores orbitais como:

- UTIL
- CRITICO
- SUSPEITO
- RUIDO

## Conexão com a Indústria Espacial

Satélites e sensores orbitais geram grande volume de dados. Nem todo dado recebido é confiável para análise, pois pode apresentar ruído, latência elevada, falhas de leitura ou interferência por radiação.

A solução propõe uma API capaz de avaliar a qualidade desses dados antes de enviá-los para análise, armazenamento ou automação.

## Tecnologias

- Python
- FastAPI
- Azure App Service
- GitHub Actions
- Azure Key Vault
- Application Insights

## Endpoints

- GET /
- GET /health
- POST /triage
