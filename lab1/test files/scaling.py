import sys
import stddraw
from picture import Picture




fileName = sys.argv[1]
w = int(sys.argv[2])
h = int(sys.argv[3])

source = Picture(fileName)
target = Picture(w, h)

for tCol in range(w):
    for tRow in range(h):
        sCol = tCol * source.width() // w
        sRow = tRow * source.height() // h
        target.set(tCol, tRow, source.get(sCol, sRow))

stddraw.setCanvasSize(w, h)
stddraw.picture(target)
stddraw.show(2000)

#-----------------------------------------------------------------------

# python scaling.py image4.jpg 800 800

# python scaling.py mandrill.jpg 600 300

# python scale.py mandrill.jpg 200 400

# python scale.py mandrill.jpg 200 200

# python scale.py mandrill.png 200 200

# python scale.py darwin.jpg 200 200



# python scaling.py image4.jpg 800 800
