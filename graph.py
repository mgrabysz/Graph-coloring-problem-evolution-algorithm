import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from random import sample

COLORS = list(colors._colors_full_map.values())


class MalformedParametersError(Exception):
    def __init__(self, power):
        super().__init__('These parameters are not correct')


class Graph:
    """
    Class Graph. Contains attributes:
    :param graph: networkx object
    :type graph: networkx.Graph

    :param number_of_nodes: number of nodes
    :type number_of_nodes: int

    :param edges: list of pairs of connected vertexes
    :type edges: list

    :param color_scheme: list of colors of adequate vertexes
    :type color_scheme: list[str]
    """
    def __init__(
        self,
        nodes=25,
        probability=0.1,
        color_scheme_numeric=None,
        seed=None
    ):

        self._graph = nx.erdos_renyi_graph(nodes, probability, seed=seed)
        self._number_of_nodes = nodes
        self._edges = self._graph.edges

        if color_scheme_numeric:

            if len(color_scheme_numeric) != nodes:
                raise MalformedParametersError

            self._color_scheme = self.color_scheme(color_scheme_numeric)

        else:
            self._color_scheme = None

    def set_color_scheme(self, new_color_scheme):

        if len(new_color_scheme) != self._number_of_nodes:
            raise MalformedParametersError

        self._color_scheme = new_color_scheme

    def color_scheme(self, color_scheme_numeric):

        shuffled_colors = sample(COLORS, self._number_of_nodes)
        color_scheme = [
            shuffled_colors[number] for number in color_scheme_numeric
            ]
        return color_scheme

    def draw(self, title, labels=False, show=True, save=False):

        if self._color_scheme:

            nx.draw_circular(
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
