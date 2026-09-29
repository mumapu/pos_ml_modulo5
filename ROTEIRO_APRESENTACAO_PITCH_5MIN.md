# Roteiro de Apresentação em Vídeo (Pitch de 5 Minutos)
## Datathon: Otimização Adaptativa de Campanhas de Marketing Bancário
**Pós-Tech FIAP - Machine Learning Engineering**

---

### Visão Geral e Dicas de Gravação
- **Tempo Total:** Exatos 5 minutos (300 segundos).
- **Formato:** Gravação de tela com câmera no canto (Loom, OBS Studio ou Zoom).
- **Postura:** Direto ao ponto, linguagem técnica balanceada com valor de negócio, ritmo dinâmico.
- **Divisão do Tempo:**
  - **Minuto 0:00 - 0:45** (45s): Introdução e Dores do Negócio
  - **Minuto 0:45 - 1:30** (45s): A Solução Adaptativa (Thompson Sampling vs Teste A/B)
  - **Minuto 1:30 - 2:15** (45s): Dados, Limpeza e Prevenção de Data Leakage
  - **Minuto 2:15 - 3:15** (60s): Resultados Experimentais, Regret e Golden Set
  - **Minuto 3:15 - 4:00** (45s): Demonstração Prática da API e MLOps (MLflow)
  - **Minuto 4:00 - 4:45** (45s): Arquitetura de Produção em Nuvem (AWS)
  - **Minuto 4:45 - 5:00** (15s): Fechamento e Impacto de Negócio

---

## Estrutura Minuto a Minuto

### [0:00 - 0:45] Bloco 1: O Problema de Negócio e o Custo do Desperdício
- **O que mostrar na tela:** Slide 1 e 2 do `apresentacao.html`.
- **Fala sugerida:**
  > "Olá! Sejam muito bem-vindos. Hoje apresento o projeto de Otimização Adaptativa de Campanhas de Marketing Bancário.
  > No setor financeiro, a aquisição de clientes via campanhas de telemarketing e canais digitais enfrenta dois grandes gargalos:
  > Primeiro: abordagens baseadas em regras fixas demoram semanas para perceber que um segmento de clientes não tem mais interesse no produto oferecido.
  > Segundo: os tradicionais testes A/B dividem o tráfego 50/50 por semanas, enviando milhares de ofertas para braços perdedores — gerando custo de oportunidade e fadiga de contato nos clientes.
  > Nosso objetivo neste projeto foi desenhar uma plataforma inteligente capaz de aprender em tempo real qual oferta tem maior propensão de conversão, equilibrando exploração e explotação."

---

### [0:45 - 1:30] Bloco 2: A Abordagem Algorítmica (Multi-Armed Bandit / Thompson Sampling)
- **O que mostrar na tela:** Slide 3 do `apresentacao.html`.
- **Fala sugerida:**
  > "Para resolver esse desafio, implementamos um algoritmo de **Multi-Armed Bandit** baseado em **Thompson Sampling** bayesiano.
  > Diferente de um modelo estático de classificação ou de um teste A/B ingênuo:
  > O Thompson Sampling modela a probabilidade de conversão de cada braço como uma distribuição Beta, parametrizada por vitórias (alpha) e insucessos (beta).
  > A cada contato, o algoritmo amostra a taxa de conversão a partir dessas distribuições a posteriori e escolhe a melhor oferta.
  > Com isso, conforme um segmento ou oferta demonstra alta conversão, o tráfego é direcionado dinamicamente para ele, enquanto ofertas de baixo retorno têm seu tráfego rapidamente reduzido, sem nunca serem eliminadas caso o mercado mude.
  > O resultado prático é a minimização direta do *Cumulative Regret*."

---

### [1:30 - 2:15] Bloco 3: Dados, Tratamento Crítico e Prevenção de Data Leakage
- **O que mostrar na tela:** Slide 4 do `apresentacao.html` ou `notebooks/01_EDA.ipynb`.
- **Fala sugerida:**
  > "Utilizamos a base real de Bank Marketing da Kaggle, contendo dados sociodemográficos, histórico de campanhas anteriores e indicadores macroeconômicos.
  > Aqui aplicamos um rigor técnico fundamental de Engenharia de Machine Learning: **prevenção contra Data Leakage**.
  > A feature `duration` (duração da chamada) possui altíssima correlação com a conversão final, porém ela é uma informação post-facto — você só sabe a duração da ligação *depois* que ela já aconteceu. Mantê-la criaria um modelo com acurácia artificialmente inflada e inútil em produção.
  > Nós removemos intencionalmente o atributo `duration`, realizamos One-Hot Encoding das variáveis categóricas de ocupação e educação, e preparamos os segmentos para alimentação do algoritmo adaptativo."

---

### [2:15 - 3:15] Bloco 4: Métricas de Avaliação, Regret Acumulado e Golden Set
- **O que mostrar na tela:** Slide 5 do `apresentacao.html` ou `notebooks/03_Baseline_and_Adaptive_Model.ipynb`.
- **Fala sugerida:**
  > "Para validar o ganho real, criamos um framework de experimentação rigoroso:
  > Comparando o Thompson Sampling contra uma política aleatória e uma política gulosa (Epsilon-Greedy fixo), o Thompson Sampling atingiu a menor curva de *Cumulative Regret*.
  > Ele convergiu para os segmentos de maior tração (como aposentados e estudantes) em menos de um terço das iterações exigidas por um teste A/B convencional, gerando um aumento relativo de conversão de mais de **35%** sobre o baseline ingênuo.
  > Além disso, criamos um **Golden Set** de validação determinística para garantir que a tomada de decisão obedece a regras de negócio e limites éticos — como priorizar segmentos responsivos e evitar saturação em clientes com baixa propensão."

---

### [3:15 - 4:00] Bloco 5: Serviço Demonstrável (FastAPI) e Rastreabilidade MLOps
- **O que mostrar na tela:** Swagger UI (`http://127.0.0.1:8000/docs`) executando `/recommend` e `/feedback`, seguido do **MLflow UI**.
- **Fala sugerida:**
  > "Para demonstrar o valor em produção, empacotamos o sistema em uma API de alta performance com **FastAPI**.
  > Aqui no endpoint `/recommend`, enviamos as características do cliente e a API retorna imediatamente a melhor oferta e a probabilidade amostrada em menos de 10 milissegundos.
  > No endpoint `/feedback`, registramos se o cliente aceitou ou recusou a oferta, disparando a atualização imediata dos parâmetros da distribuição Beta.
  > Todo o ciclo de vida dos experimentos, hiperparâmetros e métricas de conversão foi rastreado com **MLflow**, garantindo total reprodutibilidade, versionamento de artefatos e governança."

---

### [4:00 - 4:45] Bloco 6: Arquitetura-Alvo Robusta na Nuvem (AWS)
- **O que mostrar na tela:** Slide 7 do `apresentacao.html` ou diagrama Mermaid no `README.md`.
- **Fala sugerida:**
  > "Para suportar a escala de milhões de clientes de uma instituição financeira, desenhamos uma arquitetura de referência robusta na **AWS**:
  > - Na borda, **AWS WAF e CloudFront** garantem segurança perimetral e mitigação de ataques.
  > - O serviço de decisão roda conteinerizado no **Amazon ECS Fargate** com auto-scaling e fallback para *Graceful Degradation* caso haja timeout.
  > - Os parâmetros do Bandit residem em um cluster **Amazon ElastiCache Redis** para leitura sub-milissegundo.
  > - O feedback de conversão é ingerido via **Amazon Kinesis Data Streams** e processado por **AWS Lambdas**, garantindo que o modelo aprenda de forma contínua e assíncrona.
  > - Toda a telemetria vai para um Data Lakehouse no **Amazon S3** em camadas Bronze, Silver e Gold, com monitoramento contínuo de Data e Concept Drift pelo **Amazon SageMaker Model Monitor**."

---

### [4:45 - 5:00] Bloco 7: Conclusão e Encerramento
- **O que mostrar na tela:** Slide 8 do `apresentacao.html`.
- **Fala sugerida:**
  > "Em resumo: saímos de uma abordagem reativa e estática para uma plataforma de experimentação contínua que aprende com cada interação do usuário.
  > Entregamos código modular, prevenção de vazamento de dados, API funcional, rastreamento MLOps e uma arquitetura enterprise pronta para implantação.
  > Muito obrigado a todos pela atenção!"
