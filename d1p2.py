#!/usr/bin/python
import re

i = 0
j = 0
freqs = {0}
offsets = []
found = False
with open("d1p1input.txt", "r") as input:
  for offset in input.read().split('\n'):
    if re.search("[0-9]", offset):
      offsets.append(int(offset))
while not found:
  i += offsets[j]
  print str(i) + " " + str(offsets[j])
  if i in freqs:
    print "found freq " + str(i)
    found = True
  freqs.add(i)
  j = (j + 1) % len(offsets)
  
