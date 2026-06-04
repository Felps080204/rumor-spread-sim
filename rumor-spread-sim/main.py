from simulation.environment import create_environment
from simulation.rumor_engine import run_simulation
from visualization.graph_animation import generate_gif
from visualization.metrics_plot import plot_metrics

def main():
    graph, agents = create_environment()

    history, metrics_history = run_simulation(
        graph,
        agents,
        days=7
    )

    generate_gif(
        graph,
        history
    )

    plot_metrics(
        metrics_history
    )

    print("Simulação finalizada.")
    print("GIF salvo em output/simulation.gif")
    print("Gráfico salvo em output/metrics.png")

if __name__ == "__main__":
    main()