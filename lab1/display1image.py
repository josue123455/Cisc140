import sys
import stddraw
from picture import Picture

def main():
    fname = sys.argv[1]
    pic = Picture(fname)
    stddraw.setCanvasSize(pic.width(), pic.height())
    stddraw.picture(pic)
    stddraw.show(2000)

if __name__ == '__main__':
    main()
# python display1image.py image4.jpg
