import random
from QLC_alpha_1 import Particle
from QLC_alpha_1_gravity import Gravity

class UniverseSimulator:
    def __init__(self, particleCount=100):
        self.particles = []
        self.time = 0  # Keep track of simulation time
        self.create_particles(particleCount)

    def create_particles(self, count):
        """ Big Bang: Creates an explosion of particles """
        for _ in range(count):
            x, y, z = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)
            speed = random.uniform(0.1, 1.0)
            vx, vy, vz = x * speed, y * speed, z * speed  # Explosive outward motion
            charge = random.choice([1, -1])  # 50% matter, 50% antimatter
            mass = random.uniform(0.1, 5.0)  # Random mass values
            
            particle = Particle(x, y, z, vx, vy, vz, charge, mass)
            self.particles.append(particle)

    def big_bang(self):
        """ Initial explosion sends particles flying in all directions """
        print("💥 BIG BANG INITIATED! 💥 Particles spreading...")
        for p in self.particles:
            p.vx *= 10  # Give them a serious speed boost
            p.vy *= 10
            p.vz *= 10

    def evolve(self, steps=10):
        """ Simulates time passing and structure forming """
        for _ in range(steps):
            self.time += 1
            print(f"🌌 Step {self.time}: Universe evolving... ({len(self.particles)} particles)")

            to_remove = []
            for p in self.particles:
                p.move()  # Move through space

                for other in self.particles:
                    if p != other:
                        interaction = p.interact(other)

                        if interaction == "Annihilate":
                            to_remove.append(p)
                            to_remove.append(other)

                        elif interaction == "Absorb":
                            to_remove.append(other)  # The smaller one gets removed

                        elif interaction == "Absorbed":
                            to_remove.append(p)  # The smaller one gets removed

            # Remove annihilated/absorbed particles
            self.particles = [p for p in self.particles if p not in to_remove]

            print(f"🌟 Step {self.time}: {len(self.particles)} particles remain, forming clusters...")

