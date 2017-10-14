from __future__ import division
def area():
    while True:
        r = raw_input ("What is the radius of the circle(if you only have diamater press enter): ")
        if r == '':
            d = raw_input ("What is the diamater: ")
            r = int(d) / 2
            print 3.14 * int(r)** 2 
        else:
            print 3.14 * int(r)** 2
area()