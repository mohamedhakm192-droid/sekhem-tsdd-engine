from sekhem.system import SEKHEMSystem
import matplotlib.pyplot as plt

system = SEKHEMSystem()

X = [2.0, -1.0, 0.5]

history = []

for t in range(100):
    X = system.step(X)
    history.append(X)

history = list(zip(*history))  # split dimensions

plt.figure()

for i in range(len(history)):
    plt.plot(history[i], label=f"X{i}")

plt.legend()
plt.title("SEKHEM-TSDD State Evolution")
plt.xlabel("Time")
plt.ylabel("State Value")

plt.show()
