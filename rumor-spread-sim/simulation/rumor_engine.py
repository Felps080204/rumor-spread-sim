import random
from simulation.metrics import collect_metrics

def run_simulation(graph, agents, days=7):

    history = []
    metrics_history = []

    starter = random.choice(
        list(agents.keys())
    )

    agents[starter].belief_state = "believes"

    agents[starter].memory.add_memory(
        event="Rumor inicial recebido",
        importance=5,
        relevance=5,
        day=1
    )

    print(f"\n{starter} iniciou o rumor.\n")

    for day in range(1, days + 1):

        print("=" * 40)
        print(f"DIA {day}")
        print("=" * 40)

        for node in graph.nodes():

            agent = agents[node]

            if agent.belief_state != "believes":
                continue

            neighbors = list(
                graph.neighbors(node)
            )

            for neighbor_name in neighbors:

                target = agents[neighbor_name]

                if random.random() < 0.7:

                    target.receive_rumor(
                        rumor=f"Rumor vindo de {agent.name}",
                        sender=agent,
                        day=day
                    )

        states = {}

        for name, agent in agents.items():

            states[name] = (
                agent.belief_state
            )

            print(
                f"{name}: "
                f"{agent.belief_state}"
            )

        history.append(states)

        metrics = collect_metrics(
            agents
        )

        metrics_history.append(
            metrics
        )

        print("\nMétricas do dia:")

        print(
            f"Acreditam: "
            f"{metrics['believes']}"
        )

        print(
            f"Neutros: "
            f"{metrics['neutral']}"
        )

        print(
            f"Céticos: "
            f"{metrics['skeptical']}"
        )

        print()

    return history, metrics_history