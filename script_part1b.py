import matplotlib.pyplot as plt
import numpy as np


import roadster



 
# Läs in data från Anna
distance, speed= roadster.load_route('speed_anna.npz')


regspeed = roadster.velocity(distance, 'speed_anna.npz')

plt.scatter(distance, speed)
plt.plot()
plt.autoscale()
plt.show()


