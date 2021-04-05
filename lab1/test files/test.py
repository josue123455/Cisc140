import sys
import stddraw
from picture import Picture

import sys
import math
import stddraw
from picture import Picture

# Accept a file name as a command-line argument. Read the image from
# the specified file, wave the image, and display the original image
# and the waved image.

pic1 = Picture(sys.argv[1])

width  = pic1.width()
height = pic1.height()

pic2 = Picture(width, height)

# Apply the wave filter.
for col in range(width):
    for row in range(height):
        cc = col
        rr = int(row + 20.0 * math.sin(col * 2.0 * math.pi / 64.0))
        if (rr >= 0) and (rr < height):
            pic2.set(col, row, pic1.get(cc, rr))

stddraw.setCanvasSize(width, height)
stddraw.picture(pic2)
stddraw.show(2000)


    #python test.py image1.jpg image2.jpg image3.jpg image4.jpg
