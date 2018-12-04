#!/usr/bin/python
import re

twofers = 0
threefers = 0
i = 1
with open("d2p1input.txt", "r") as input:
  for id in input.read().split('\n'):
    i += 1
    cs = {}
    for c in id: 
      if c in cs.keys():
        cs[c] += 1
      else:
        cs[c] = 1
    fer2 = False
    fer3 = False
    for pairs in cs:
      if cs[pairs] == 2:
        fer2 = True
      if cs[pairs] == 3:
        fer3 = True
    if fer2:
      twofers += 1
    if fer3:
      threefers += 1
    
print twofers * threefers
