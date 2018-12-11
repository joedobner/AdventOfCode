#!/usr/bin/python

ser = 7403

class Cell(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.rackid = self.x + 10
    self.powerlevel = self.rackid * self.y + ser 
    self.powerlevel = self.powerlevel * self.rackid 
    if self.powerlevel < 100:
      self.powerlevel = -5
    else:
      self.powerlevel = int(str(self.powerlevel)[-3]) -5

class Grid(object): 
  def __init__(self):
    self.cells = []
    for i in range(300):
      self.cells.append([]) 
      for j in range(300):
        self.cells[i].append(Cell(i, j))

  def powersquare(self, x, y, scale):
    power = 0
    for i in range(scale):
      for j in range(scale):
        power += self.cells[x + i][y + j].powerlevel
    return power
    
     


g = Grid()
maxpower = 0
maxx = 0
maxy = 0
z = 1
while z <= 300:
  for i in range(301 - z):
    for j in range(301 - z):
      mp = g.powersquare(i, j, z)
      if mp > maxpower:
        maxpower = mp
        maxx = i
        maxy = j
        maxs = z
  print z
  z += 1


print maxx
print maxy
 
