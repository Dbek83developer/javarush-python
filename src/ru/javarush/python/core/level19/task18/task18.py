import random

# Условие задачи
weights = [2, 3, 4, 5, 9]
values = [3, 4, 8, 8, 10]
capacity = 20
population_size = 10
generations = 100
mutation_rate = 0.1
tournament_size = 3

# Генерация начальной популяции
def generate_individual(length):
    # Индивидуум представлен как список бинарных значений
    return [random.randint(0, 1) for _ in range(length)]

def generate_population(size, length):
    return [generate_individual(length) for _ in range(size)]

# Функция приспособленности
def fitness(individual):
    total_weight = sum(w * i for w, i in zip(weights, individual))
    total_value = sum(v * i for v, i in zip(values, individual))
    if total_weight > capacity:  # Если превышен вес, приспособленность равна 0
        return 0
    return total_value

# Турнирный отбор
def tournament_selection(population):
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=fitness)

# Кроссовер
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Мутация
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Переключение бита

# Главный цикл генетического алгоритма
def genetic_algorithm():
    population = generate_population(population_size, len(weights))
    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:population_size]
        best_individual = max(population, key=fitness)
        print(f"Generation {generation}: Best individual = {best_individual}, Fitness = {fitness(best_individual)}")
    return best_individual

# Запуск алгоритма
best_solution = genetic_algorithm()
print("Best solution found:", best_solution)
print("Total value:", fitness(best_solution))
