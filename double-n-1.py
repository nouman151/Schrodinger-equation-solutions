import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as spla

def step_func(x):
    return 0.5*(1+np.sign(x))


steps=500
hbar=1
m=1.0
# create x-vector from -A to A
A=10
o = np.arange(-A, A, 0.01);
xvec=np.linspace(-A,A,steps)
# get step size
h=xvec[1]-xvec[0]




vD=1000
v=400
x1=0.2
x2=1.2    
U=v*step_func(xvec+x1)-v*step_func(xvec-x1)+vD*step_func(xvec-x2)+vD*step_func(-xvec-x2)

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






plt.figure(2)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
plt.plot(xvec,U, 'black',   linewidth=4.0 ,label='Any')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$V(x)$', fontsize=30,fontweight='bold')
#plt.xlim(0,4)
#plt.ylim(-1,1)
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)


'''
frame1 = plt.gca()
for xlabel_i in frame1.axes.get_yticklabels():
    xlabel_i.set_fontsize(0.0)
    xlabel_i.set_visible(False)
for tick in frame1.axes.get_yticklines():
    tick.set_visible(False)
'''
plt.show()









'''

y = []
y = np.append(y,V[:,z[0]])
invt=sum(abs(y)**2)*h
y=y/np.sqrt(invt)



y1 = []
y1 = np.append(y1,V[:,z[1]])
invt=sum(abs(y1)**2)*h
y1=y1/np.sqrt(invt)


y2 = []
y2 = np.append(y2,V[:,z[2]])
invt=sum(abs(y2)**2)*h
y2=y2/np.sqrt(invt)

y3 = []
y3 = np.append(y3,V[:,z[3]])
invt=sum(abs(y3)**2)*h
y3=y3/np.sqrt(invt)

#analytical energies
g=((3.0648951024026166130)**2)/32
g1=((6.1293455732955920715)**2)/32
g2=((9.1928830979055678123)**2)/32

a=4

k=np.sqrt(2*g)
k1=np.sqrt(2*g1)
k2=np.sqrt(2*g2)

m=(np.sin(2*a*k))
m1=(np.sin(2*a*k1))
m2=(np.sin(2*a*k2))

b=(a/2) - (m/(4*k))
b1=(a/2) - (m1/(4*k1))
b2=(a/2) - (m2/(4*k2))


s=(np.sin(k*o))/(np.sqrt(b))
s1=(np.sin(k1*o))/(np.sqrt(b1))
s2=(np.sin(k2*o))/(np.sqrt(b2))

s=(np.sin(k*xvec))/(np.sqrt(b))
s1=(np.sin(k1*xvec))/(np.sqrt(b1))
s2=(np.sin(k2*xvec))/(np.sqrt(b2))


#n=1
nlevel=1
plt.figure(1)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
plt.plot(o,s, 'b',   linewidth=4.0 ,label='Any') 
#plt.plot(xvec,y1+g1, 'red')
#plt.plot(xvec,y2+g2, 'brown')
#plt.plot(xvec,y3+g3, 'orange')
plt.plot(xvec,U, 'r*',linewidth=3.0,markersize=7) 
plt.plot(xvec,y, 'r*',linewidth=3.0,markersize=7, label='Num') 
#plt.plot(xvec,y1+E[2], 'red')
#plt.plot(xvec,y2+E[4],'brown')
#plt.plot(xvec,y3+E[6],'orange')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_1(x)$', fontsize=30,fontweight='bold')
#plt.xlim(0,10)
#plt.ylim(-1,1)
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )

#ab1 = "E:/Python/Wavefunction-%g.png" %(nlevel)      
#plt.savefig(ab1, format='png', dpi=1000)


#n=2
nlevel=2
plt.figure(2)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(xvec,y+g, 'b') 
plt.plot(o,s1, 'b',   linewidth=4.0 ,label='Any')
#plt.plot(xvec,y2+g2, 'brown')
#plt.plot(xvec,y3+g3, 'orange')

#plt.plot(xvec,y+E[0], 'b') 
plt.plot(xvec,-y1, 'r*',linewidth=3.0,markersize=7, label='Num')
#plt.plot(xvec,y2+E[4],'brown')
#plt.plot(xvec,y3+E[6],'orange')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_1(x)$', fontsize=30,fontweight='bold')
#plt.xlim(0,4)
#plt.ylim(-1,1)
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )

#ab1 = "E:/Python/Wavefunction-%g.png" %(nlevel)      
#plt.savefig(ab1, format='png', dpi=1000)



#n=3
nlevel=3
plt.figure(3)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(xvec,y+g, 'b') 
#plt.plot(xvec,y1+g1, 'red')
plt.plot(o,s2, 'b',   linewidth=4.0 ,label='Any')
#plt.plot(xvec,y3+g3, 'orange')

#plt.plot(xvec,y+E[0], 'b') 
#plt.plot(xvec,y1+E[2], 'red')
plt.plot(xvec,y2, 'r*',linewidth=3.0,markersize=7, label='Num')
#plt.plot(xvec,y3+E[6],'orange')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_3(x)$', fontsize=30,fontweight='bold')
plt.xlim(0,4)
plt.ylim(-1,1)
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )

ab1 = "E:/Python/Wavefunction-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)




plt.figure(4)
plt.plot(xvec,U, 'r*',linewidth=3.0,markersize=7, label='Num')
#plt.plot(xvec,y3+E[6],'orange')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_3(x)$', fontsize=30,fontweight='bold')
%plt.xlim(0,4)
%plt.ylim(-1,1)
plt.xticks(color='k', size=15)
plt.yticks(color='k', size=15)
plt.show() 


'''