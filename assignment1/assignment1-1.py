from helpers import plot_poles, plot_measurements
import matplotlib.pyplot as plt
import numpy as np
import math

def distance(location, pole_location):
    ### STUDENT CODE START
    x_length = abs(location[0] - pole_location[0])
    y_length = abs(location[1] - pole_location[1])
    output = math.sqrt(x_length**2 + y_length**2)
    ### STUDENT CODE END
    return output


def calc_dist(location, poles):
    print("Dist 1: " + str(distance(location, poles[0])))
    print("Dist 2: " + str(distance(location, poles[1])))
    print("Dist 3: " + str(distance(location, poles[2])))


location = [10, 5]
poles = [[0, 0]]
poles += [[3, 2]]
poles += [[7, 4]]

plot_poles(poles)
plt.title('Pole Location')
plt.show()

plot_poles(poles)
plot_measurements(location, poles)
plt.title('Pole Measurements')
plt.show()

calc_dist(location, poles)
