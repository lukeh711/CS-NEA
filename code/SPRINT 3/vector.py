import numpy as np

class Vector:
    def __init__(self, xIn, yIn):
        self.xy = np.array([xIn, yIn], dtype=np.float64)

    # ADD
    def __add__(self, other):
        if isinstance(other, Vector):
            result = self.xy + other.xy
            return Vector(*result)  # *result unpacks the result (which is a numpy array) into 2 float64s, which then are input into the constructor method to create the new Vector object
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    # SUBTRACT
    def __sub__(self, other):
        if isinstance(other, Vector):
            result = self.xy - other.xy
            return Vector(*result)
        return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(-other)

    # MULTIPLY
    def __mul__(self, other):
        if isinstance(other, Vector):
            result = self.xy * other.xy
            return Vector(*result)
        if type(other) in [int, float]:
            result = self.xy * other
            return Vector(*result)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    # DIVIDE
    def __truediv__(self, other):
        if isinstance(other, Vector):
            result = self.xy / other.xy
            return Vector(*result)
        if type(other) in [int, float]:
            result = self.xy / other
            return Vector(*result)
        return NotImplemented

    # FLOOR
    def __floordiv__(self, other):
        if isinstance(other, Vector):
            result = self.xy // other.xy
            return Vector(*result)
        return NotImplemented

    # - before var
    def __neg__(self):
        result = -self.xy
        return Vector(*result)

    # iteratively unpacking
    def __iter__(self):
        yield self.xy[0]
        yield self.xy[1]

    def copy(self):
        return Vector(*self.xy.copy())

    # returning the magnitude of the vector using pythagoras
    def length(self):
        return (self.xy[0]**2 + self.xy[1]**2)**0.5

    def getX(self):
        return self.xy[0]

    def getY(self):
        return self.xy[1]