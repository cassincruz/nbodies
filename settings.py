# --- Pygame Settings --- #
DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600

# Colors #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MIN_DISPLAY_RADIUS = 5
MAX_DISPLAY_RADIUS = 25

# --- Simulation Settings --- #

# Constants #
G = 6.674e-11  # [m^3 kg^–1 s^–2] Gravitational constant 

SYSTEM_RADIUS = 5.906e9 # [km] From the semi-major orbital axis of Pluto 

EARTH_RADIUS = 6.371e6 # [m]
EARTH_MASS = 5.972e24  # [kg] 
EARTH_VELOCITY = 3e5 # [m/s]

SOLAR_RADIUS = 6.957e8 # [m]
SOLAR_MASS = 1.988e31 # [kg]

DT = 30 # [s] Simulation time step length

# World wrapping #
WRAPPING = False