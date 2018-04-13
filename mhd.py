#MHD Project Code- Garrett and Katie
#Code used to calculate the B field, plasma velocity, kinetic energy,
#and magnetic energy and visualize results. Arrays that define the
#space and time interval being worked in are set up. Parameters related
#to the plasma can be specified. The pressure field is input. Using
#a Euler step, B field and velocity at different times are calculated.
#Spatial derivatives are evaluated using the Finite Difference Method.
#This code assumes ideal Taylor-Green flow, i.e. no resistivity or
#viscosity. Those are not coded into this simulation.
#--------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

tf=1.0#final time in seconds
tstep=0.000001#size of the time step
x0=1.0 #magnitude of min/max x value
y0=1.0 #" y value
step=0.1



t = np.arange(0,tf+step,tstep) #set up time for problem

x = np.arange(0,x0+step,step) #Solving 2D mhd problem
y = np.arange(0,y0+step,step)  


X,Y = np.meshgrid(x,y) #2D meshgrid


#Define the parameter values
rho = 1#the density of the plasma
b0 = 0.35 #initial b field in Alfven units
v0=0.35 #initial velocity


#Specify the pressure field
P=np.zeros((len(x),len(y)))
def P0(X,Y):
	return -rho/4*(np.cos(2*X)+np.sin(2*Y))
for i in range(len(x)):
	for j in range(len(y)):
		P[i][j] = P0(x[i],y[i])


#set up the B field and velocity arrays
bx = np.zeros((len(t),len(x),len(y)))
by = np.zeros((len(t),len(x),len(y)))
vx = np.zeros((len(t),len(x),len(y)))
vy = np.zeros((len(t),len(x),len(y)))



#Initial conditions of the plasma
def bx0(X,Y):
	return b0*np.sin(X)*np.cos(Y)
def by0(X,Y):
	return b0*np.cos(X)*np.sin(Y)
def vx0(X,Y):
	return v0*np.sin(X)*np.cos(Y)
def vy0(X,Y):
	return -v0*np.cos(X)*np.sin(Y)


for i in range(len(x)):
	for j in range(len(y)):
		bx[0][i][j] = bx0(x[i],y[j])
		by[0][i][j] = by0(x[i],y[j])
		vx[0][i][j] = vx0(x[i],y[j])
		vy[0][i][j] = vy0(x[i],y[j])

# Empty arrays to keep track of changes in time
Ev=np.zeros(len(t))
Eb=np.zeros(len(t))

cen = len(x)/2

Ev[0]=0.5*(vx[0][cen][cen]**2+vy[0][cen][cen]**2)
Eb[0]=0.5*(bx[0][cen][cen]**2+vy[0][cen][cen]**2)



# def rk4x(f,xx,yy,a):
	# k1=f(xx,yy)
	# k2=f(xx+a*k1/2,yy)
	# k3=f(xx+a*k2/2,yy)
	# k4=f(xx+a,yy)
	# fnew = 

def rk4y(f,xx,yy,a):
	k1=f(xx,yy)
	k2=f(xx,yy+a*k1/2)
	k3=f(xx,yy+a*k2/2)
	k4=f(xx,yy+a*k3/2)
	
def dx(f,I,J,a):
	fp = (f[I+1][J]-f[I-1][J])/(2*a)
	return fp

def dy(f,I,J,a):
	fp = (f[I][J+1]-f[I][J-1])/(2*a)
	return fp


#Euler Step for B and v assuming fluid dominates
i=0
while i < len(t)-1:
	for j in range(1,len(x)-1):
		for k in range(1,len(y)-1):

			bx[i+1][j][k] = bx[i][j][k]+tstep*(-1*vx[i][j][k]*dx(bx[i],j,k,step)+bx[i][j][k]*dx(vx[i],j,k,step))
			by[i+1][j][k] = by[i][j][k]+tstep*(-1*vy[i][j][k]*dy(by[i],j,k,step)+by[i][j][k]*dy(by[i],j,k,step))
		
			vx[i+1][j][k] = vx[i][j][k]+tstep*(-1*vx[i][j][k]*dx(vx[i],j,k,step)-dx(P,j,k,step)-0.5*dx(bx[i]**2,j,k,step))
			vy[i+1][j][k] = vy[i][j][k]+tstep*(-1*vx[i][j][k]*dy(vy[i],j,k,step)-dy(P,j,k,step)-0.5*dy(by[i]**2,j,k,step))


	Ev[i+1]=0.5*(vx[i+1][cen][cen]**2+vy[i+1][cen][cen]**2)
	Eb[i+1]=0.5*(bx[i+1][cen][cen]**2+vy[i+1][cen][cen]**2)
	i=i+1
			




fig0=plt.figure()
ax1=fig0.add_subplot(1,1,1)
ax2 = ax1.twinx()
ax1.plot(t,Eb,'b-',label='Eb')
ax2.plot(t,Ev,'r-',label='Ev')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Magnetic Energy',color='b')
ax2.set_ylabel('Kinetic Energy',color='r')




plt.tight_layout()
plt.show()
plt.close()




# fig1=plt.figure(figsize=(16,8))
# plt.xlabel('x')
# plt.ylabel('y')
# plt.streamplot(X, Y, vx[80],vy[80],color='k')



# plt.show()
# plt.close()

# fig2=plt.figure(figsize=(8,8))
# plt.xlabel('x')
# plt.ylabel('y')
# plt.imshow(np.sqrt(bx[80]**2+by[80]**2),cmap='plasma')

# plt.show()
# plt.close()
