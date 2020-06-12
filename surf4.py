import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#3a import nr_results & nr_input, create matplotlib figure, add 4 subplots displayed 2x2 
import nr_results as nr
import nr_input as inp

fig = plt.figure(figsize=(10,6))
fig.suptitle('Above the Book - NetRet Model')
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')

#3b create x/y variables, with values determined by 'range variables' from nr_input 
X, Y/Z variables
x = np.arange(inp.exp_spr-6, inp.exp_spr+6, 1)
y = np.arange(inp.lo_tp, inp.hi_tp, 1)

#3c use 'x' and 'y' to create Numpy meshgrid 'X, Y', assign net_map (from nr_results) to 'Z'
X, Y = np.meshgrid(x, y)
Z = nr.net_map

#3d create colormap. For each axis: define subplot titles and create surface plot
mycmap = plt.get_cmap('RdYlGn')

ax1.set_title('Spread View')
ax1.set_zlabel('Result ($)')
ax1.set_xlabel('Spread')
ax1.set_ylabel('Total Points')
surf1 = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax1.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf1, ax=ax1, shrink=.7, aspect=15)

ax2.set_title('Total Point Display')
ax2.set_zlabel('Result ($)')
ax2.set_xlabel('Spread')
ax2.set_ylabel('Total Points')
surf2 = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax2.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf2, ax=ax2, shrink=.7, aspect=15)

ax3.set_title('Spread')
ax3.set_xlabel('Spread')
ax3.set_zlabel('Result ($)')
ax3.set_yticks([])
surf3 = ax3.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax3.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf3, ax=ax3, shrink=.7, aspect=15)

ax4.set_title('Total Pt')
ax4.set_zlabel('Result ($)')
ax4.set_ylabel('Total Points')
ax4.set_xticks([])
surf4 = ax4.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=mycmap)
ax4.set_zlim(np.min(Z), np.max(Z))
fig.colorbar(surf4, ax=ax4, shrink=.7, aspect=15)


#3e assign view angles to each surface plot (elevation, azimuth)
ax1.view_init(40, 55)
ax2.view_init(40, 35)
ax3.view_init(0, 90)
ax4.view_init(0, 180)


#3f display matplotlib figure
plt.show()
