import math
class Vector:
    """ First build __init__ function to attributes the object.
    Build the function that can count add,  length, dot, multiply and subtract.
    And build the function __repr__ that can show the result if no initial value is provided.
    Every function I need to use self is a parameter because I want to decide location that will use in the function.
    Define a vector in 2D space

    Each Vector object contains two attributes: x and y.  They can be
    optionally initialized via the constructor.
    >>> v1 = Vector(x=3, y=6)
    >>> v1.x, v1.y
    (3, 6)

    If no initial value is provided, the default value of zero is assigned.
    >>> v2 = Vector()
    >>> v2.x, v2.y
    (0, 0)
    >>> v3 = Vector(x=5)
    >>> v3.x, v3.y
    (5, 0)
    >>> v4 = Vector(y=2)
    >>> v4.x, v4.y
    (0, 2)

    The length method returns the length of the vector.
    >>> u = Vector(3, 4)
    >>> v = Vector(5, 12)
    >>> u.length()
    5.0
    >>> v.length()
    13.0

    When represented as a string, a Vector object displays the values of its x
    and y attributes as shown:
    >>> v1 = Vector(3, 4)
    >>> v1
    Vector(x=3, y=4)
    >>> print(v1)
    Vector(x=3, y=4)
    >>> v2 = Vector()
    >>> v2
    Vector(x=0, y=0)
    >>> print(v2)
    Vector(x=0, y=0)

    The dot method computes the dot product of the current vector and the
    specified vector.
    >>> u = Vector(3, 4)
    >>> v = Vector(5, 2)
    >>> u.dot(v)
    23
    >>> v.dot(u)
    23
    >>> print(u, v)
    Vector(x=3, y=4) Vector(x=5, y=2)

    The add and subtract methods compute and return a new Vector object by
    adding and subtracting the current vector to and from the specified
    vector.  The multiply method multiplies the current vector with the
    specified scalar and returns a new Vector object.

    Suppose we have the vectors u and v defined as follows:
    >>> u = Vector(2, 5)
    >>> v = Vector(3, 8)

    The following computes w = u+v.
    >>> w = u.add(v)
    >>> print(u, v, w)
    Vector(x=2, y=5) Vector(x=3, y=8) Vector(x=5, y=13)

    The following computes x = u-v.
    >>> x = u.subtract(v)
    >>> print(u, v, x)
    Vector(x=2, y=5) Vector(x=3, y=8) Vector(x=-1, y=-3)

    The following computes y = 3v.
    >>> y = v.multiply(3)
    >>> print(v, y)
    Vector(x=3, y=8) Vector(x=9, y=24)

    The following computes z = v + 2u.
    >>> z = v.add(u.multiply(2))
    >>> print(u, v, z)
    Vector(x=2, y=5) Vector(x=3, y=8) Vector(x=7, y=18)

    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt((self.x**2)+(self.y**2))
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    def dot(self, v):
        return (self.x * v.x) + (self.y * v.y)
    def add(self, v):
        return Vector((self.x + v.x), (self.y + v.y))
    def subtract(self, v):
        return Vector((self.x - v.x), (self.y - v.y))
    def multiply(self, s):
        return Vector((self.x * s), (self.y * s))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

