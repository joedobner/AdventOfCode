#!/usr/bin/python
import re

tags = set()
length = 26
with open("d2p1input.txt", "r") as input:
  for id in input.read().split('\n'):
    if re.search("[a-z]", id):
      tags.add(id)

for i in range(length):
  barrier = {}
  for tag in tags:
    subkey = tag[:i:] + tag[i+1::]
    if subkey in barrier.keys():
      print subkey
    else:
      barrier[subkey] = ""
