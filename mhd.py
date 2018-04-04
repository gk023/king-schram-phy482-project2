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


tf=10 #final time in seconds
tstep=1 #size of the time step
x0=2*np.pi #magnitude of min/max x value
y0=2*np.pi #" y value
z0=2*np.pi #" z value
step=0.2*np.pi #step to create mesh


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
bx = np.zeros((len(t),len(X),len(Y)))
by = np.zeros((len(t),len(X),len(Y)))

vx = np.zeros((len(t),len(X),len(Y)))
vy = np.zeros((len(t),len(X),len(Y)))



#Initial conditions of the plasma

bx[0] = b0*np.cos(2*X)*np.sin(2*Y)
by[0] = -b0*np.sin(2*X)*np.cos(2*Y)

vx[0] = v0*np.sin(X)*np.cos(Y)
vy[0] = -v0*np.cos(X)*np.sin(Y)




#Euler Step for B and v to find how bz evolves in time
#Working in the plane

for i in range(len(t)-1):
	for j in range(len(x)-1):
		for k in range(len(y)-1):
			bx[i+1][j][k] = bx[i][j][k]+vx[i][j][k]*(bx[i][j+1][k]-bx[i][j][k])/step-bx[i][j][k]*(vx[i][j+1][k]-vx[i][j][k])/step
			by[i+1][j][k] = by[i][j][k]+vy[i][j][k]*(by[i][j][k+1]-by[i][j][k])/step-by[i][j][k]*(vy[i][j][k+1]-vy[i][j][k])/step

			vx[i+1][j][k] = vx[i][j][k]-vx[i][j][k]*(vx[i][j+1][k]-vx[i][j][k])/step-(P[j+1][k]-P[j][k])/step
			vy[i+1][j][k] = vx[i][j][k]-vx[i][j][k]*(vy[i][j][k+1]-vy[i][j][k])/step-(P[j][k+1]-P[j][k])/step
	 
print(bx[5])