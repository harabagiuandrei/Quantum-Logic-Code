from QLC_alpha_1 import *

class BlackHole:
    def __init__(self):
        self.mass = 0  # Starts with no mass

    def absorb(self, particle):
        """ Absorbs a particle into the singularity """
        if isinstance(particle, Particle):
            self.mass += particle.state  # Consumes logical mass
            particle.state = None  # Particle ceases to exist!
        return "Singularity Grows!" if self.mass > 5 else "Still forming..."

    def event_horizon(self):
        """ Once mass reaches critical threshold, it locks logic inside """
        return "Logical Collapse!" if self.mass >= 10 else "Horizon Expanding..."
