class Memory:

    def __init__(self):
        self.episodic_memory = []
        self.reflections = []

    def add_memory(
        self,
        event,
        importance,
        relevance,
        day
    ):

        self.episodic_memory.append({
            "event": event,
            "importance": importance,
            "relevance": relevance,
            "day": day
        })

    def add_reflection(self, text):

        self.reflections.append(text)

    def retrieve_memories(self, current_day):

        scored = []

        for memory in self.episodic_memory:

            recency = 1 / (
                current_day -
                memory["day"] + 1
            )

            score = (
                recency +
                memory["importance"] +
                memory["relevance"]
            )

            scored.append(
                (score, memory)
            )

        scored.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        return [
            memory
            for score, memory
            in scored[:5]
        ]