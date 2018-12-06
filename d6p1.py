#!/usr/bin/python
import re

i = 0

class coord(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.coordcount = 0
    self.infinite = False

  def distance(self, x, y):
    return abs(x - self.x) + abs(y - self.y) 
  

coords = {}
with open("d6p1input.txt", "r") as input:
  i = 0
  for coordinate in input.read().strip().split('\n'):
    x, y = coordinate.split(', ')
    print("%s %s" % (x, y))
    coords[i] = coord(int(x) + 200, int(y) + 200)
    i += 1

for i in range(600):
  for j in range(600):
    print("%d %d" % (i, j))
    distance = 8000
    newlow = False
    for c in coords.keys():
      if coords[c].distance(i, j) < distance:
        distance = coords[c].distance(i, j)
        newlow = c 
      elif coords[c].distance(i, j) == distance:
        newlow = False
    if newlow:
      coords[newlow].coordcount += 1     
      if i in (0, 599) or j in (0, 599):
        coords[newlow].infinite = True
      
max = 0
for c in coords.keys():
  if coords[c].coordcount > max and not coords[c].infinite:
    max = coords[c].coordcount

print max
   
