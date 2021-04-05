import stddraw
from vector import Vector
import math
class Body:

    # Construct a new Body object whose position is specified by
    # Vector object r, whose velocity is specified by Vector object
    # v, and whose mass is specified by float mass.

    def __init__(self, mass, r, v, size):
        self._mass = float(mass) # Mass

        if not isinstance(r, Vector):
            raise TypeError("The position must be a vector")
        self._r = r       # Position
        if not isinstance(v, Vector):
            raise TypeError("The velocity be a vector")
        self._v = v        # Velocity
        self._size = float(size)


    # Move self by applying the force specified by Vector object
    # f for the number of seconds specified by float dt

    def move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v = self._v + (a.scale(dt))
        self._r = self._r + self._v.scale(dt)

    # Return the force between Body objects self and other.

    def forceFrom(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    # Draw self to standard draw.

    def draw(self):
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0], self._r[1])


class Densitybody():
    def __init__(self, mass, r, v, d):
        self._mass = float(mass) # Mass

        if not isinstance(r, Vector):
            raise TypeError("The position must be a vector")
        self._r = r       # Position
        if not isinstance(v, Vector):
            raise TypeError("The velocity be a vector")
        self._v = v        # Velocity
        self._d = float(d) #density

    def dens(self):
        dens = self.density/ self.mass
        return dens

    def draw(self):
        self.dens()

        stddraw.setPenRadius(0.0125 * ( volume / 4.5e10))
        stddraw.point(self.r[0], self.r[1])
class NoGravityBody():
    def __init__(self, mass, r, v, d):
        self._mass = float(mass) # Mass

        if not isinstance(r, Vector):
            raise TypeError("The position must be a vector")
        self._r = r       # Position
        if not isinstance(v, Vector):
            raise TypeError("The velocity be a vector")
        self._v = v        # Velocity
        self._d = float(d) #density
    def move(self, f, dt):
        a = f.scale(1 / self._mass)
        self._v = self._v + (a.scale(dt))
        self._r = self._r + self._v.scale(dt)

    # Return the force between Body objects self and other.

    def forceFrom(self, other):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)
        return delta.direction().scale(magnitude)

    # Draw self to standard draw.

    def draw(self):
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0], self._r[1])
