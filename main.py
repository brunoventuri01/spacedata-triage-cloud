from fastapi import FastAPI
from pydantic import BaseModel, Field
from triage_rules import classify_space_data


app = FastAPI(
    title="SpaceData Triage API",
    description="API para triagem de qualidade de dados espaciais simulados.",
    version="1.0.0"
)


class SpaceDataInput(BaseModel):
    satellite_id: str = Field(..., example="SAT-001")
    temperature: float = Field(..., example=72.5)
    radiation_level: float = Field(..., example=0.82)
    signal_noise_ratio: float = Field(..., example=14.3)
    latency_ms: int = Field(..., example=920)
    missing_fields: int = Field(..., example=0)


@app.get("/")
def home():
    return {
        "product": "SpaceData Triage",
        "description": "Plataforma de triagem e priorização de dados espaciais.",
        "problem": "Satélites e sensores orbitais geram grande volume de dados, mas nem todos são confiáveis para análise.",
        "solution": "A API classifica dados simulados como UTIL, SUSPEITO, CRITICO ou RUIDO.",
        "space_connection": "A solução simula uma camada de software usada para validar telemetria e dados orbitais antes de análise ou tomada de decisão.",
        "ods": [
            "ODS 9 - Indústria, Inovação e Infraestrutura",
            "ODS 13 - Ação contra a mudança global do clima"
        ],
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "online",
        "service": "SpaceData Triage API"
    }


@app.post("/triage")
def triage(data: SpaceDataInput):
    result = classify_space_data(
        temperature=data.temperature,
        radiation_level=data.radiation_level,
        signal_noise_ratio=data.signal_noise_ratio,
        latency_ms=data.latency_ms,
        missing_fields=data.missing_fields
    )

    return {
        "satellite_id": data.satellite_id,
        "classification": result["classification"],
        "score": result["score"],
        "reason": result["reason"]
    }
