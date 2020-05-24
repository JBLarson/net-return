import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import call_nr_results as nr

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111, projection='3d')


x = np.arange(-4, 2, 1)
y = np.arange(40, 46, 1)
X, Y = np.meshgrid(x, y) 
Z = nr.net_map_net



mycmap = plt.get_cmap('RdYlGn')
ax1.set_title('Net Return Colormap')
ax1.set_zlabel('Net Return ($)')
ax1.set_xlabel('Spread')
ax1.set_ylabel('Total Points')



surf1 = ax1.plot_surface(X, Y, Z, cmap=mycmap)
ax1.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf1, ax=ax1, shrink=.8, aspect=20)

#ax.view_init(30,angle)

plt.show()
