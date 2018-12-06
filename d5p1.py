#!/usr/bin/python 

with open("d5p1input.txt", "r") as input:
  reax = True
  poly = input.read()
#  poly = "dDDDdabAcCaCBAcCcaDApEeP"
  poly = poly.strip()
  while reax == True:
    reax = False
    #print "whoop here we go"
    i = 0
    plen = len(poly) - 1
    while i < plen:
      if ( poly[i].islower() and poly[i].upper() == poly[i+1] ) or (poly[i].isupper() and poly[i].lower() == poly[i+1] ):
#       print "reacted " + poly[i] + poly[i+1] + " " + str(i) + " " + str(plen) + " remaining." 
        poly = poly[:i:] + poly[i+2::]
        if i > 0:
          i -= 1
        plen -= 2 
#       print "New string is " + str(len(poly))
        reax = True
      else:
         i += 1

print len(poly)
