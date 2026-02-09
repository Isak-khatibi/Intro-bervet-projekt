import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v:np.array):
    a1 = 546.6
    a2 = 50.31
    a3 = 0.2584
    a4 = 0.008210
    C = a1*(1/v) + a2 + a3*v + a4*v**2
    '''plt.plot(v, C)
    plt.xlabel('v (km/h)')
    plt.ylabel('C (Wh/km)')
    plt.xlim(0, 200)
    plt.show()'''
    return C


### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

def trapetsmetoden(n, a, b, funk):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)

    T = funk(x[0]) + funk(x[-1])
    T += 2 * np.sum(funk(x[1:-1]))

    return (h / 2) * T

### PART 2A ###
def time_to_destination(x, route, n):
    funk_s = lambda s : 1/(velocity(s, route))
    
    T = trapetsmetoden(n, 0 , x, funk_s) 
    
    return T



'''print(time_to_destination(65, 'speed_anna.npz', 1000000))
print(time_to_destination(65, 'speed_elsa.npz', 1000000))'''
### PART 2B ##

def total_consumption(x, route, n):
    c_vs = lambda s: consumption(velocity(s, route))

    E = trapetsmetoden(n, 0, x, c_vs)

    return E



def Tolerans(n, integral, x, route, tol):
    
    
    while n < 10000:
        delta =  integral(x, route, 2*n) - integral(x, route, n)
        if abs(delta) < tol:
            rätt_intervall = 2*n
            return rätt_intervall
        n += 1

    return 'testa på ett högre intervall'

def Konvergensstudie(integral,route, x = 65 ):
    integral_exakt = integral(x, route , 50000000)
    n = 1
    int_fel = []
    n_plotlist = []
    förväntad = []
    
    
    while n < 50000000:
        n_plotlist.append(n)
        int_fel.append(abs(integral_exakt - integral(x, route, n)))
      
        C = int_fel[0] * n_plotlist[0]**2
        förväntad.append(C / n**2)
        n = 2*n

    plt.loglog(n_plotlist, int_fel)
    plt.plot(n_plotlist, förväntad, 'r--')
    plt.xlabel('n, antal delintervall')
    plt.ylabel('integralfel')
    return plt.show()
'''print(total_consumption(65, 'speed_anna.npz',  1000000))
print(total_consumption(65, 'speed_elsa.npz',  1000000))'''
'''print(Tolerans(100, time_to_destination, 65, 'speed_anna.npz', 0.01))'''

Konvergensstudie(time_to_destination, 'speed_anna.npz')

### PART 3A ###
def distance(T, route): 
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('distance not implemented yet!')

### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')
