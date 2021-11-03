import json


class Database:
    """
    Class holds parameteres about execution of evolurtionary algorithm
    """
    def __init__(
        self,
        population_size,
        individual_size,
        mutation_ind_prob,
        mutation_elem_prob,
        iterations,
        edges,
        seed=None
    ):
        self.population_size = population_size
        self.individual_size = individual_size
        self.mutation_ind_prob = mutation_ind_prob
        self.mutation_elem_prob = mutation_elem_prob
        self.iterations = iterations
        self.seed = seed
        self.fitness_rates = []
        self.edges = self.convert_edges(edges)
        self.final_individual_core = None
        self.final_individual_rate = None
        self.time = None

    def add_log(self, value):
        self.fitness_rates.append(value)

    def set_time(self, new_time):
        self.time = new_time

    def set_final_individual_core(self, new_core):
        self.final_individual_core = new_core

    def set_final_individual_rate(self, new_rate):
        self.final_individual_rate = new_rate

    def set_seed(self, new_seed):
        self.seed = new_seed

    def set_edges(self, new_edges):
        self.edges = new_edges

    def convert_edges(self, edges):
        """
        Method convert object nx.EdgeView into list of tuples
        """
        list_of_edges = []
        for (u, v) in edges:
            list_of_edges.append((u, v))
        return list_of_edges

    def write_to_json(self, path):

        database_data = {
            'population_size': self.population_size,
            'individual_size': self.individual_size,
            'mutation_ind_prob': self.mutation_ind_prob,
            'mutation_elem_prob': self.mutation_elem_prob,
            'iterations': self.iterations,
            'seed': self.seed,
            'execution_time': self.time,
            'final_individual_rate': self.final_individual_rate,
            'final_individual_core': self.final_individual_core,
            'graph edges': self.edges,
            'fitness_rates': self.fitness_rates
        }

        with open(path, 'w') as file_handle:
            json.dump(database_data, file_handle, indent=4)
