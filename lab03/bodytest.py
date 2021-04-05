from body import Body
from vector import Vector
import stddraw


def main():#testing for no gravity there is no information for positon or vellcity since there is no gravity everything will just float to the top of the canvas
    r1 = Vector([ 0 , 0])
    r2 = Vector([0, 0])

    v0 = Vector([0,0])

    body1 = Body(0, r1, v0, 0)
    body2 = Body(0, r2, v0, 0)



    stddraw.setXscale(10,10)
    stddraw.setYscale(10, 10)

    dt = 10000

    while True:
        body1.draw()
        body2.draw()

        magnitude1 = body1.forceFrom(body2)
        magnitude2 = body2.forceFrom(body1)

        body1.move(dt, magnitude1)
        body2.move(dt, magnitude2)

        stddraw.show(20)
        stddraw.clear()


def main():
    r1 = Vector([ 3e3 , 4e3])
    r2 = Vector([-1e2, -3e2])

    v0 = Vector([0,0])

    body1 = Body(1e15, r1, v0, 0.25)
    body2 = Body(3e15, r2, v0, 0.15)



    stddraw.setXscale(-5e3, 5e3)
    stddraw.setYscale(-5e3, 5e3)

    dt = 10000

    while True:
        body1.draw()
        body2.draw()

        magnitude1 = body1.forceFrom(body2)
        magnitude2 = body2.forceFrom(body1)

        body1.move(dt, magnitude1)
        body2.move(dt, magnitude2)

        stddraw.show(20)
        stddraw.clear()


if __name__ == '__main__':
    main()
