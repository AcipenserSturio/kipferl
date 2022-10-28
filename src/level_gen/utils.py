"""
Miscellaneous utilities that are not provided by numpy.
"""
import numpy as np

def euclidean(x1, x2, y1, y2):
    """
    Calculate Euclidean distance with numpy operators.
    """
    # pylint: disable=invalid-name
    # Argument names are appropriate for maths.
    return np.sqrt(np.abs(x1-x2)**2+np.abs(y1-y2)**2)

def linear(value, x1, x2, y1, y2):
    """
    Do a 1d linear transform with numpy operators
    from an old range of possible values to a new one.
    """
    # pylint: disable=invalid-name
    # Argument names are appropriate for maths.
    return (y1-y2)*(value-x1)/(x1-x2) + y1

def sigmoid(value):
    """Apply a sigmoid function to the value with numpy operators."""
    return np.tanh(np.tan(np.pi*value/2))

def semicircle(value):
    """Apply a semicircle function to the value with numpy operators."""
    return np.sqrt(4-(value-1)**2)-1
