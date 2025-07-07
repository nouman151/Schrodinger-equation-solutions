import numpy as np
import matplotlib.pyplot as plt

def Vpot(x):
    return  0 #x**2   

a = 5  #lower and upper limit
N =50  # number of grid points
m = np.arange(0, a, 0.01);
x = np.linspace(0, a, N)
h = x[1]-x[0]


T = np.zeros((N-2)**2).reshape(N-2,N-2)

for i in range(N-2):
    for j in range(N-2):
        if i==j:
            T[i,j]= -2
        elif np.abs(i-j)==1:
            T[i,j]=1
        else:
            T[i,j]=0
            
          
V = np.zeros((N-2)**2).reshape(N-2,N-2)

for i in range(N-2):
    for j in range(N-2):
        if i==j:
            V[i,j]= Vpot(x[i+1])
        else:
            V[i,j]=0
            
                                                        
H = -T/(2*h**2) 
val,vec=np.linalg.eig(H)
z = np.argsort(val) 


#n=1
nlevel=1
p=((2/a)**(1/2))*np.sin((1*np.pi*m)/a)

y = []
y = np.append(y,vec[:,z[0]])
y = np.append(y,0)
y = np.insert(y,0,0)
invt=sum(abs(y)**2)*h
y=y/np.sqrt(invt)
 
  
    
plt.figure(1)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25) 
plt.plot(m,np.abs(p)**2, 'b',   linewidth=4.0 ,label='Any')
plt.plot(x,np.abs(y)**2, 'r*',linewidth=3.0,markersize=10, label='Num')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_1(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25)
plt.show() 
plt.legend( loc='upper right', numpoints = 1, fancybox=False, shadow=False, prop={"size":20} )
'''
ab1 = "E:/Python/pniw-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)
'''


    



plt.figure(2)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.20)
plt.plot(m,p, 'b',   linewidth=4.0 ,label='Any')
plt.plot(x,y, 'r*',linewidth=3.0,markersize=10, label='Num')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_1(x)$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25) 
plt.show() 
plt.legend( loc='upper right', numpoints = 1, fancybox=False, shadow=False, prop={"size":20} )
'''
ab1 = "E:/Python/niw-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)
'''




#n=2


nlevel=2

q=((2/a)**(1/2))*np.sin((2*np.pi*m)/a)
y1 = []
y1 = np.append(y1,vec[:,z[1]])
y1 = np.append(y1,0)
y1 = np.insert(y1,0,0)
invt=sum(abs(y1)**2)*h
y1=y1/np.sqrt(invt)


plt.figure(3)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25) 
plt.plot(m,np.abs(q)**2, 'b',   linewidth=4.0 ,label='Any')
plt.plot(x,np.abs(y1)**2, 'r*',linewidth=3.0,markersize=10, label='Num')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_2(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )
'''
ab1 = "E:/Python/pniw-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)
'''


    



plt.figure(4)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
plt.plot(m,q, 'b',   linewidth=4.0 ,label='Any')
plt.plot(x,-y1, 'r*',linewidth=3.0,markersize=10, label='Num')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_2(x)$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20} )
'''
ab1 = "E:/Python/niw-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)
'''



'''

#n=3


nlevel=3
r=((2/a)**(1/2))*np.sin((3*np.pi*m)/a) 
y2 = []
y2 = np.append(y2,vec[:,z[2]])
y2 = np.append(y2,0)
y2 = np.insert(y2,0,0)
invt=sum(abs(y2)**2)*h
y2=y2/np.sqrt(invt)


plt.figure(5)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25) 
#plt.plot(m,np.abs(r)**2, 'b',   linewidth=4.0 ,label='Any')
plt.plot(x,np.abs(y2)**2, 'r',linewidth=3.0,markersize=10, label='Num')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_3(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20}  )

ab1 = "E:/Python/pniw-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)


    



plt.figure(6)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25)
#plt.plot(m,r, 'b',   linewidth=4.0 ,label='Any')
plt.plot(x,y2, 'r',linewidth=3.0,markersize=10, label='Num')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$\psi_3(x)$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=25)
plt.yticks(color='k', size=25)
plt.show() 
plt.legend( loc='upper right', numpoints = 1,fancybox=False, shadow=False, prop={"size":20} )

ab1 = "E:/Python/niw-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)
'''
                    
                                                      
                                                                                                                                                                          