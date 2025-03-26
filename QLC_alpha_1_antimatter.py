class AntiParticle:
    def __init__(self):
        self.state = -1  # The opposite of 1

    def interact(self, other):
        """ Anti-Logic: It repels instead of attracting """
        if isinstance(other, Particle):
            return self.state * other.state  # -1 * 1 = Repulsion!
        elif isinstance(other, AntiParticle):
            return self.state and other.state  # They attract each other!
        return None  # No effect on vacuum or photons
