#!/usr/bin/python
import re

i = 0
with open("d1p1input.txt", "r") as input:
  for offset in input.read().split('\n'):
    if re.search("[0-9]", offset):
      i += int(offset)
print str(i)
