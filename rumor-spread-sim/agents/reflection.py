def generate_reflection(memories):

    if len(memories) == 0:

        return (
            "Não tenho informações "
            "suficientes."
        )

    if len(memories) >= 3:

        return (
            "Este rumor apareceu "
            "várias vezes."
        )

    return (
        "Ainda não tenho certeza "
        "sobre este rumor."
    )