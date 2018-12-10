#!/usr/bin/python
import sys

class star(object):
  def __init__(self, x, y, vx, vy):
    self.x = int(x)
    self.y = int(y)
    self.vx = int(vx)
    self.vy = int(vy)

  def step(self, stepval):
    self.x += stepval * self.vx
    self.y += stepval * self.vy
  
class starfield(object):
  def __init__(self):
    self.field = []
    self.ymin = None
    self.ymax = None
    self.xmin = None
    self.xmax = None
    self.stepcount = 0
    self.increasing = None

  def stepall(self, mult=1):
    self.stepcount += mult
    s = self.spread()
    self.ymin = self.field[0].y
    self.ymax = self.field[0].y
    self.xmin = self.field[0].x
    self.xmax = self.field[0].x
    for star in self.field:
      star.step(mult)
      if star.x > self.xmax:
        self.xmax = star.x
      if star.y > self.ymax:
        self.ymax = star.y
      if star.x < self.xmin:
        self.xmin = star.x
      if star.y < self.ymin:
        self.ymin = star.y
    if self.spread() > s:
      self.increasing = True
    else:
      self.increasing = False

  def spread(self):
    if self.xmin is None:
      return sys.maxint
    else:
      return abs(self.xmax-self.xmin) + abs(self.ymax - self.ymin)

  def pretty(self):
    field = []
    for x in range(self.xmin, self.xmax+1):
      field.append([])
      for y in range(self.ymin, self.ymax+1):
        field[x - self.xmin].append(" ")
    for star in self.field:
      field[star.x - self.xmin][star.y - self.ymin] = "#"
    for y in range(self.ymin, self.ymax+1):
      line = "" 
      for x in range(self.xmin, self.xmax+1):
        line += field[x-self.xmin][y-self.ymin]
      print line
   

stars = starfield()
#with open("d10p0input_sanitized.txt", "r") as input:
with open("d10p1input_sanitized.txt", "r") as input:
  for stardef in input.read().strip().split('\n'):
    x, y, vx, vy = stardef.split()
    stars.field.append(star(x, y, vx, vy))
 
stride = 100
stars.stepall(1)
# stride forward until spread increases
while not stars.increasing:
  stars.stepall(stride)
# Step back until spread increases
stars.stepall(-1)
while not stars.increasing:
  stars.stepall(-1)
# One step forward and that's the min
stars.stepall(1)

stars.pretty()

print stars.stepcount
