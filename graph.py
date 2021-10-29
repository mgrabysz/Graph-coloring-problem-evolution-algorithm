import networkx as nx
import matplotlib.pyplot as plt


class MalformedParametersError(Exception):
    def __init__(self, power):
        super().__init__('These parameters are not correct')


class Graph:

    def __init__(self, nodes=25, probability=0.1, color_scheme=None, seed=None):
        self._graph = nx.erdos_renyi_graph(nodes, probability, seed=seed)

        if color_scheme:
            if len(color_scheme) != nodes:
                raise MalformedParametersError

        self._color_scheme = color_scheme

    def draw(self, title, labels=False, show=True, save=False):

        if self._color_scheme:
            nx.draw_networkx(
                self._graph,
                node_color=self._color_scheme,
                with_labels=labels
                )
        else:
            nx.draw_circular(self._graph, with_labels=labels)

        plt.title(title)

        if show:
            plt.show()
        if save:
            png_file = title + '.png'
            plt.savefig(png_file)

        plt.clf()
