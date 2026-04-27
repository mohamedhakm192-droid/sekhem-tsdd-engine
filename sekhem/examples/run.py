from sekhem.system import SEKHEMSystem

system = SEKHEMSystem()

X = [2.0, -1.0, 0.5]

for t in range(100):
    X = system.step(X)
    print(X)
