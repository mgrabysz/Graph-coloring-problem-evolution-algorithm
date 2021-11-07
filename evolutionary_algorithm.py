from random import randint
import random
from database_io import Database
from copy import deepcopy
import time


class Individual:
    def __init__(self, core):
        self.core = core        # list
        self.fitness_rate = None     # integer

    def __str__(self):
        return str(self.core)

    def set_fitness_rate(self, new_fitness):
        self.fitness_rate = new_fitness

    def fitness_rate(self):
        return self.fitness_rate


def decision(probability):
    """
    Returns True with given probability (otherwise returns False)
    """
    return random.random() < probability


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
    num_of_incorrect_pairs = 0
    for (u, v) in edges:
        if individual.core[u] == individual.core[v]:
            num_of_incorrect_pairs += 1

    # if individual is correct its fitness is number of different values
    if num_of_incorrect_pairs == 0:
        a_set = set(individual.core)
        return len(a_set)
    else:
        return individual_size + num_of_incorrect_pairs


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
        fitness_1 = opponent_1.fitness_rate
        fitness_2 = opponent_2.fitness_rate

        if fitness_1 < fitness_2:
            # opponent_1 is better
            winner = deepcopy(opponent_1)
        elif fitness_1 > fitness_2:
            # opponent 2 is better
            winner = deepcopy(opponent_2)
        else:
            # opponents are equally good
            winner = deepcopy(random.choice([opponent_1, opponent_2]))

        new_population.append(winner)

    return new_population


def mutation(
    population,
    population_size,
    individual_size,
    mutation_ind_prob,
    mutation_elem_prob,
    seed=None
):
    """
    Function modifies given population (does not create a new one)
    mutation_ind_prob is probability of mutate given individual
    mutation_elem_prob is probability of modifying given element
    """

    def _mutate(individual, individual_size, prob):
        """
        Performs mutation of single individual
        """
        for i in range(len(individual.core)):
            if decision(prob):
                individual.core[i] = randint(0, individual_size-1)

    random.seed(seed)

    for individual in population:
        if decision(mutation_ind_prob):
            _mutate(individual, individual_size, mutation_elem_prob)


# =====================================================================


def evolutionary_algorithm(
    iterations,
    edges,
    population_size=20,
    individual_size=25,
    mutation_ind_prob=0.2,
    mutation_elem_prob=0.08,
    seed=None
):
    """
    Main fuction performing evolutionary algorithm
    """
    start = time.time()

    random.seed(seed)

    database = Database(
        population_size=population_size,
        individual_size=individual_size,
        mutation_ind_prob=mutation_ind_prob,
        mutation_elem_prob=mutation_elem_prob,
        iterations=iterations,
        edges=edges,
        seed=seed
    )

    current_population = initialize_randomly(
        population_size,
        individual_size,
        seed
    )
    current_best_individual = deepcopy(random.choice(current_population))
    current_best_fitness = fitness(
        current_best_individual,
        individual_size,
        edges)
    fitness_rates_sum = 0

    # finding the best individual
    for individual in current_population:

        fitness_rate = fitness(individual, individual_size, edges)
        individual.set_fitness_rate(fitness_rate)
        fitness_rates_sum += fitness_rate

        if fitness_rate < current_best_fitness:
            current_best_fitness = fitness_rate
            current_best_individual = deepcopy(individual)

    # save average fitness rate of actual population
    average_fitness = fitness_rates_sum / population_size
    database.add_log(average_fitness)

    # main loop
    for _ in range(iterations):

        if seed:
            seed = seed + 1

        # reproduction
        new_population = reproduction(
            population=current_population,
            population_size=population_size,
            individual_size=individual_size,
            edges=edges,
            seed=seed
        )

        # mutation
        mutation(
            population=new_population,
            population_size=population_size,
            individual_size=individual_size,
            mutation_ind_prob=mutation_ind_prob,
            mutation_elem_prob=mutation_elem_prob,
            seed=seed
        )

        # prepare to calculate average fitness of actual population
        fitness_rates_sum = 0

        # finding the best
        for individual in new_population:

            fitness_rate = fitness(individual, individual_size, edges)
            individual.set_fitness_rate(fitness_rate)
            fitness_rates_sum += fitness_rate

            if fitness_rate < current_best_fitness:
                current_best_fitness = fitness_rate
                current_best_individual = deepcopy(individual)

        # save average fitness rate of actual population
        average_fitness = fitness_rates_sum / population_size
        database.add_log(average_fitness)

        # replace population
        current_population = new_population

    # store data
    best_core = current_best_individual.core
    database.set_final_individual_core(best_core)
    database.set_final_individual_rate(current_best_fitness)

    end = time.time()
    duration = end - start
    database.set_time(duration)

    return database, current_best_individual
