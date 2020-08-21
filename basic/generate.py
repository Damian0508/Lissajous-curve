import math
from io import StringIO

import matplotlib.pyplot as plt
import numpy as np

def generate_lissajou_curve(x_frequency, y_frequency, phase, simulation_time):
    time = np.arange(0, simulation_time, 0.0001)
    phase_rad = phase * (math.pi / 180)
    x = [math.sin(x_frequency*t + phase_rad) for t in time]
    y = [math.sin(y_frequency*t) for t in time]

    fig = plt.figure(figsize=(7,7))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])
    plt.yticks([])

    figure = plt.plot(x, y)
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data