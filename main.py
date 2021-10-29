from matplotlib.pyplot import cool
from networkx.algorithms.bipartite.basic import color
from graph import Graph
from evolutionary_algorithm import Algorithm
from random import randint

if __name__ == "__main__":
    graph = Graph(nodes=5, seed=1)
    algorithm = Algorithm(graph=graph, population_size=4, seed=1)

    actual_population = algorithm.initialize_randomly()
    print(actual_population)