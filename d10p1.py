#!/usr/bin/python
import re

i = 0

class star(object):
  def __init__(self, x, y, vx, vy):
    self.x = int(x)
    self.y = int(y)
    self.vx = int(vx)
    self.vy = int(vy)

  def step(self):
    self.x += self.vx
    self.y += self.vy
  
class starfield(object):
  def __init__(self):
    self.field = []

  def stepall(self):
    for star in self.field:
      star.step()

  def xcompactness(self):
    starhash = {}
    for star in self.field:
      if star.x in starhash.keys():
        starhash[star.x] += 1
      else:
        starhash[star.x] = 1
    return len(starhash.keys())
      
  def ycompactness(self):
    starhash = {}
    for star in self.field:
      if star.y in starhash.keys():
        starhash[star.y] += 1
      else:
        starhash[star.y] = 1
    return len(starhash.keys())
 
  def compactness(self):
    return self.ycompactness() + self.xcompactness()

  def pretty(self):
    ymin = 10000
    ymax = -10000
    xmin = 10000
    xmax = -10000
    for star in self.field:
      if star.x > xmax:
        xmax = star.x
      if star.y > ymax:
        ymax = star.y
      if star.x < xmin:
        xmin = star.x
      if star.y < ymin:
        ymin = star.y
    field = []
    for x in range(xmin, xmax+1):
      field.append([])
      for y in range(ymin, ymax+1):
        field[x - xmin].append(" ")
    for star in self.field:
      field[star.x - xmin][star.y - ymin] = "#"
    for y in range(ymin, ymax+1):
      line = "" 
      for x in range(xmin, xmax+1):
        line += field[x-xmin][y-ymin]
      print line
   

stars = starfield()
#with open("d10p0input_sanitized.txt", "r") as input:
with open("d10p1input_sanitized.txt", "r") as input:
  for stardef in input.read().strip().split('\n'):
    x, y, vx, vy = stardef.split()
    stars.field.append(star(x, y, vx, vy))
 
cmin = 10000000
cmin_step = 0
for i in range(100000):
  stars.stepall()
  c = stars.compactness()
  if c < cmin:
    cmin = stars.compactness()
    cmin_step = i
  if c == 58:
    stars.pretty()
    print i

print cmin
print cmin_step


# print("%s %s %s %s" % (x, y, vx, vy))
#for i in range(600):
#  for j in range(600):
#    print("%d %d" % (i, j))
#    distance = 8000
#    newlow = False
#    for c in stars.keys():
#      if stars[c].distance(i, j) < distance:
#        distance = stars[c].distance(i, j)
#        newlow = c 
#      elif stars[c].distance(i, j) == distance:
#        newlow = False
#    if newlow:
#      stars[newlow].starcount += 1     
#      if i in (0, 599) or j in (0, 599):
#        stars[newlow].infinite = True
#      
#max = 0
#for c in stars.keys():
#  if stars[c].starcount > max and not stars[c].infinite:
#    max = stars[c].starcount
#
#print max
#   
