# Define the fundamental building blocks of the universe

# class Particle:
#     def __init__(self, state=1):  # A particle is made of logical "1"
#         self.state = state

#     def interact(self, other):
#         """ Default interaction rule between particles """
#         if isinstance(other, Particle):
#             return self.state and other.state  # (1 AND 1) means stable attraction
#         elif isinstance(other, Vacuum):
#             return self.state or other.state  # (1 OR 0) allows movement
#         elif isinstance(other, Photon):
#             return self.nand_collapse(other)  # NAND collapse upon photon interaction

#     def nand_collapse(self, photon):
#         """ The quantum measurement effect """
#         #conditia de dedesupt nu e doar "not self.state si photon.state"
#         #ci eventual posibile transformari ale celor 2 entitati
#         return not (self.state and photon.state)  # NAND gate collapse
#         #return ..

# version 2 particle

# import random

# class Particle:
#     def __init__(self, state=1, x=0, y=0, z=0):
#         self.state = state  # Logical state: 1 or 0
#         self.x, self.y, self.z = x, y, z  # Spatial coordinates
#         self.vx, self.vy, self.vz = 0, 0, 0  # Velocity components

#     def set_speed(self, vx, vy, vz):
#         """ Sets particle velocity in 3D space """
#         self.vx, self.vy, self.vz = vx, vy, vz

#     def move(self):
#         """ Updates position based on velocity """
#         self.x += self.vx
#         self.y += self.vy
#         self.z += self.vz

#     def interact(self, other):
#         """ Logical interactions between particles """
#         if isinstance(other, Particle):
#             return self.state and other.state  # Attraction via AND
#         elif isinstance(other, Vacuum):
#             return self.state or other.state  # OR allows free movement
#         elif isinstance(other, Photon):
#             return self.nand_collapse(other)  # Collapse under photon interaction

#     def nand_collapse(self, photon):
#         """ Simulates NAND collapse upon photon interaction """
#         return not (self.state and photon.state)  # Logical reset

#version 3 particle

# import random

# class Particle:
#     def __init__(self, state=1, x=0, y=0, z=0, mass=1, charge=1):
#         self.state = state  # Logical state: 1 (matter) or 0 (antimatter)
#         self.x, self.y, self.z = x, y, z  # 3D Position
#         self.vx, self.vy, self.vz = random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3)  # Initial speed
#         self.mass = mass  # More mass means stronger gravity
#         self.charge = charge  # Matter (+1) or Antimatter (-1)

#     def move(self):
#         """ Updates position based on velocity """
#         self.x += self.vx
#         self.y += self.vy
#         self.z += self.vz

#     def interact(self, other):
#         """ Interaction logic: Gravity & Annihilation """
#         if isinstance(other, Particle):
#             distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

#             if distance < 1 and self.charge != other.charge:  
#                 # Matter & Antimatter collide → Annihilation!
#                 return "Annihilate"
            
#             elif distance < 3:  
#                 # Closer means more attraction based on mass
#                 attraction = (self.mass * other.mass) / (distance ** 2)
#                 self.vx += attraction * (other.x - self.x) * 0.01
#                 self.vy += attraction * (other.y - self.y) * 0.01
#                 self.vz += attraction * (other.z - self.z) * 0.01
                
#         return "Stable"

# version 4 Particle

# import random

# class Particle:
#     def __init__(self, state=1, x=0, y=0, z=0, mass=1, charge=1):
#         self.state = state  # Logical state: 1 (matter) or 0 (antimatter)
#         self.x, self.y, self.z = x, y, z  # 3D Position
#         self.vx, self.vy, self.vz = random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3)  # Initial speed
#         self.mass = mass  # More mass means stronger gravity
#         self.charge = charge  # Matter (+1) or Antimatter (-1)

#     def move(self):
#         """ Updates position based on velocity """
#         self.x += self.vx
#         self.y += self.vy
#         self.z += self.vz

#     # def interact(self, other):
#     #     """ Interaction logic: Gravity & Annihilation """
#     #     if isinstance(other, Particle):
#     #         distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

#     #         if distance < 1 and self.charge != other.charge:  
#     #             # Matter & Antimatter collide → Annihilation!
#     #             return "Annihilate"
            
#     #         elif distance < 3:  
#     #             # Closer means more attraction based on mass
#     #             attraction = (self.mass * other.mass) / (distance ** 2)
#     #             self.vx += attraction * (other.x - self.x) * 0.01
#     #             self.vy += attraction * (other.y - self.y) * 0.01
#     #             self.vz += attraction * (other.z - self.z) * 0.01
                
#     #     return "Stable"
#     def interact(self, other):
#     #""" Interaction logic: Gravity, Growth, and Annihilation """
#         if isinstance(other, Particle):
#             distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

#             if distance < 1 and self.charge != other.charge:
#                 # Matter & Antimatter collide → PURE Annihilation
#                 return "Annihilate"

#             elif distance < 1 and self.charge == other.charge:
#                 # Same type particles merge! Bigger absorbs smaller.
#                 if self.mass >= other.mass:
#                     self.mass += other.mass * 0.9  # Absorb 90% of the other's mass
#                     return "Absorb"
#                 else:
#                     other.mass += self.mass * 0.9  # The other absorbs this one
#                     return "Absorbed"

#             elif distance < 3:
#                 # Closer means more attraction based on mass
#                 attraction = (self.mass * other.mass) / (distance ** 2)
#                 self.vx += attraction * (other.x - self.x) * 0.01
#                 self.vy += attraction * (other.y - self.y) * 0.01
#                 self.vz += attraction * (other.z - self.z) * 0.01

#         return "Stable"


#version 5 Particle

import math

class Particle:
    def __init__(self, x, y, z, vx=0, vy=0, vz=0, charge=1, mass=1):
        """ Defines a particle in 3D space with velocity, charge, and mass """
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx  # Velocity X
        self.vy = vy  # Velocity Y
        self.vz = vz  # Velocity Z
        self.charge = charge  # 1 = Matter, -1 = Antimatter
        self.mass = mass  # Determines gravitational attraction

    def move(self):
        """ Updates position based on velocity (basic Newtonian motion for now) """
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def interact(self, other):
        """ Defines interactions between particles based on logical physics """

        # 🔥 1. Annihilation (Matter + Antimatter = BOOM)
        if self.charge == -other.charge:  
            return "Annihilate"

        # 🔥 2. Attraction (Gravity-like effect, larger mass absorbs smaller mass)
        elif self.mass > other.mass:
            self.absorb(other)
            return "Absorb"

        # 🔥 3. Other case: It gets absorbed by something larger
        elif self.mass < other.mass:
            return "Absorbed"

        return "NoInteraction"

    def absorb(self, other):
        """ Simulates mass merging when one particle absorbs another """
        total_mass = self.mass + other.mass
        self.vx = (self.vx * self.mass + other.vx * other.mass) / total_mass
        self.vy = (self.vy * self.mass + other.vy * other.mass) / total_mass
        self.vz = (self.vz * self.mass + other.vz * other.mass) / total_mass
        self.mass = total_mass  # The bigger mass now includes the other!

class Vacuum:
    def __init__(self):
        self.state = 0  # Vacuum is defined as "0"

    def interact(self, other):
        """ Vacuum allows wave propagation but repels mass """
        if isinstance(other, Particle):
            return self.state or other.state  # (0 OR 1) allows movement
        return None  # Nothing happens otherwise


class Photon:
    def __init__(self):
        self.state = 1 or 0  # Superposition before interaction

    def interact(self, other):
        """ Photons trigger NAND-collapse in matter """
        if isinstance(other, Particle):
            return other.nand_collapse(self)
        return None
