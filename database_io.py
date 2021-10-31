import json


class Database:
    """
    Class holds following parameters evolutionary_algorithm was called with:
    population_size
    individual_size
    mutation_ind_prob
    mutation_elem_prob
    seed


    """
    def __init__(
        self,
        population_size,
        individual_size,
        mutation_ind_prob,
        mutation_elem_prob,
        iterations,
        seed
    ):
        self.population_size = population_size
        self.individual_size = individual_size
        self.mutation_ind_prob = mutation_ind_prob
        self.mutation_elem_prob = mutation_elem_prob
        self.iterations = iterations
        self.seed = seed
        self.fitness_rates = []
        self.final_individual_core = None
        self.final_individual_rate = None
        self.time = None

    def add_log(self, value):
        self.fitness_rates.append(value)

    def set_time(self, new_time):
        self.time = new_time

    def write_to_json(self, path):

        database_data = {
            'population_size': self.population_size,
            'individual_size': self.individual_size,
            'mutation_ind_prob': self.mutation_ind_prob,
            'mutation_elem_prob': self.mutation_elem_prob,
            'iterations': self.iterations,
            'seed': self.seed,
            'final_individual_rate': self.final_individual_rate,
            'final_individual_core': self.final_individual_core,
            'execution_time': self.time,
            'fitness_rates': self.fitness_rates
        }

        with open(path, 'w') as file_handle:
            json.dump(database_data, file_handle, indent=4)
