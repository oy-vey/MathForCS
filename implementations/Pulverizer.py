#!/usr/bin/env python3

import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])

x,y = a,b
c,d,e,f = (1,0,0,1)
q = x // y
print("x: ",x,"y: ",y)
print("x = ",c,"a", d,"b","y = ", e,"a", f,"b")
print("q: ", q)


while x % y != 0:

    q = x // y
    x, y = y, x % y
    c,d,e,f = (e, f, c-q * e, d-q * f)
    print("x: ",x,"y: ",y)
    print("x = ",c,"a", d,"b","y = ", e,"a", f,"b")
    print("q: ", q)

x, y = y, x
c, d = e, f
print("gcd:", x)
print("s: ", c, "t: ", d)
