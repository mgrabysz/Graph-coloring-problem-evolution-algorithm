# import pytest
from evolutionary_algorithm import (
    Individual,
    initialize_randomly,
    fitness
)
from graph import Graph


def test_graph_getters():
    graph = Graph(nodes=5, seed=1)
    assert (2, 4) in graph.edges()
    assert (3, 4) in graph.edges()
    assert graph.number_of_nodes() == 5


def test_inizialize_randomly():
    actual_population = initialize_randomly(4, 5, 1)
    actual_population_cores = [i.core for i in actual_population]
    expected_population_cores = [
        [1, 4, 0, 2, 0],
        [3, 3, 3, 3, 1],
        [0, 3, 0, 3, 3],
        [4, 0, 3, 2, 1]
        ]
    assert actual_population_cores == expected_population_cores


def test_fitness():
    edges = [(2, 4), (3, 4)]
    individual = Individual([1, 2, 3, 4, 5])           # correct individual
    better_individual = Individual([1, 1, 1, 4, 5])
    malformed_individual = Individual([1, 2, 3, 4, 3])
    assert fitness(individual, 5, edges) == 5
    assert fitness(better_individual, 5, edges) == 3
    assert fitness(malformed_individual, 5, edges) == 6
