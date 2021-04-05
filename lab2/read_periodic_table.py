import stdio
import stdarray
import sys
from element import Element
from instream import InStream

filename = sys.argv[1]
file = InStream(filename)

n = -1

while file.hasNextLine():
    file.readLine()
    n += 1


file = InStream(filename)

header = file.readLine()

elarray = stdarray.create1D(n)
i = 0

while file.hasNextLine():
    Rline = file.readLine()
    array = stuff.split(',')
    elem = Element(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7])

    elarray[i] = elem
    i += 1
print (elem)
print (Rline)

# finish tomorrow and figure out whats going on exactly the lab is basicly done
