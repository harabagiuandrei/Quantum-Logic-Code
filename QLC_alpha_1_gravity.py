class Gravity:
    def __init__(self, strength=1):
        self.strength = strength  # Defines how strong the pull is

    def attract(self, particle1, particle2):
        """ Applies logical gravity between two particles """
        if isinstance(particle1, Particle) and isinstance(particle2, Particle):
            return (particle1.state and particle2.state) * self.strength  # 1 AND 1 pulls them together!
        return 0  # If no particles, no gravity effect
