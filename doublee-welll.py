import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as spla

def step_func(x):
    return 0.5*(1+np.sign(x))


steps=900
hbar=1

m=1
# create x-vector from -A to A
xvec=np.linspace(-10,10,steps)
# get step size
h=xvec[1]-xvec[0]
# create the potential from step function


vD=1000
v=80
x1=0.2
x2=1.2    
U=v*step_func(xvec+x1)-v*step_func(xvec-x1)+vD*step_func(xvec-x2)+vD*step_func(-xvec-x2)
'''
plt.figure(1)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
plt.plot(xvec,U, 'black',marker='o' , label='Unit step function')
plt.xlim(-2,2)
plt.ylim(0,2)
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$y$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
plt.show() 
#ab1 = "E:/Python/step-potential.png"      
#plt.savefig(ab1, format='png', dpi=1000)
'''
  
# create Laplacian via 3-point finite-difference method
Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
+np.diag(np.ones(steps-1),-1))/(float)(h**2)
# create the Hamiltonian
Hamiltonian=np.zeros((steps,steps))
[i,j]=np.indices(Hamiltonian.shape)
Hamiltonian[i==j]=U
Hamiltonian+=(-0.5)*((hbar**2)/m)*Laplacian
# diagonalize the Hamiltonian yielding the wavefunctions and energies
E,V= spla.eigh(Hamiltonian)  #np.linalg.eig(Hamiltonian)   
z = np.argsort(E)



#probabltes


nlevel=1
y = []
y = np.append(y,V[:,z[0]])
invt=sum(abs(y)**2)*h
y=y/np.sqrt(invt)

plt.figure(1)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(xvec,U, 'black',label='Num')
plt.plot(xvec,np.abs(y)**2, 'r',label='Num') 
plt.xlim(-3,3)
plt.ylim(0,1)
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_1(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
#ab1 = "E:/Python/pdw-%g.png" %(nlevel)      
#plt.savefig(ab1, format='png', dpi=1000)


nlevel=2
y1 = []
y1 = np.append(y1,V[:,z[2]])
invt=sum(abs(y1)**2)*h
y1=y1/np.sqrt(invt)

plt.figure(2)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(xvec,U, 'black') 
plt.plot(xvec,np.abs(y1)**2, 'r',label='Num')
plt.xlim(-3,3)
plt.ylim(0,1)
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('|$\psi_2(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
#ab1 = "E:/Python/pdw-%g.png" %(nlevel)      
#plt.savefig(ab1, format='png', dpi=1000)


nlevel=3
y2 = []
y2 = np.append(y2,V[:,z[4]])
invt=sum(abs(y2)**2)*h
y2=y2/np.sqrt(invt)


plt.figure(3)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(xvec,U, 'black')
plt.plot(xvec,np.abs(y2)**2, 'r',label='Num')
plt.ylim(0,1)
plt.xlim(-3,3)
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_3(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
#ab1 = "E:/Python/pdw-%g.png" %(nlevel)      
#plt.savefig(ab1, format='png', dpi=1000)




#wavefunctons
'''


nlevel=1
y = []
y = np.append(y,V[:,z[0]])
invt=sum(abs(y)**2)*h
y=y/np.sqrt(invt)

plt.figure(1)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(xvec,U, 'black',label='Num')
plt.plot(xvec,y, 'r',label='Num') 
plt.xlim(-3,3)
#plt.ylim(0,1)
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_1(x)$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
ab1 = "E:/Python/dw-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)


nlevel=2
y1 = []
y1 = np.append(y1,V[:,z[2]])
invt=sum(abs(y1)**2)*h
y1=y1/np.sqrt(invt)

plt.figure(2)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(xvec,U, 'black',label='Num') 
plt.plot(xvec,y1, 'r',label='Num')
plt.xlim(-3,3)
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_2(x)$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
#ab1 = "E:/Python/dw-%g.png" %(nlevel)      
#plt.savefig(ab1, format='png', dpi=1000)



nlevel=3
y2 = []
y2 = np.append(y2,V[:,z[4]])
invt=sum(abs(y2)**2)*h
y2=y2/np.sqrt(invt)


plt.figure(3)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
plt.plot(xvec,y2, 'r',label='Num')
plt.xlim(-3,3)
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_3(x)$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
#ab1 = "E:/Python/dw-%g.png" %(nlevel)      
#plt.savefig(ab1, format='png', dpi=1000)

'''