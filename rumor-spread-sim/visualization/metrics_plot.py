import matplotlib.pyplot as plt

def plot_metrics(history):

    believes = []
    neutral = []
    skeptical = []

    for day in history:

        believes.append(
            day["believes"]
        )

        neutral.append(
            day["neutral"]
        )

        skeptical.append(
            day["skeptical"]
        )

    plt.figure(figsize=(8,5))

    plt.plot(
        believes,
        label="Believes"
    )

    plt.plot(
        neutral,
        label="Neutral"
    )

    plt.plot(
        skeptical,
        label="Skeptical"
    )

    plt.xlabel("Dias")
    plt.ylabel("Agentes")

    plt.legend()

    plt.savefig(
        "output/metrics.png"
    )

    plt.close()