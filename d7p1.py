#!/usr/bin/python

class Step(object):
  def __init__(self, name):
    self.name = name
    self.allows = []
    self.requires = []
    self.depth = 0

  def allow(self, step):
    self.allows.append(step)

  def require(self, step):
    self.requires.append(step)

  def satisfied(self, done):
    return set(self.requires).issubset(set(done))
 
  def pretty(self):
    prepend = ""
    for i in range(self.depth):
      prepend += "  "
    print prepend +"Step " + self.name 
    print prepend +"Allows: " + ",".join(self.allows)
    print prepend +"Requires: " + ",".join(self.requires)

steps = {}
with open("d7p1input_sorted.txt", "r") as input:
  for line in input.read().strip().split('\n'):
    fields = line.split()
    name = fields[1]
    allows = fields[7]
    if name not in steps.keys():
      steps[name] = Step(name)
    steps[name].allow(allows)
    if allows not in steps.keys():
      steps[allows] = Step(allows)
    steps[allows].require(name)

order = []

def ordermaker():
  if len(order) == len(steps.keys()):
    return
  for step in sorted(steps.keys()):
    if step not in order: 
      if steps[step].satisfied(order):
        order.append(step)
        ordermaker()
    
ordermaker()
    
print "".join(order)

