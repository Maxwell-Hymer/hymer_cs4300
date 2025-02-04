import numpy as np

def numpy_demo(val_a, val_b):
    # Creates an array using numpy for the 2 argument values 
    array_a = np.array([[val_a, val_b]])
    # Checks and returns the data type using numpy
    return array_a.dtype

if __name__ == "__main__":
    data_type = numpy_demo(3,2)
    print(data_type)