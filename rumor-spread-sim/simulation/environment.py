import networkx as nx
from agents.agent import Agent

def create_environment():
    graph = nx.Graph()

    names = [
        "Erik",
        "Felipe",
        "Gabriel",
        "Pedro Henrique",
        "Pedro Octavio",
        "Douglas"
    ]

    agents = {}

    for name in names:
        agents[name] = Agent(name)
        graph.add_node(name)

    connections = [
        ("Erik", "Felipe"),
        ("Erik", "Gabriel"),
        ("Felipe", "Pedro Henrique"),
        ("Gabriel", "Pedro Octavio"),
        ("Pedro Henrique", "Douglas"),
        ("Pedro Octavio", "Douglas")
    ]

    graph.add_edges_from(connections)

    return graph, agents