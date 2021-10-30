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
        self.edges = graph.edges()
        self.population_size = population_size
        self.mutation_prob = mutation_prob
        self.population = []
        self.individual_size = graph.number_of_nodes()

    def initialize_randomly(self):
        """
        Returns randomly initiated population
        """
        population = []
        max_number = self.individual_size - 1

        for _ in range(self.population_size):
            individual = [
                randint(0, max_number) for _ in range(self.individual_size)
                ]
            population.append(individual)

        return population

    def fitness(self, individual):
        """
        Funtion evaluates given individual.
        Fitness value equals to number of colors used in graph, therefore
        the smaller value is the better.
        Individuals which are not correct (connected nodes have the same
        color) are evaluated as n+1 where n is number of nodes
        """
        # check every pair of connected nodes (every edge)
        for (u, v) in self.edges:
            if individual[u] == individual[v]:
                return self.individual_size + 1

        # if individual is correct its fitness is number of different values
        a_set = set(individual)
        return len(a_set)
