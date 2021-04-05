#-----------------------------------------------------------------------
# fade.py
#-----------------------------------------------------------------------
import sys
import stddraw
from picture import Picture
from color import Color
import math



def fade(current_pic, next_pic):
    pass


def blend(c1, c2, aplha):
    r = (1 - aplha)*c1.getRed() + aplha*c2.getRed()
    g = (1 - aplha)*c1.getGreen() + aplha*c2.getGreen()
    b = (1 - aplha)*c1.getBlue() + aplha*c2.getBlue()
    return Color(int(r), int(g), int(b))

sourceFile = sys.argv[1]
targetFile = sys.argv[2]
n = 2



source = Picture(sourceFile)
target = Picture(targetFile)



width = source.width()
height = source.height()



pic = Picture(width, height)
for t in range(n + 1):
    for col in range(width):
        for row in range(height):
            c0 = source.get(col, row)
            cn = target.get(col, row)
            aplha = float(t) / float(n)
            c = blend(c0, cn, aplha)
            pic.set(col, row, c)
        stddraw.picture(pic)
        stddraw.show(5)
    stddraw.show(5)




def main():
    fname = sys.argv[1]
    pic = Picture(fname)
    stddraw.setCanvasSize(712, 712)

    for k in range(2, len(sys.argv)):
        for i in range(1, len(sys.argv)):
            fname = sys.argv[i]
            pic = Picture(sys.argv[i])
            stddraw.picture()
            stddraw.show(5)
        fade(pic, Picture(sys.argv[i + 1]), 5)


if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python image4.py image1.jpg image2.jpg 7

# python fade.py mandrill.jpg darwin.jpg 5

# python fade.py mandrill.jpg darwin.png 7

# python fade.py mandrill.png darwin.jpg 7

# python fade.py mandrill.png darwin.png 7

#  python image4.py image4.jpg
