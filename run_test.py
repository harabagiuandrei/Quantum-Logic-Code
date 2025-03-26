from QLC_alpha_1 import *
from QLC_alpha_1_gravity import Gravity
from QLC_alpha_1_black_hole import BlackHole
from QLC_alpha_1_antimatter import AntiParticle

# Instantiate objects in our logical universe
p1 = Particle()
p2 = Particle()
vac = Vacuum()
photon = Photon()

# Simulate interactions
print("Particle meets Particle:", p1.interact(p2))  # Expected: 1 (They attract)
print("Particle meets Vacuum:", p1.interact(vac))    # Expected: 1 (It can move)
print("Particle meets Photon:", p1.interact(photon)) # Expected: NAND collapse result!

#Simulate black hole?

p3 = Particle()
p4 = Particle()
p5 = Particle()
p6 = Particle()
p7 = Particle()
p8 = Particle()

bh = BlackHole()

print(bh.absorb(p3) + "\r\n")
print(bh.absorb(p4) + "\r\n")
print(bh.absorb(p5) + "\r\n")
print(bh.absorb(p6) + "\r\n")
print(bh.absorb(p7) + "\r\n")
print(bh.absorb(p8) + "\r\n")