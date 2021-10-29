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
