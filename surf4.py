import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import map_nr as nr
import input_nr as inp



fig = plt.figure(figsize=(12,6))
fig.suptitle('Net Return')
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')


x = np.arange(inp.exp_spr-6, inp.exp_spr+6, 1)
y = np.arange(inp.lo_tp, inp.hi_tp, 1)
X, Y = np.meshgrid(x, y)
Z = nr.net_map


ax1.set_title('Spr View')
ax1.set_zlabel('Result ($)')
ax1.set_xlabel('Spread')
ax1.set_ylabel('Total Points')



mycmap = plt.get_cmap('RdYlGn')
surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax1.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf1, ax=ax1, shrink=.7, aspect=15)




ax2.set_title('TP View')
ax2.set_zlabel('Result ($)')
ax2.set_xlabel('Spread')
ax2.set_ylabel('Total Points')

surf2 = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax2.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf2, ax=ax2, shrink=.7, aspect=15)


ax3.set_title('Spr Overview')
ax3.set_ylabel('Total Points')
ax3.set_xlabel('Spread')
ax3.set_zticks([])


mycmap = plt.get_cmap('RdYlGn')
surf3 = ax3.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax3.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf3, ax=ax3, shrink=.7, aspect=15)




ax4.set_title('TP Overview')
ax4.set_zlabel('Result ($)')
ax4.set_ylabel('Total Points')

#ax4.set_axis_off()
ax4.set_xticks([])

surf4 = ax4.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax4.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf4, ax=ax4, shrink=.7, aspect=15)


ax1.view_init(40, 55)
ax2.view_init(40, 35)
ax3.view_init(90, 90)
ax4.view_init(0, 0)



plt.show()
