#!/usr/bin/python

class Node(object):
  def __init__(self, kidcount, mdcount):
    self.kidcount = int(kidcount)
    self.mdcount = int(mdcount)
    self.kids = []
    self.metadata = []

  def mdsum(self):
    sum = 0
    for m in self.metadata:
      sum += m
    for k in self.kids:
      sum += k.mdsum()
    return sum

def nodemaker():
  kc = int(digits.pop(0))
  md = int(digits.pop(0))
  n = Node(kc, md)
  i = 0
  for i in range(n.kidcount):
    n.kids.append(nodemaker())
  for i in range(md):
    n.metadata.append(int(digits.pop(0)))
  return n

with open("d8p1input.txt", "r") as input:
  digits = input.read().strip().split(' ')
  root = nodemaker()
  print root.mdsum()
  
    

