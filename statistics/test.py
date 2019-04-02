import numpy as np
from reg_lin import reg_lin

data = np.array([
    [1.4,0.5],
    [1.9,2.3],
    [3.2,2.9],
])

r=reg_lin(data)
print(r.m,r.n)
