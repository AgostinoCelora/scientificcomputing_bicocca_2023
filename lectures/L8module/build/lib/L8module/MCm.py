import random
import matplotlib.pyplot as plt
import numpy as np

MCm = [ #Marcov Chain model: 0 = Bull, 1 = Bear, 2 = Recession
    [0.9, 0.075, 0.025],  
    [0.15, 0.8, 0.05],    
    [0.25, 0.25, 0.5]
]

def simulate_stock_market(num_days):
    state = random.randint(0, 2)
    stateCounts = [0, 0, 0] 
    for _ in range(num_days):
        stateCounts[state] += 1
        state = random.choices([0, 1, 2], weights=MCm[state])[0]
    total_days = sum(stateCounts)
    fractions = [count / total_days for count in stateCounts]
    return fractions