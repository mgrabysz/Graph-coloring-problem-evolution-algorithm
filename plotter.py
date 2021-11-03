import matplotlib.pyplot as plt
import argparse
import json


def load_output_from_json(path):
    with open(path, 'r') as file_handle:
        data = json.load(file_handle)

        average_fitness_rates = data["fitness_rates"]
        iterations = [i for i in range(data["iterations"]+1)]
        return average_fitness_rates, iterations


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Title of the plot")
    parser.add_argument("path", help="path to json file")
    args = parser.parse_args()

    y, x = load_output_from_json(args.path)
    plt.plot(x, y)
    plt.ylabel("average fitness rate in population")
    plt.xlabel("iterations")
    plt.title(args.title)

    png_file = str(args.title) + '.png'
    plt.savefig(png_file)
    plt.show()
    plt.clf()
