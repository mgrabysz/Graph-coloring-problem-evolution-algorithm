from random import randint
import random


class Algorithm:

    def __init__(
        self,
        graph,
        population_size=20,
        mutation_prob=0.05,
        seed=None
    ):
        random.seed(seed)
        self.graph = graph
        self.population_size = population_size
        self.mutation_prob = mutation_prob
        self.population = []
        self.individual_size = graph.number_of_nodes()

    def initialize_randomly(self):

        population = []
        max_number = self.individual_size - 1

        for _ in range(self.population_size):
            individual = [
                randint(0, max_number) for _ in range(self.individual_size)
                ]
            population.append(individual)

        return population
