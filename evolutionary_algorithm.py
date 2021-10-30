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

# ===================================================================================


class Individual:
    def __init__(self, core):
        self.core = core        # list
        self.fitness = None     # integer

    def __str__(self):
        return str(self.core)


def initialize_randomly(population_size, individual_size, seed=None):
    """
    Returns randomly initiated population
    """
    random.seed(seed)
    population = []
    max_number = individual_size - 1

    for _ in range(population_size):
        individual_core = [
            randint(0, max_number) for _ in range(individual_size)
            ]
        individual = Individual(individual_core)
        population.append(individual)

    return population


def fitness(individual, individual_size, edges):
    """
    Funtion evaluates given individual.
    Fitness value equals to number of colors used in graph, therefore
    the smaller value is the better.
    Individuals which are not correct (connected nodes have the same
    color) are evaluated as n+1 where n is number of nodes
    """
    # check every pair of connected nodes (every edge)
    for (u, v) in edges:
        if individual.core[u] == individual.core[v]:
            return individual_size + 1

    # if individual is correct its fitness is number of different values
    a_set = set(individual.core)
    return len(a_set)


def reproduction(
    population,
    population_size,
    individual_size,
    edges,
    seed=None
):

    random.seed(seed)
    new_population = []
    for _ in range(population_size):
        opponent_1 = random.choice(population)
        opponent_2 = random.choice(population)
        fitness_1 = fitness(opponent_1, individual_size, edges)
        fitness_2 = fitness(opponent_2, individual_size, edges)

        if fitness_1 < fitness_2:
            # opponent_1 is better
            new_population.append(opponent_1)
        elif fitness_1 > fitness_2:
            # opponent 2 is better
            new_population.append(opponent_2)
        else:
            # opponents are equally good
            winner = random.choice([opponent_1, opponent_2])
            new_population.append(winner)

    return new_population
