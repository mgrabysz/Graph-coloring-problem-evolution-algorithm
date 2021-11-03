from graph import Set_Graph
import argparse
import json


def load_output_from_json(path):
    with open(path, 'r') as file_handle:
        data = json.load(file_handle)

        edges = data['graph edges']
        num_of_nodes = data['individual_size']
        color_scheme_numeric = data['final_individual_core']

        return edges, num_of_nodes, color_scheme_numeric


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Title of the plot")
    parser.add_argument("path", help="path to json file")
    args = parser.parse_args()

    edges, num_of_nodes, color_scheme_numeric = load_output_from_json(args.path)

    graph = Set_Graph(
        nodes=num_of_nodes,
        edges=edges,
        color_scheme_numeric=color_scheme_numeric
    )

    graph.draw(title=str(args.title), labels=True, save=False)
