from evolutionary_algorithm import evolutionary_algorithm
from graph import Graph

if __name__ == "__main__":

    my_graph = Graph(seed=1)
    edges = my_graph.edges()

    database, scheme = evolutionary_algorithm(
        iterations=200000,
        edges=edges,
    )

    database.write_to_json("First graph.json")
    my_graph.set_color_scheme(scheme.core)
    my_graph.draw("First graph", save=True)
