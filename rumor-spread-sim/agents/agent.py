from agents.memory import Memory
from agents.profile import PROFILES
from agents.reflection import generate_reflection

import random

class Agent:

    def __init__(self, name):

        self.name = name
        self.memory = Memory()

        self.credulity = (
            PROFILES[name]["credulity"]
        )

        self.relevance = (
            PROFILES[name]["relevance"]
        )

        self.belief_state = "neutral"

    def receive_rumor(
        self,
        rumor,
        sender,
        day
    ):

        importance = random.randint(2, 5)

        self.memory.add_memory(
            rumor,
            importance,
            sender.relevance,
            day
        )

        self.reflect(day)

        self.update_belief(day)

    def reflect(self, day):

        memories = (
            self.memory
            .retrieve_memories(day)
        )

        reflection = (
            generate_reflection(
                memories
            )
        )

        self.memory.add_reflection(
            reflection
        )

    def update_belief(self, day):

        memories = (
            self.memory
            .retrieve_memories(day)
        )

        if len(memories) == 0:
            return

        score = sum(
            memory["importance"]
            + memory["relevance"]
            for memory in memories
        )

        score += len(memories) * 2
        
        score *= self.credulity

        if score >= 15:

            self.belief_state = (
                "believes"
            )

        elif score >= 8:

            self.belief_state = (
                "neutral"
            )

        else:

            self.belief_state = (
                "skeptical"
            )

    def __str__(self):

        return (
            f"{self.name} - "
            f"{self.belief_state}"
        )