import sys
import numpy as np
from scipy.interpolate import Rbf, griddata
# http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
from mystic.munge import *
from mystic.models import griewangk as model
i,xy,z = logfile_reader('log.txt')
i,ixy,iz = logfile_reader('inv.txt')
#xy,z = ixy,iz
del i

#############
shift = 0
scale = 0
N = 10000.
args = {
'smooth': 0, # 1
'function': 'thin_plate', #'multiquadratic'
#multiquadratic, inverse, gaussian, linear, qubic, quintic, thin_plate
}
#############



xyz = np.vstack((np.array(xy).T,z))
#'''
ixyz = np.vstack((np.array(ixy).T,iz))
ixyz[-1,:] = -ixyz[-1]
del ixy,iz
xyz = np.hstack((xyz, ixyz))
#'''

# f = Rbf(*xyz)

# _z = [model(i) for i in xyz.T[:,:2]]

x = xyz.T[:,0]
y = xyz.T[:,1]
z = xyz.T[:,2]

def unique(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]


#HACK: remove duplicate points by adding noise
#XXX: better to strip duplicates (e.g. make unique) ?
_x = x + np.random.normal(scale=1e-8, size=x.shape)
_y = y + np.random.normal(scale=1e-8, size=y.shape)

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

figure = plt.figure()
kwds = {'projection':'3d'}
ax = figure.gca(**kwds)
ax.autoscale(tight=True)

true = 'ko'
logs = 'ro'

'''
ax.plot(_x, _y, _z, true, linewidth=2, markersize=4)
ax.plot(x, y, z, logs, linewidth=2, markersize=4)
plt.show()
'''

'''
ax.plot_trisurf(_x, _y, _z, cmap=cm.jet, linewidth=0)
ax.plot(_x, _y, _z, true, linewidth=2, markersize=4)
plt.show()
'''

if len(z) > N:
    N = max(int(round(len(z)/N)),1)
    print "for speed, sampling {} down to {}".format(len(z),len(z)/N)
    x, _x, y, _y, z = x[::N], _x[::N], y[::N], _y[::N], z[::N]
#   ax.plot(x, y, z, 'ko', linewidth=2, markersize=4)
#   plt.show()
#   sys.exit(0)

f = Rbf(_x, _y, z, **args)
# _z = f(_x, _y)


n = 100
n = complex('{}j'.format(n))
xgrid,ygrid = np.mgrid[x.min():x.max():n, y.min():y.max():n]
z_ = f(xgrid, ygrid)


mz = np.argmin(z)
xx,yy = x[mz],y[mz]
print "min: {}; min@f: {}".format(z[mz], f(xx,yy))
mz = np.argmax(z)
xx,yy = x[mz],y[mz]
print "max: {}; max@f: {}".format(z[mz], f(xx,yy))


# scaling used by model plotter
if scale:
  if shift:
      z_ = np.asarray(z_)+shift
      z = np.asarray(z)+shift
  z_ = np.log(4*np.asarray(z_)*scale+1)+2
  z = np.log(4*np.asarray(z)*scale+1)+2


density = 9
d = max(11 - density, 1)
ax.plot_wireframe(xgrid, ygrid, z_, rstride=d, cstride=d)
#ax.plot_surface(xgrid, ygrid, z_, rstride=d, cstride=d, cmap=cm.jet, linewidth=0, antialiased=False)
ax.plot(x, y, z, 'ko', linewidth=2, markersize=4)

#ax.set_xlim3d(*xbounds)
#ax.set_ylim3d(*ybounds)
plt.show()
figure.savefig('ackley.png')

