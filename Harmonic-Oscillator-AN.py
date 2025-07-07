from matplotlib import pyplot as plt
import numpy as np

 


N =800
a = 10
x = np.linspace(-a,a,N) 
h = x[1]-x[0] 

 

xx = np . zeros (( N ) , dtype = float )

for i in range ( N ) :
   xx [ i ]= (x [ i ] )**2

Vpot=xx/2

T =  np . zeros (( N-2, N-2 ) , dtype = complex ) # np.zeros((N-2)**2).reshape(N-2,N-2)

for i in range(N-2):
    for j in range(N-2):
        if i==j:
            T[i,j]= -2
        elif np.abs(i-j)==1:
            T[i,j]=1
        else:
            T[i,j]=0
            
V = np . zeros (( N-2, N-2 ) , dtype = float )   # np.zeros((N-2)**2).reshape(N-2,N-2)

for i in range(N-2):
    for j in range(N-2):
        if i==j:
            V[i,j]= Vpot[i+1]
        else:
            V[i,j]=0
                        
H = -(T/(2*h**2)) + V
val,vec=np.linalg.eig(H)
z = np.argsort(val) 
z = z[0:7] #to print first 2 energies
energies=(val[z]/val[z][0])
print(energies)

#n=0
nlevel=0
y = []
y = np.append(y,vec[:,z[0]])
y = np.append(y,0)
y = np.insert(y,0,0)
invt=sum(abs(y)**2)*h
y=y/np.sqrt(invt)

s= ((1/(np.pi))**(1/4))*(np.exp(-xx/2))
 

plt.figure(1)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25) 
plt.plot(x,np.abs(y)**2, 'r*',linestyle='-', marker='o',label='Num')
plt.plot(x,np.abs(s)**2,'b',linestyle='-', label='Any')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_0(x)|^2$', fontsize=30,fontweight='bold')
#plt.plot(x,d,color="grey")
plt.xticks(color='k', size=12)
plt.yticks(color='k', size=12)
plt.show() 
plt.legend( loc='upper right', numpoints = 1, fancybox=False, shadow=False, prop={"size":20} )
ab1 = "E:\Documents\Project\latex-work\Thesis\hop-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)

#n=1
nlevel=1
y1 = []
y1 = np.append(y1,vec[:,z[1]])
y1 = np.append(y1,0)
y1 = np.insert(y1,0,0)
invt=sum(abs(y1)**2)*h
y1=y1/np.sqrt(invt)

s1= (((np.pi))**(-1/4))*(np.sqrt(2))*x*(np.exp(-(xx)/2 ))
plt.figure(2)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25) 
#plt.plot(x,y1, 'r*',linestyle='-', marker='o',label='Num')
#plt.plot(x,s1, 'b',linestyle='-', label='Any')
plt.plot(x,np.abs(y1)**2, 'r*',linestyle='-', marker='o',label='Num')
plt.plot(x,np.abs(s1)**2, 'b',linestyle='-', label='Any')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
#plt.ylabel('$\psi_1(x)$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_1(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=12)
plt.yticks(color='k', size=12)
plt.legend( loc='upper right', numpoints = 1, fancybox=False, shadow=False, prop={"size":20} )
plt.show()
ab1 = "E:\Documents\Project\latex-work\Thesis\hop-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)

#n=2
nlevel=2
y2 = []
y2 = np.append(y2,vec[:,z[2]])
y2 = np.append(y2,0)
y2 = np.insert(y2,0,0)
invt=sum(abs(y2)**2)*h
y2=y2/np.sqrt(invt)

s2=(((np.pi))**(-1/4))*(1/(np.sqrt(8)))*((4*xx)-2)*(np.exp(-(xx)/2 ))
plt.figure(3)
plt.gcf().subplots_adjust(bottom=0.17)
plt.gcf().subplots_adjust(left=0.25) 
plt.plot(x,np.abs(y2)**2, 'r*',linestyle='-', marker='o',label='Num')
plt.plot(x,np.abs(s2)**2,'b',linestyle='-', label='Any')
plt.xlabel('$x$', fontsize=30,fontweight='bold')
plt.ylabel('$|\psi_2(x)|^2$', fontsize=30,fontweight='bold')
plt.xticks(color='k', size=12)
plt.yticks(color='k', size=12)
plt.legend( loc='upper right', numpoints = 1, fancybox=False, shadow=False, prop={"size":20} )
plt.show()
ab1 = "E:\Documents\Project\latex-work\Thesis\hop-%g.png" %(nlevel)      
plt.savefig(ab1, format='png', dpi=1000)
