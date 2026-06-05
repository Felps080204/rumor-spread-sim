# Rumor Spread Simulation

# Descrição
O Rumor Spread Simulation é um projeto de simulação social baseado em agentes generativos inspirado no artigo Generative Agents (Park et al., 2023). O sistema busca reproduzir a propagação de rumores em uma pequena comunidade artificial, considerando fatores como memória, influência social e atualização de crenças.

Cada agente possui memória episódica, capacidade de reflexão e mecanismos de tomada de decisão que influenciam a disseminação de informações ao longo do tempo.

# Objetivo
Simular a propagação de um rumor em uma vila com 5–8 agentes conectados em rede, analisando:
- Velocidade de propagação;
- Influência social dos agentes;
- Evolução das crenças ao longo do tempo;
- Comportamentos emergentes gerados pelas interações.

# Tecnologias utilizadas
- Python
- LangChain
- NetworkX
- Matplotlib
- ImageIO

# Arquitetura da Simulação
A simulação segue o fluxo:
Rumor Inicial
      ↓
Memória Episódica
      ↓
Recência + Importância + Relevância
      ↓
Reflexão
      ↓
Atualização da Crença
      ↓
Compartilhamento
      ↓
Outros Agentes

# Funcionalidades implementadas 

# Agentes Generativos
- Perfis individuais de influência social;
- Sistema de credulidade;
- Estados de crença dinâmicos.

# Sistema de Memória
- Memória episódica;
- Recuperação baseada em recência;
- Recuperação baseada em importância;
- Recuperação baseada em relevância.

# Sistema de Reflexão
- Geração de reflexões a partir das experiências armazenadas;
- Influência das reflexões na atualização de crenças.

# Propagação do Rumor
- Compartilhamento entre agentes conectados;
- Evolução temporal da simulação;
- Atualização diária dos estados dos agentes.

# Visualização
- Geração automática de GIF;
- Rede social representada por grafos;
- Gráfico de métricas da propagação.

# Estrutura do projeto
agents/: definição dos agentes e sistema de memória;
simulation/: lógica da simulação e propagação;
visualization/: geração do grafo e GIF;
output/: visualização dos resultados gerados.

rumor-spread-sim/
│
├── agents/
│   ├── agent.py          
│   ├── memory.py         
│   ├── reflection.py     
│   └── profile.py        
│
├── simulation/
│   ├── environment.py    
│   ├── rumor_engine.py   
│   └── metrics.py        
│
├── visualization/
│   ├── graph_animation.py 
│   └── metrics_plot.py    
│
├── output/
│   ├── simulation.gif
│   └── metrics.png
│
├── docs/
│   ├── checkpoint2.md
│   └── references.md
│
├── main.py
├── requirements.txt
└── README.md

# Estados dos agentes
| Estado    | Significado           |
| --------- | --------------------- |
| believes  | acredita no rumor     |
| neutral   | estado neutro/incerto |
| skeptical | não acredita no rumor |

# Como executar
```bash
pip install -r requirements.txt
python main.py
```
# Saídas Geradas
Após a execução serão gerados:

output/
├── simulation.gif
└── metrics.png

# simulation.gif
Animação mostrando a propagação do rumor ao longo dos dias da simulação.

# metrics.png
Gráfico contendo a quantidade diária de agentes:
- Believes
- Neutral
- Skeptical