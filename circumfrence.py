from __future__ import division
def cir():
    while True:
        r = raw_input("What is the radius(if you only have diamater press enter): ")
        if r == '':
            d = raw_input("what is the diamater: ")
            r = int(d) / 2
            print 2*3.14*int(r)
        else:
            print 2*3.14*int(r)
cir()