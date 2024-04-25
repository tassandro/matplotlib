#Primeiro devemos definir as funções a serem plotadas, vamos usar uma função afim e uma função quadrática
#importando as bibliotecas

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')

plt.show()

#Agora criando dois gráficos separados lado a lado:
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
fig

#caso se deseje redimensionar
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

axes[0].plot(x,y,color="blue", lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')

