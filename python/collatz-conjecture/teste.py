from collatz_conjecture import steps
import matplotlib.pyplot as plt
import numpy as np

try:
    _steps = steps(500)
except ValueError as e:
    print(e)

x = np.arange(0, _steps[0] + 1)
plt.plot(x, _steps[1])
plt.xlabel('Numeros de interação')
plt.ylabel('Numeros')
plt.grid()
plt.show()