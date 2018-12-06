#!/usr/bin/python 

minlength = 50000
winnar = '0'
for c in 'abcdefghijklmnopqrstuvwxyz':
  with open("d5p1input.txt", "r") as input:
    poly = input.read()
    poly = poly.strip()
    i = 0
    plen = len(poly) - 1
    while i < plen:
      if ( poly[i].islower() and poly[i].upper() == poly[i+1] ) or (poly[i].isupper() and poly[i].lower() == poly[i+1] ) or poly[i] == c or poly[i].lower() == c:
        if poly[i] == c or poly[i].lower() == c:
          poly = poly[:i:] + poly[i+1::]
          plen -= 1
          if i > 0:
            i -= 1
        else:
          poly = poly[:i:] + poly[i+2::]
          if i > 0:
            i -= 1
          plen -= 2 
      else:
         i += 1
    if len(poly) < minlength:
      minlength = len(poly)
      winnar = c

print minlength
print winnar
