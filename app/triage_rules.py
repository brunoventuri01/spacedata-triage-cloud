def classify_space_data(
    temperature: float,
    radiation_level: float,
    signal_noise_ratio: float,
    latency_ms: int,
    missing_fields: int
):
    """
    Regra simplificada de triagem de dados espaciais.

    A função recebe dados simulados de sensores orbitais e calcula um score de risco.
    Quanto maior o score, menor a confiabilidade do dado para análise.
    """

    risk_score = 0
    reasons = []

    if temperature < -20 or temperature > 85:
        risk_score += 25
        reasons.append("temperatura fora da faixa operacional esperada")

    if radiation_level > 0.75:
        risk_score += 25
        reasons.append("nível de radiação elevado")

    if signal_noise_ratio < 10:
        risk_score += 25
        reasons.append("baixa relação sinal-ruído")

    if latency_ms > 800:
        risk_score += 15
        reasons.append("latência elevada na transmissão")

    if missing_fields > 0:
        risk_score += 10
        reasons.append("campos ausentes no pacote de dados")

    if risk_score >= 70:
        classification = "RUIDO"
    elif risk_score >= 45:
        classification = "SUSPEITO"
    elif risk_score >= 25:
        classification = "CRITICO"
    else:
        classification = "UTIL"

    if not reasons:
        reasons.append("dados dentro dos parâmetros esperados para análise")

    return {
        "classification": classification,
        "score": round(risk_score / 100, 2),
        "reason": "; ".join(reasons)
    }
