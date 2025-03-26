class WhiteHole:
    def __init__(self, mass=0):
        self.mass = mass  # Starts with a mass threshold

    def emit(self):
        """ Expels logical particles back into space """
        if self.mass > 0:
            self.mass -= 1  # Lose mass as it ejects particles
            return Particle()  # New particles are formed from expelled mass
        return None  # No mass left to emit

    def interact(self, other):
        """ White Holes repel everything! """
        if isinstance(other, Particle) or isinstance(other, AntiParticle):
            return -1  # Repulsion force
        return None
