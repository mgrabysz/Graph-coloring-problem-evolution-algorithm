# import pytest
from evolutionary_algorithm import Algorithm
from graph import Graph


def test_inizialize_randomly():
    graph = Graph(nodes=5, seed=1)
    algorithm = Algorithm(graph=graph, population_size=4, seed=1)

    actual_population = algorithm.initialize_randomly()
    expected_population = [
        [1, 4, 0, 2, 0],
        [3, 3, 3, 3, 1],
        [0, 3, 0, 3, 3],
        [4, 0, 3, 2, 1]
        ]
    assert actual_population == expected_population


def test_graph_getters():
    graph = Graph(nodes=5, seed=1)
    assert (2, 4) in graph.edges()
    assert (3, 4) in graph.edges()
    assert graph.number_of_nodes() == 5


def test_fitness():
    graph = Graph(nodes=5, seed=1)
    algorithm = Algorithm(graph=graph, population_size=4, seed=1)
    # edges = [(2, 4), (3, 4)]
    individual = [1, 2, 3, 4, 5]           # correct individual
    better_individual = [1, 1, 1, 4, 5]    # better individual
    malformed_individual = [1, 2, 3, 4, 3]
    assert algorithm.fitness(individual) == 5
    assert algorithm.fitness(better_individual) == 3
    assert algorithm.fitness(malformed_individual) == 6
