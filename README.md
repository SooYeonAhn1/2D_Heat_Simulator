# 2D Heat Simulator

This is a solo project created to practice **CUDA concepts** by simulating heat diffusion using the 2D heat equation.

The simulation is based on solving the **partial differential equation (PDE)** for heat distribution over time.

---

## Project Structure

- `HeatSimulator.py`: Contains the simulation logic and animation functions
- `main.py`: Example script that sets up the grid and runs the simulation

---

## How to Use

```python
import numpy as np
from HeatSimulator import HeatSimulator as hs

# Initialize a 50x50 grid with random heat values
grid = np.random.rand(50, 50) * 100

# Create simulator instance
sim = hs(grid)

# Display the current heat distribution (in a GUI-capable environment)
sim.display()

# Animate the heat spread over time
sim.animate(steps=200, interval=30)
* Parameters
    *steps: Number of frames in the animation
    * interval: Delay between frames (in milliseconds)
```

📌 Note
This project is intended for learning and experimentation. GUI display requires a Python environment with GUI support (e.g., WSL2 with Windows 11, or native Linux/Windows with matplotlib installed).
