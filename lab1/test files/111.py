import sys
import stddraw
from picture import Picture

def main():
    test = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"]
    for i in range(len(test)):
        new = test[i]
        print(new)
        print(i)
        picture = image.open(new)
        picture.show(2000)


    #python 111.py image1.jpg image2.jpg image3.jpg image4.jpg
