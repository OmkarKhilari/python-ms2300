# Additional Method 
# The Egyptian Octagon Method 

import numpy as np

def egyptian_octagon(r):
    area = ((7/9) * r * r)*4
    return area

def error_analysis(r):
    og_area = np.pi * r ** 2
    eo_area = egyptian_octagon(r)

    error = (np.abs(og_area - eo_area) / og_area)*100

    return error

r = 50
print(egyptian_octagon(r))
print(error_analysis(r))