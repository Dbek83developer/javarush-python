import random
import numpy as np

# Параметры генетического алгоритма
POPULATION_SIZE = 100
NUM_GENERATIONS = 500
TOURNAMENT_SIZE = 5
MUTATION_RATE = 0.01


# Пример функции приспособленности (максимизация суммы элементов в хромосоме)
def fitness_function(individual):
    return sum(individual)


# Инициализация популяции
def initialize_population(pop_size, chromosome_length):
    return [[random.uniform(-10, 10) for _ in range(chromosome_length)] for _ in range(pop_size)]


# Турнирный отбор
def tournament_selection(population, fitnesses):
    tournament_indices = random.sample(range(len(population)), TOURNAMENT_SIZE)
    tournament = [population[i] for i in tournament_indices]
    tournament_fitnesses = [fitnesses[i] for i in tournament_indices]
    return tournament[np.argmax(tournament_fitnesses)]


# Одноточечный кроссовер
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


# Мутация
def mutate(individual):
    return [gene + random.gauss(0, 1) if random.random() < MUTATION_RATE else gene for gene in individual]


# Основной цикл генетического алгоритма
def genetic_algorithm():
    chromosome_length = 10
    population = initialize_population(POPULATION_SIZE, chromosome_length)

    for generation in range(NUM_GENERATIONS):
        fitnesses = [fitness_function(ind) for ind in population]

        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population

    # Оптимальное решение
    fitnesses = [fitness_function(ind) for ind in population]
    best_index = np.argmax(fitnesses)
    best_individual = population[best_index]
    return best_individual, fitnesses[best_index]


# Вызов алгоритма
best_individual, best_fitness = genetic_algorithm()
print("Лучший индивидуум:", best_individual)
print("Функция приспособленности:", best_fitness)
