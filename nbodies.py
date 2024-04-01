""" Defining class structure for particles and particle system. """

from settings import * 
import pygame
import numpy as np
from scipy.integrate import RK45
from typing import List

from numba import njit 

class Particle : 
    def __init__(self, position:np.ndarray, velocity:np.ndarray, mass:float, radius:float, color=WHITE) : 
        self.position = position
        self.velocity = velocity
        self.mass = mass 
        self.radius = radius
        self.color = color

    def copy(self) : 
        return Particle(self.position, self.velocity, self.mass, self.radius, self.color)
    
    def draw(self, window):
        display_position = min(window.get_size()) * (self.position / SYSTEM_RADIUS + 1) / 2
        display_radius = min(window.get_size()) * (0.5 * self.radius / SYSTEM_RADIUS)
        display_radius = max(display_radius, MIN_DISPLAY_RADIUS)
        display_radius = min(display_radius, MAX_DISPLAY_RADIUS)
        pygame.draw.circle(window, self.color, (int(display_position[0]), int(display_position[1])), display_radius)

class System : 
    def __init__(self, particles : List[Particle], window=None, t_max=1e5 * DT) : 
        self.particles = particles 
        self.window = window
        self.t_max = t_max
        self.f = self._make_f()
        self.rk = RK45(self.f, 0, self.y, self.t_max, max_step=DT)

    def dvdt(System) : 
        forces = []
        for p1 in System.particles : 
            force = np.zeros(2)
            for p2 in System.particles : 
                r = p2.position - p1.position
                if (r_norm := np.sqrt(r @ r)) != 0: 
                    
                    force = force + G * (min(r_norm, p2.radius)**3 / p2.radius**3) * p2.mass * r / r_norm ** 3

            forces.append(force)
        return np.array(forces)
    
    def _make_f(self) : 
        def f(t, y) : 
            return np.vstack([self.velocities, self.dvdt()]).flatten()
        
        return f

    @property
    def y(self) : 
        return np.vstack([self.positions, self.velocities]).flatten()

    @property
    def positions(self) : 
        return np.array([p.position for p in self.particles])
    
    @property
    def velocities(self) : 
        return np.array([p.velocity for p in self.particles])

    def update(self) : 
        self.rk.step()
        positions = self.rk.y[:self.rk.y.size // 2].reshape(-1, 2)
        velocities = self.rk.y[self.rk.y.size // 2:].reshape(-1, 2)
        for i, particle in enumerate(self.particles) : 
            particle.position = positions[i]
            particle.velocity = velocities[i]

    def draw(self) : 
        if self.window is None : 
            raise Exception
        
        else : 
            for particle in self.particles : 
                particle.draw(self.window)