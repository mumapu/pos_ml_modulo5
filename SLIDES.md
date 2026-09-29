# Slides da Apresentação (Pitch de 5 Minutos)
## Datathon: Otimização Adaptativa de Campanhas de Marketing Bancário
**Pós-Tech FIAP - Machine Learning Engineering**

> **Dica:** Abra o arquivo [apresentacao.html](file:///Users/murillo/Documents/FIAP/ML/Módulo%205/TrabalhoFinal/apresentacao.html) no navegador para usar os slides com design interativo, tema escuro, métricas visuais e controle por teclado.

---

### Slide 1: Capa
- **Título:** Otimização Adaptativa de Campanhas de Marketing Bancário
- **Subtítulo:** Maximizando conversão e receita através de Multi-Armed Bandit (Thompson Sampling) e MLOps em Nuvem
- **Evento:** Datathon Pós-Tech FIAP • Módulo de Machine Learning Engineering

---

### Slide 2: O Problema de Negócio (0:00 - 0:45)
- Regras estáticas demoram para reagir (conversão média < 11%).
- Teste A/B clássico (50/50) desperdiça metade do tráfego em ofertas perdedoras.
- Solução: Experimentação contínua com Multi-Armed Bandit.

---

### Slide 3: A Abordagem Algorítmica (0:45 - 1:30)
- Thompson Sampling Bayesiano modelando cada braço como Beta(alpha, beta).
- Exploração proporcional à incerteza da distribuição.
- Minimização direta do *Cumulative Regret*.

---

### Slide 4: Engenharia de Dados & Anti-Leakage (1:30 - 2:15)
- Remoção intencional da coluna `duration` (Data Leakage temporal).
- One-Hot Encoding e pré-processamento robusto.
- Golden Set de 5 clientes com regras éticas de crédito.

---

### Slide 5: Resultados & Validação (2:15 - 3:15)
- Baseline Aleatório: 11.2% | Baseline Epsilon-Greedy: 13.8%.
- **Thompson Sampling: 15.4% (+37% de ganho relativo)**.
- Redução de **42% no Cumulative Regret**.

---

### Slide 6: Serviço Demonstrável & MLOps (3:15 - 4:00)
- API FastAPI: `POST /recommend`, `POST /feedback` e `GET /stats` (< 10ms).
- Rastreamento e governança com MLflow.

---

### Slide 7: Arquitetura em Nuvem (AWS) (4:00 - 4:45)
- AWS WAF + CloudFront + API Gateway.
- ECS Fargate Multi-AZ com Circuit Breaker e Graceful Degradation (< 25ms).
- ElastiCache Redis (< 2ms) + Kinesis/Lambda para closed-loop feedback.
- SageMaker Model Monitor para Concept & Data Drift.

---

### Slide 8: Conclusão & Impacto (4:45 - 5:00)
- Maior conversão, menor custo de aquisição e proteção contra fadiga de leads.
- Arquitetura corporativa pronta para produção em ambiente regulado bancário.
