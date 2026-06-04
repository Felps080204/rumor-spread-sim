def collect_metrics(agents):

    metrics = {
        "believes": 0,
        "neutral": 0,
        "skeptical": 0
    }

    for agent in agents.values():

        metrics[
            agent.belief_state
        ] += 1

    return metrics