import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class HeatSimulator:

    def __init__(self, grid):
        self.grid = grid

    def update(self, alpha=0.1, dt = 1.0, dx = 1.0, dy = 1.0):
        """
        Updates the heat grid using finite difference method.

        Parameters:
        alpha (float): thermal diffusivity
        dt (float): time step
        dx, dy (float): spatial resolution
        """
        m,n = self.grid.shape
        new_grid = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                i1 = i + 1
                i2 = i - 1
                j1 = j + 1
                j2 = j - 1
                if i == 0:
                    i2 = m - 1
                if j == 0:
                    j2 = n - 1
                if i == m - 1:
                    i1 = 0
                if j == n - 1:
                    j1 = 0
                new_grid[i, j] = self.grid[i, j] + alpha * dt * (
                    (self.grid[i1, j] - 2*self.grid[i, j] + self.grid[i2, j]) / dx**2 +
                    (self.grid[i, j1] - 2*self.grid[i, j] + self.grid[i, j2]) / dy**2
                    )
        self.grid = new_grid

    def display(self):
        """
        shows the image of the current 2D grid
        """
        plt.imshow(self.grid, cmap="hot", interpolation="nearest")
        plt.colorbar(label="Temperature")
        plt.title("Heat Distribution")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def animate(self, steps = 100, interval = 30):
        """
        shows an animation of the heat distribution
        """
        fig, ax = plt.subplots()
        im = ax.imshow(self.grid, cmap='hot', interpolation='nearest')
        plt.colorbar(im, ax=ax)

        def update_frame(frame):
            self.update()
            im.set_array(self.grid)
            return [im]
        
        ani = animation.FuncAnimation(
            fig, update_frame, frames=steps, interval=interval, blit=True
        )
        plt.show()