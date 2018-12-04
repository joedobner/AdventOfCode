#!/usr/bin/python
import re

class Pattern(object):
  def __init__(self, line):
    fields = re.split(" ",line)
    self.name = fields[0]
    coord = fields[2]
    self.x = int(re.split("[,:]", fields[2])[0])
    self.y = int(re.split("[,:]", fields[2])[1])
    self.width = int(re.split("x", fields[3])[0])
    self.height = int(re.split("x", fields[3])[1])
 
  def knockouts(self):
    ko = set()
    for i in range(self.x, self.x + self.width):
      for j in range(self.y, self.y + self.height):
        ko.add(str(i)+","+str(j))
    return ko

  def prettyprint(self):
    print self.name + ":" + " ".join(self.knockouts())


fabric = []
for i in range(1000):
  fabric[i] = []
  for j in range(1000):
    fabric[i][j] = 0
with open("d3p1input.txt", "r") as input:
  for pattern in input.read().split('\n'):
    if not re.match("^[	 ]*$", pattern):
      p = Pattern(pattern)
      print len(fabric.keys())
      for ko in p.knockouts():
        if ko not in fabric.keys():
          fabric[ko] = False
        else: 
          fabric[ko] = True

collisions = 0
for swatch in fabric.keys():
  if fabric[swatch]:
    collisions += 1
print collisions
