import pandas as pd
import numpy as np

def linearData(w1 = 1, b = 0, num_points = 10, noise = 1, data_range = [0,9]):
    x = pd.Series(np.linspace(data_range[0], data_range[1], num_points))
    y = w1*x+b
    y+= np.random.random_sample(num_points)*2-1

    df = pd.DataFrame({'x':x, 'y':y})
    return df
