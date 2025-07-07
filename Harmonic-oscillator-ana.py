import matplotlib.pyplot as plt
import numpy as np
Lx = 10
#Lx-Lx/Nx, 2*Lx/Nx
Nx=800
x = np.linspace(-Lx,Lx,Nx)
'''
x=np.arange(-Lx, Lx-Lx/Nx, 2*Lx/Nx) 

xx = np . zeros (( Nx ) , dtype = complex )

for i in range ( Nx ) :
   xx [ i ]= (x [ i ] )**2             # square of position vector
   '''
#s= (((np.pi))**(-1/4))*(np.exp(-((x)**2))/2)
s=(((np.pi))**(-1/4))*(np.sqrt(2))*x*(np.exp(-((x)**2))/2)
#s= (((np.pi))**(-1/4))*(np.sqrt(2))*x*(np.exp(-(xx))/2)
plt.figure(5)
plt.plot(x,s, 'b')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_1(x)$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25) 
plt.show() 
plt.legend( loc='upper right', numpoints = 1, fancybox=False, shadow=False, prop={"size":20} ) 