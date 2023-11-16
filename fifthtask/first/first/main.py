import numpy as np

a = 0.3
b = -21.17

def ctg(x):
    return 1 / np.tan(x)


y = ctg(np.pi/4 - 1)**4 + (a + 1.5)**(1/3) + (a-b)**8 - b/(np.arcsin(np.abs(a)**2))

print(f"Ответ равен {y}")
