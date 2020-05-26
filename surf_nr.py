import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import map_nr as nr
import input_nr as inp
#renamed to surf_nr.py from alt_model_nr2.py



fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111, projection='3d')



x = np.arange(inp.hi_spr, inp.hi_spr+10, 1)
y = np.arange(inp.lo_tp, inp.hi_tp, 1)
X, Y = np.meshgrid(x, y) 
Z = nr.net_map




ax1.set_title('Net Return Colormap')
ax1.set_zlabel('Net Return ($)')
ax1.set_xlabel('Spread')
ax1.set_ylabel('Total Points')



mycmap = plt.get_cmap('RdYlGn')
surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax1.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf1, ax=ax1, shrink=.7, aspect=15)

ax1.view_init(45)

plt.show()
