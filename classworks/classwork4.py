import numpy as np
import pandas as pd

arr1 = np.array([1,2,3,4])
arr2 = np.array([1.0, 1.2, 1.5, 1.8])

sqr_arr1 = arr1 ** 2
sqr_arr2 = arr2 ** 2

data = {
    "x1" : arr1,
    "y1" : arr2,
    "sqr_x" : sqr_arr1,
    "sqr_y" : sqr_arr2
}

data_frame = pd.DataFrame(data)
