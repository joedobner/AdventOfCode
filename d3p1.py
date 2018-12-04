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
    ko = []
    for i in range(self.x, self.x + self.width):
      for j in range(self.y, self.y + self.height):
        ko.append([i, j])
    return ko

collisions = 0
fabric = [ ([0] * 1000) for row in range(1000) ]
with open("d3p1input.txt", "r") as input:
  for pattern in input.read().split('\n'):
    if not re.match("^[	 ]*$", pattern):
      p = Pattern(pattern)
      for ko in p.knockouts():
        fabric[ko[0]][ko[1]] += 1
        if fabric[ko[0]][ko[1]] == 2:
          collisions += 1


print collisions
