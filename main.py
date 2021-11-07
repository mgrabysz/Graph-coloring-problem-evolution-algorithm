from evolutionary_algorithm import evolutionary_algorithm
from graph import Graph
import json
import statistics
import argparse

if __name__ == "__main__":

    my_graph = Graph(seed=1)
    edges = my_graph.edges()

    edges = [
        (0, 1),
        (2, 3),
        (4, 5),
        (6, 7),
        (8, 9),
        (10, 11),
        (12, 13),
        (14, 15),
        (16, 17),
        (18, 19),
        (20, 21),
        (22, 23)
        ]

    database, best_individual = evolutionary_algorithm(
        iterations=25000,
        edges=edges,
        mutation_elem_prob=0.04
    )

    database.write_to_json("Bipartite_graph.json")

    # =======================================================

    # parser = argparse.ArgumentParser()
    # parser.add_argument("title")
    # parser.add_argument("iterations")
    # parser.add_argument("population_size")
    # parser.add_argument("mutation_ind_prob")
    # parser.add_argument("mutation_elem_prob")
    # args = parser.parse_args()

    # my_graph = Graph(
    #     seed=1,
    # )
    # edges = my_graph.edges()

    # # bipartite graph
    # edges = [
    #     (0, 1),
    #     (2, 3),
    #     (4, 5),
    #     (6, 7),
    #     (8, 9),
    #     (10, 11),
    #     (12, 13),
    #     (14, 15),
    #     (16, 17),
    #     (18, 19),
    #     (20, 21),
    #     (22, 23)
    #     ]

    # # parameters
    # iterations = int(args.iterations)
    # population_size = int(args.population_size)
    # mutation_ind_prob = float(args.mutation_ind_prob)
    # mutation_elem_prob = float(args.mutation_elem_prob)

    # path = args.title + ".json"

    # best_rates = []
    # times = []

    # for _ in range(25):
    #     database, best = evolutionary_algorithm(
    #         iterations=iterations,
    #         edges=edges,
    #         population_size=population_size,
    #         mutation_ind_prob=mutation_ind_prob,
    #         mutation_elem_prob=mutation_elem_prob
    #     )

    #     best_rate = database.final_individual_rate
    #     time = database.time
    #     best_rates.append(best_rate)
    #     times.append(time)

    # min_val = min(best_rates)
    # max_val = max(best_rates)
    # standard_deviation = statistics.stdev(best_rates)
    # mean_val = statistics.mean(best_rates)
    # mean_time = statistics.mean(times)

    # data = {
    #         'population_size': population_size,
    #         'mutation_ind_prob': mutation_ind_prob,
    #         'mutation_elem_prob': mutation_elem_prob,
    #         'iterations': iterations,
    #         'min_val': min_val,
    #         'max_val': max_val,
    #         'standard_deviation': standard_deviation,
    #         'mean_val': mean_val,
    #         'mean_time': mean_time
    #     }

    # with open(path, 'w') as file_handle:
    #     json.dump(data, file_handle, indent=4)

