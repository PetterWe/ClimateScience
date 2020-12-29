###Climate science model 1 - naked planet with a thick layer of water### 
#The heat capacity of of the planet is dHeatContent/dt = L*(1-albedo)/4 - epsilon * sigma * T^4
#T[K]=HeatContent [J/m^2] / HeatCapacity [J/m^2K]
#HeatContent(t+1)=HeatContent(t)+dHeatContent/dT*TimeStep
import numpy as np
import matplotlib.pyplot

nSteps=int(input("")) #number of iterations
timeStep=10 #years
waterDepth=4000 #meters
L=1350 #influx W/m^2
albedo=0.3
epsilon=1
sigma=0.0000000567 #Boltzmans constant W/m^2K^4

time_list=[0] #starting conditions
temperature_list=[400] #starting conditions


heatCapacity=waterDepth*4200000 #the specific heat capacity of water is 4179.6 J·kg^−1·K^−1
heatContent=heatCapacity*temperature_list[0] #heat content is of course the heat capacity times the temperature
heatIn=L*(1-albedo)/4 #influx
heatOut=epsilon*sigma*pow(temperature_list[-1],4) #outflux

for itime in range(0,nSteps):
    time_list.append(timeStep+time_list[-1])
    heatContent=heatContent+(heatIn-heatOut)*timeStep*31400000 #approximation of seconds in a year
    temperature_list.append(heatContent/heatCapacity)
    heatOut=epsilon*sigma*pow(temperature_list[-1],4)
    
    
print(temperature_list[-1],heatOut)

matplotlib.pyplot.plot(time_list, temperature_list)
matplotlib.pyplot.show()
