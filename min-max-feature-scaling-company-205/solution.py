import numpy as np

def solve(x):
    if max(x) == min(x):
        return np.zeros(len(x),dtype = float)
    output = []
    for item in x:
        item_scaled = (item-min(x))/(max(x)-min(x))
        output.append(item_scaled)
    return np.array(output,dtype = float)
