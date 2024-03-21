import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Body Simulation")

# Constants
G = 6.67430e-11  # Gravitational constant
PARTICLE_RADIUS = 5
PARTICLE_MASS = 1e13  # Mass of each particle

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other settings
WRAPPING = False

# Particle class
class Particle:
    def __init__(self, x, y, vx, vy, mass, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.radius = radius

    def draw(self):
        pygame.draw.circle(window, WHITE, (int(self.x), int(self.y)), self.radius)

    def update(self, particles):
        # Calculate the force from each other particle
        force_x = force_y = 0
        for other in particles:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                distance_squared = min(dx ** 2 + dy ** 2, (self.radius + other.radius)**2)
                if distance_squared > 0:
                    distance = math.sqrt(distance_squared)
                    force_magnitude = G * self.mass * other.mass / distance_squared
                    force_x += force_magnitude * dx / distance
                    force_y += force_magnitude * dy / distance

        # Update velocity and position based on the force
        self.vx += force_x / self.mass * dt
        self.vy += force_y / self.mass * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Wrap around the screen
        if WRAPPING : 
            self.x = (self.x + WIDTH) % WIDTH
            self.y = (self.y + HEIGHT) % HEIGHT

# Set up the particles
particles = [
    Particle(random.randint(100, 700), random.randint(100, 500), 1e3* (random.random()-0.5), 1e3* (random.random()-0.5), 10 * PARTICLE_MASS * random.random(), PARTICLE_RADIUS)
    for _ in range(3)
]

# Time step
dt = 0.0001

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    for particle in particles:
        particle.update(particles)

    # Clear the window
    window.fill(BLACK)

    # Draw the particles
    for particle in particles:
        particle.draw()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()