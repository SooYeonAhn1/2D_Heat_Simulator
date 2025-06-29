import numpy as np
from HeatSimulator import HeatSimulator as hs

grid = np.random.rand(50, 50) * 100

sim = hs(grid)
sim.animate(steps=200, interval=30)