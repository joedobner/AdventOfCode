#!/usr/bin/python

class marble(object):
  def __init__(self, val, nextval, prevval):
    self.value = val
    self.nextval = nextval
    self.prevval = prevval

class marblecircle(object):
  def __init__(self):
    self.marble = marble(0, None, None)
    self.marble.prevval = self.marble
    self.marble.nextval = self.marble

  def place(self, value):
    score = 0
    if value % 23 == 0:
      score += value
      for q in range(7):
        self.marble = self.marble.prevval
      score += self.marble.value
      self.marble.prevval.nextval = self.marble.nextval
      self.marble.nextval.prevval = self.marble.prevval
      self.marble = self.marble.nextval
    else:
      pm = marble(value, self.marble.nextval.nextval, self.marble.nextval)
      self.marble.nextval.nextval.prevval = pm
      self.marble.nextval.nextval = pm
      self.marble = pm
    return score
  
  def pretty(self):
    m = self.marble
    tval =  self.marble.value
    pret = "0 "
    while m.value != 0:
      m = m.nextval
    while m.nextval.value != 0:
      m = m.nextval
      if m.value == tval:
        pret += "("+str(m.value)+")"
      else:
        pret += " "+str(m.value)+" "
    while m.value != tval:
      m = m.nextval
    return pret

 
scores = {}
i = 0
j = 0
lastscore = 0
players = 424
#players = 9
mc = marblecircle()
for j in range(71144):
  j += 1
  lastscore = mc.place(j)
  if i not in scores.keys():
    scores[i] = 0
  scores[i] += lastscore
  print mc.pretty()
  i = (i + 1) % players
topscore = 0
for e in scores.keys():
  if scores[e] > topscore:
    topscore = scores[e]
print topscore

  
    

