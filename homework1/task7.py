import numpy as np

def numpy_demo(val_a, val_b):
    array_a = np.array([[val_a, val_b]])
    return array_a.dtype
    

if __name__ == "__main__":
    data_type = numpy_demo(3,2)
    print(data_type)