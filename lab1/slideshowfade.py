import sys
import stddraw
from picture import Picture
from color import Color
import math


#

def fade(current_pic,next_pic):
    pass

def blend(c1, c2, alpha):
    r = (1-alpha)*c1.getRed()   + alpha*c2.getRed() #+ #alpha*c3.getRed() + alpha*c4.getRed()
    g = (1-alpha)*c1.getGreen() + alpha*c2.getGreen()# + alpha*c3.getGreen() + alpha*c4.getGreen()
    b = (1-alpha)*c1.getBlue()  + alpha*c2.getBlue() #+ alpha*c3.getBlue() + alpha*c4.getBlue()
    return Color(int(r), int(g), int(b))

#-----------------------------------------------------------------------

# Accept strings sourceFile and targetFile and integer frameCount
# as command-line arguments. Read images from sourceFile and targetFile.
# Then, over the course of frameCount frames, gradually replace the
# image from sourceFile with the image with the image from targetFile.
# Display to standard draw each intermediate image. The images in the
# files can be in either JPG or PNG formats.

sourceFile = sys.argv[1]
targetFile = sys.argv[2]
n = 2     # number of intermediate frames

source = Picture(sourceFile)
target = Picture(targetFile)

width = source.width()
height = source.height()

stddraw.setCanvasSize(width, height)

pic = Picture(width, height)

for t in range(n + 2):
    for col in range(width):
        for row in range(height):
            c0 = source.get(col, row)
            cn = target.get(col, row)
            alpha = float(t) / float(n)
            c = blend(c0, cn, alpha)
            pic.set(col, row,c)
    stddraw.picture(pic)
    stddraw.show(2000)

stddraw.show()


def main():
    for i in range(1, len(sys.argv)):
        pic = Picture (sys.argv[i])
        fade(pic)
        stddraw.setCanvasSize(pic.width(), pic.height())
        stddraw.picture(pic)
        stddraw.show(2000)


if __name__ == '__main__':
    main()
# python slideshowfade.py image1.jpg image2.jpg image3.jpg image4.jpg
