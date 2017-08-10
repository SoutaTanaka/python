import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 6, 00.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos")
plt.show()
