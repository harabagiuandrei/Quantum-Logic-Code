from QLC_alpha_1_universe_simulator import UniverseSimulator

# universe = UniverseSimulator(1000000)  # One million particles!!
universe = UniverseSimulator(1000)  # One thousand particles!!
print("Universe instantiated \r\n")
print("Big Banging It! \r\n")
universe.big_bang()  # Initial explosion
print("Big Banged It! \r\n")
print("Evolving 1000000 steps... \r\n")
universe.evolve(1000000)  # Simulate a million time steps