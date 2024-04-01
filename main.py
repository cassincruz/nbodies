#%%
from settings import * 
from nbodies import *

import pygame
import numpy as np 
from scipy.integrate import RK45
import random

from typing import List 

### Initialize Pygame ###
pygame.init()

window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("N-Body Simulation")

# %% --- Create System --- %% #
earth_sun = [

    *[Particle((SYSTEM_RADIUS * (2 * np.random.random(2) - 1))/2, EARTH_VELOCITY * (2*np.random.random(2) -1), EARTH_MASS, EARTH_RADIUS) for _ in range(10)], 
    Particle(np.array([SYSTEM_RADIUS*0.3, 0]), np.array([0, 4e5]), SOLAR_MASS, SOLAR_RADIUS), 
    Particle(np.array([SYSTEM_RADIUS*0.7, 0]), np.array([0, -4e5]), SOLAR_MASS, SOLAR_RADIUS)

]

sys = System(earth_sun, window) 

#%%
if __name__ == '__main__' : 
    RUNNING = True
    while RUNNING:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        sys.update() 
        window.fill(BLACK)
        sys.draw()
        pygame.display.update()