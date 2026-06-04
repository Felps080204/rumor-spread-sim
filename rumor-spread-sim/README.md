# Rumor Spread Simulation

## Descrição
Este projeto implementa uma simulação social baseada em agentes generativos utilizando LLMs. O objetivo é analisar como rumores e informações falsas se propagam em uma pequena rede social composta por agentes com memória e capacidade de interação.

## Objetivo
Simular a propagação de um rumor em uma vila com 5–8 agentes conectados em rede, analisando:
- velocidade de propagação;
- influência social;
- mudança de crenças ao longo do tempo.

## Tecnologias utilizadas
- Python
- LangChain
- NetworkX
- Matplotlib
- ImageIO

## Funcionalidades implementadas até o momento
- Criação de agentes sociais;
- Rede social baseada em grafos;
- Sistema básico de crenças;
- Propagação de rumores;
- Simulação temporal;
- Geração automática de GIF da propagação.

## Estrutura do projeto
agents/: definição dos agentes e sistema de memória;
simulation/: lógica da simulação e propagação;
visualization/: geração do grafo e GIF;
output/: resultados gerados.

rumor-spread-sim/
│
├── agents/
│   ├── agent.py
│   ├── memory.py
│
├── simulation/
│   ├── environment.py
│   ├── rumor_engine.py
│
├── visualization/
│   ├── graph_animation.py
│
├── output/
│   ├── simulation.gif
│
├── docs/
│   ├── checkpoint2.md
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


## Como executar
```bash
pip install -r requirements.txt
python main.py
```
