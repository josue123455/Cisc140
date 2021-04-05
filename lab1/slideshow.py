import sys
import stddraw
from picture import Picture



def main():
    for i in range(1, len(sys.argv)):
        pic = Picture (sys.argv[i])
        stddraw.picture(pic)
        stddraw.show(2000)





if __name__ == '__main__':
    main()


# python SequenceofImages.py image1.jpg image2.jpg image3.jpg image4.jpg
