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


tf=5 #final time in seconds
tstep=0.01#size of the time step
x0=10 #magnitude of min/max x value
y0=10 #" y value
step=1 #step to create mesh


t = np.arange(0,tf+tstep,tstep) #set up time for problem

x = np.arange(-x0,x0+step,step) #Solving 2D mhd problem
y = np.arange(-y0,y0+step,step)  


X,Y = np.meshgrid(x,y) #2D meshgrid


#Define the parameter values
rho = 1 #the density of the plasma
b0 = 1 #the B field amplitude in Gaussian units
v0 = 1 #velocity

#Specify the pressure field
P = -rho/4*(np.cos(2*X)+np.sin(2*Y))

#set up the B field and velocity arrays
bx = np.zeros((len(t),len(x),len(y)))
by = np.zeros((len(t),len(x),len(y)))

vx = np.zeros((len(t),len(x),len(y)))
vy = np.zeros((len(t),len(x),len(y)))



#Initial conditions of the plasma

bx[0] = b0*np.cos(2*X)*np.sin(2*Y)
by[0] = -b0*np.sin(2*X)*np.cos(2*Y)


vx[0] = v0*np.sin(X)*np.cos(Y)
vy[0] = -v0*np.cos(X)*np.sin(Y)


#Empty arrays to keep track of changes in time
Ev=np.zeros(len(t))
Eb=np.zeros(len(t))

Ev[0]=0.5*(vx[0][0][0]**2+vy[0][0][0]**2)
Eb[0]=0.5*(bx[0][0][0]**2+by[0][0][0]**2)

#Euler Step for B and v 

i=0
while i < len(t)-1:
	for j in range(len(x)-1):
		for k in range(len(y)-1):
			bx[i+1][j][k] = bx[i][j][k]+tstep*(-vx[i][j][k]*(bx[i][j+1][k]-bx[i][j][k])/step+bx[i][j][k]*(vx[i][j+1][k]-vx[i][j][k])/step)
			by[i+1][j][k] = by[i][j][k]+tstep*(-vy[i][j][k]*(by[i][j][k+1]-by[i][j][k])/step+by[i][j][k]*(vy[i][j][k+1]-vy[i][j][k])/step)
		
			vx[i+1][j][k] = vx[i][j][k]+tstep*(vx[i][j][k]*(vx[i][j+1][k]-vx[i][j][k])/step-(P[j+1][k]-P[j][k])/step-by[i][j][k]*(by[i][j+1][k]-by[i][j][k])/step)
			vy[i+1][j][k] = vy[i][j][k]+tstep*(vy[i][j][k]*(vy[i][j][k+1]-vy[i][j][k])/step-(P[j][k+1]-P[j][k])/step+bx[i][j][k]*(bx[i][j][k+1]-bx[i][j][k])/step)



	Ev[i+1]=0.5*(vx[i+1][0][0]**2+vy[i+1][0][0]**2)
	Eb[i+1]=0.5*(bx[i+1][0][0]**2+by[i+1][0][0]**2)
	i=i+1
			
print(bx[len(t)-1])

fig0=plt.figure()
ax1=fig0.add_subplot(1,1,1)
ax2 = ax1.twinx()
ax1.plot(t,Eb,'b-')
ax2.plot(t,Ev,'r-')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Kinetic Energy')
ax2.set_ylabel('Magnetic Energy')



plt.tight_layout()
plt.show()
plt.close()


# plt.tight_layout()
# plt.show()
# plt.close()