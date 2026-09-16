import numpy as np

def expected_value_discrete(x: list, p: list) -> float:

    x=np.array(x)
    p=np.array(p)

    if len(x) == len(p):
        return float(np.dot (x,p))