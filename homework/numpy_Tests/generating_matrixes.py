import numpy as np
print("With zeros:")
arrayd1 = np.zeros(3)
print(arrayd1)
arrayd2 = np.zeros((2,4))
print(arrayd2)

print("With ones:")
arrayd1 = np.ones(3)
print(arrayd1)
arrayd2 = np.ones((2,4))
print(arrayd2)

print("With full:")
arrayd1 = np.full((3), 2)
print(arrayd1)
arrayd2 = np.full((2,4), 3)
print(arrayd2)

print("With eye:")
arrayd1 = np.eye(3, dtype=int)
print(arrayd1)
arrayd2 = np.eye(5, k=2)
print(arrayd2)