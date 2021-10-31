from evolutionary_algorithm import evolutionary_algorithm

if __name__ == "__main__":

    example_edges = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

    dupabase, winner = evolutionary_algorithm(
        iterations=100000,
        edges=example_edges,
        seed=1
    )

    dupabase.write_to_json('dupa.json')

    print(winner)
    print(winner.fitness_rate)
