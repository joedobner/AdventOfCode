#!/usr/bin/python

ser = 7403
#ser = 18

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
  def __init__(self, scale):
    self.cells = []
    for i in range(scale):
      self.cells.append([]) 
      for j in range(scale):
        self.cells[i].append(Cell(i, j))

  def powersquare(self, x, y, scale):
    power = 0
    for i in range(scale):
      for j in range(scale):
        power += self.cells[x + i][y + j].powerlevel
    return power
    
     

scale = 300
g = Grid(scale)
#scratchgrid = []
sg = []
for i in range(scale):
  sg.append([])
  for j in range(scale):
    sg[i].append(g.cells[i][j].powerlevel)

maxpower = 0
maxx = 0
maxy = 0
z = 1
while z <= scale:
  for i in range(scale - z):
    for j in range(scale - z):
      p = sg[i][j]
      for a in range(z):
        p += g.cells[i + z][j + a].powerlevel
        p += g.cells[i + a][j + z].powerlevel
      p += g.cells[i + z][j + z].powerlevel
      sg[i][j] = p
      if p > maxpower:
        maxpower = p
        maxx = i
        maxy = j
        maxz = z + 1
  print z
  z += 1


print "max"
print maxx
print maxy
print maxz
 
