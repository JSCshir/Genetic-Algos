import random
import time
import matplotlib.pyplot as plt

BEST_FIT_VAL = 100000000
MAX_NUM_GENERATIONS = 100000
MIN_ACCEPTANCE_RATE = 4
VALUE_RANGE = (0, 10000)
MUTATION_RATE = 0.01
GENERATIONS_PER_SECOND = 150

def foo(x, y, z):
    return 81*x**6 + 2*y**4 + 900*z - 100

def fitness(x, y, z):
    ans = foo(x, y, z)
    if ans == 0:
        return BEST_FIT_VAL
    else:
        return abs(1/ans)

def gen_algo():
    datapt = []
    
    solutions = []
    for s in range(1000):
        solutions.append((random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE), 
                          random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE), 
                          random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)))
    
    for i in range(MAX_NUM_GENERATIONS):
        start_time = time.time() 
        
        rankedsolutions = []
        for s in solutions:
            rankedsolutions.append((fitness(s[0], s[1], s[2]), s))
        rankedsolutions.sort(reverse=True)
        
        best_fitness = rankedsolutions[0][0]
        datapt.append((i, best_fitness))  
        
        print(f"=== Gen {i} best solutions === ")
        print(rankedsolutions[0])
        
        if best_fitness > 10 ** (MIN_ACCEPTANCE_RATE + 1):
            break
    
        bestsolutions = rankedsolutions[:100]
    
        elements = []
        for s in bestsolutions:
            elements.append(s[1][0])
            elements.append(s[1][1])
            elements.append(s[1][2])
    
        newGen = []
        for _ in range(1000):
            e1 = random.choice(elements) * random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)
            e2 = random.choice(elements) * random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)
            e3 = random.choice(elements) * random.uniform(1 - MUTATION_RATE, 1 + MUTATION_RATE)
            newGen.append((e1, e2, e3))
        
        solutions = newGen
    
        elapsed_time = time.time() - start_time
        sleep_time = max(0, 1/GENERATIONS_PER_SECOND - elapsed_time) 
        time.sleep(sleep_time)

    generations, fitness_scores = zip(*datapt)  
    plt.figure(figsize=(12, 6))
    plt.bar(generations, fitness_scores, color='blue')
    plt.title('Best Fitness Score by Generation')
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness Score')
    plt.grid(True)
    plt.show()





for i in range(15):
    gen_algo()