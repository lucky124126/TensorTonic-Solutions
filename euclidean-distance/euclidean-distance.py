import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    x = np.array(x)
    y=np.array(y)
    return float (np.linalg.norm(x-y))
    pass