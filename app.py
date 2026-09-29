from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np

app = FastAPI(
    title="API de Recomendação Adaptativa - Marketing Bancário (Multi-Armed Bandit)",
    description="Serviço demonstrável de recomendação de ofertas em tempo real utilizando Thompson Sampling e feedback contínuo.",
    version="1.0.0"
)

# Estado das distribuições Beta dos braços (Alpha = vitórias, Beta = insucessos)
# Inicializado com as taxas empíricas observadas na base histórica
arms_state = {
    "student": {"alpha": 31, "beta": 69},
    "retired": {"alpha": 25, "beta": 75},
    "unemployed": {"alpha": 14, "beta": 86},
    "admin.": {"alpha": 13, "beta": 87},
    "management": {"alpha": 11, "beta": 89},
    "technician": {"alpha": 10, "beta": 90},
    "unknown": {"alpha": 10, "beta": 90},
    "self-employed": {"alpha": 10, "beta": 90},
    "housemaid": {"alpha": 10, "beta": 90},
    "entrepreneur": {"alpha": 8, "beta": 92},
    "services": {"alpha": 8, "beta": 92},
    "blue-collar": {"alpha": 6, "beta": 94}
}

class ClientInput(BaseModel):
    age: int = Field(..., example=35)
    job: str = Field(..., example="student")
    marital: str = Field("single", example="single")

class FeedbackInput(BaseModel):
    job: str = Field(..., example="student")
    converted: int = Field(..., ge=0, le=1, description="1 se o cliente aceitou a oferta, 0 se recusou", example=1)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "Plataforma de Recomendação Adaptativa (Thompson Sampling)",
        "docs_url": "/docs"
    }

@app.post("/recommend")
def recommend_action(client: ClientInput):
    job = client.job.lower().strip()
    
    # Se a profissão existir no estado dos braços, amostra da distribuição Beta
    if job in arms_state:
        a = arms_state[job]["alpha"]
        b = arms_state[job]["beta"]
        # Thompson Sampling: sorteio da probabilidade a posteriori
        amostra_theta = float(np.random.beta(a, b))
        taxa_media = a / (a + b)
    else:
        amostra_theta = 0.10
        taxa_media = 0.10

    # Lógica de decisão de prioridade de contato
    if taxa_media >= 0.20:
        recomendacao = "Contato Prioritário (Alta propensão de conversão)"
        prioridade = 1
        canal_sugerido = "Ligação Direta do Gerente / Notificação Push Especial"
    elif taxa_media >= 0.10:
        recomendacao = "Contato Padrão (Média propensão de conversão)"
        prioridade = 2
        canal_sugerido = "E-mail Marketing / Banner no Internet Banking"
    else:
        recomendacao = "Baixa Prioridade (Baixa propensão - Evitar saturação de canal)"
        prioridade = 3
        canal_sugerido = "Nenhum contato imediato (Economia de orçamento)"

    return {
        "client_job": job,
        "expected_conversion_rate": f"{round(taxa_media * 100, 2)}%",
        "sampled_theta_thompson": round(amostra_theta, 4),
        "recommendation": recomendacao,
        "priority_level": prioridade,
        "suggested_channel": canal_sugerido
    }

@app.post("/feedback")
def update_feedback(feedback: FeedbackInput):
    job = feedback.job.lower().strip()
    
    if job not in arms_state:
        arms_state[job] = {"alpha": 1, "beta": 1}
        
    if feedback.converted == 1:
        arms_state[job]["alpha"] += 1
        status_msg = "Sucesso contabilizado: alpha incrementado!"
    else:
        arms_state[job]["beta"] += 1
        status_msg = "Recusa contabilizada: beta incrementado!"
        
    total = arms_state[job]["alpha"] + arms_state[job]["beta"]
    nova_taxa = arms_state[job]["alpha"] / total
    
    return {
        "message": "Feedback registrado com sucesso (Closed-Loop Update)",
        "job": job,
        "detail": status_msg,
        "current_alpha": arms_state[job]["alpha"],
        "current_beta": arms_state[job]["beta"],
        "updated_conversion_rate": f"{round(nova_taxa * 100, 2)}%"
    }

@app.get("/stats")
def get_stats():
    resumo = {}
    for job, dados in sorted(arms_state.items(), key=lambda x: x[1]["alpha"]/(x[1]["alpha"]+x[1]["beta"]), reverse=True):
        total = dados["alpha"] + dados["beta"]
        taxa = dados["alpha"] / total
        resumo[job] = {
            "taxa_conversao": f"{round(taxa * 100, 2)}%",
            "vitorias_alpha": dados["alpha"],
            "derrotas_beta": dados["beta"],
            "total_amostras": total
        }
    return {"arms_ranking": resumo}
