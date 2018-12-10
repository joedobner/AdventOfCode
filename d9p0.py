#!/usr/bin/python

class marblecircle(object):
  def __init__(self):
    self.circle = [0]
    self.value = 0
    self.curr_idx = 0

  def place(self):
    self.value = self.value + 1
    points = 0
    if (self.value % 23) == 0:
      points += 23
      rem_idx = (self.curr_idx - 7) % len(self.circle)
      points += self.circle[rem_idx]
      self.circle = self.circle[0:rem_idx:] + self.circle[(rem_idx+1) % len(self.circle)::]
      self.curr_idx = rem_idx
      #print points
    else:
      ins_idx = (self.curr_idx + 2) % len(self.circle)
      self.circle = self.circle[0:ins_idx:] + [self.value] + self.circle[ins_idx::]
      self.curr_idx = ins_idx 
    return points

  def pretty(self):
    pret = ""
    for i in range(len(self.circle)):
      if i == self.curr_idx:
        pret += " ("+str(self.circle[i])+") "
      else:
        pret += "  "+str(self.circle[i])+"  "
    print pret

 
scores = {}
i = 0
lastscore = 0
players = 424
#players = 9
mc = marblecircle()
#while lastscore != 71144:
for j in range(71144 * 23):
  if j % 100 == 0:
    print j
  lastscore = mc.place()
  #scores[i] += lastscore
  #mc.pretty()
  i = (i + 1) % players
print lastscore
  
    

