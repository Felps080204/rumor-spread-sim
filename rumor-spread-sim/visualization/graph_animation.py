import networkx as nx
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

def generate_gif(graph, history):
    os.makedirs("output", exist_ok=True)

    images = []

    pos = {
    "Erik": (0, 2),
    "Felipe": (-1.5, 1),
    "Gabriel": (1.5, 1),
    "Pedro Henrique": (-1.5, -1),
    "Pedro Octavio": (1.5, -1),
    "Douglas": (0, -2)
}

    for i, states in enumerate(history):
        plt.figure(figsize=(8, 6))

        colors = []

        for node in graph.nodes():
            state = states[node]

            if state == "believes":
                colors.append("red")
            elif state == "neutral":
                colors.append("yellow")
            else:
                colors.append("blue")

        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_color=colors,
            node_size=2000,
            font_size=11,
            font_weight="bold"
        )

        plt.title(
            f"Propagação do Rumor - Dia {i + 1}",
            fontsize=16,
            pad=20
        )
       
        filename = f"output/frame_{i}.png"

        plt.savefig(
            filename,
            bbox_inches="tight"
        )

        plt.close()

        images.append(imageio.imread(filename))

    imageio.mimsave(
        "output/simulation.gif",
        images,
        duration=5000
    )

    for i in range(len(history)):
        os.remove(f"output/frame_{i}.png")