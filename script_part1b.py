import matplotlib.pyplot as plt
import numpy as np


import roadster



 
# Läs in data från Anna
distance, speed= roadster.load_route('speed_elsa.npz')


regspeed = roadster.velocity(distance, 'speed_elsa.npz')

plt.scatter(distance, speed)
plt.plot(distance, regspeed)
plt.xlim(0, 15)
plt.ylabel('v (km/h)')
plt.xlabel('s (km)')
plt.show()
