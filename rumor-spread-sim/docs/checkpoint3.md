# Checkpoint 3 – Evolução da Implementação

## Funcionalidades Adicionadas

Durante o Checkpoint 3, o protótipo foi expandido para incorporar os principais conceitos apresentados na arquitetura de agentes generativos.

### Sistema de Memória

Foi implementada uma arquitetura de memória composta por:

* Memória episódica para armazenar eventos recebidos pelos agentes;
* Recuperação de memórias baseada em recência, importância e relevância;
* Armazenamento do histórico de interações durante toda a simulação.

### Sistema de Reflexão

Foi adicionado um mecanismo de reflexão capaz de gerar interpretações a partir das memórias recuperadas, influenciando o processo de atualização das crenças dos agentes.

### Perfis dos Agentes

Foram criados perfis individuais contendo níveis distintos de:

* Credulidade;
* Relevância social.

Essas características tornam os agentes mais ou menos suscetíveis ao rumor e influenciam sua capacidade de propagação.

### Atualização de Crenças

Os agentes passaram a recalcular seu estado com base nas memórias acumuladas, podendo assumir os estados:

* Believes;
* Neutral;
* Skeptical.

### Métricas da Simulação

Foi implementado um sistema de coleta de métricas para registrar diariamente:

* Quantidade de agentes que acreditam no rumor;
* Quantidade de agentes neutros;
* Quantidade de agentes céticos.

### Visualização dos Resultados

Foram adicionados:

* GIF animado mostrando a propagação do rumor ao longo dos dias;
* Coloração dos nós de acordo com o estado de crença;
* Gráfico temporal das métricas coletadas durante a simulação.

## Resultado

O sistema passou de uma simples propagação de rumor para uma simulação social baseada em agentes com memória, reflexão, influência social e visualização dos comportamentos emergentes observados durante a execução.
