#!/usr/bin/python
import re

class Guard(object):
  def __init__(self, name):
    self.name = name
    self.shifts = []

  def addShift(self):
    self.shifts.append(Shift())

  def sleepiness_ratio(self):
    onduty = 0
    asleep = 0
    for s in self.shifts:
      onduty += 60 
      asleep += s.asleepminutes()
    return float(asleep) / float(onduty)

  def sleepiness(self):
    asleep = 0
    for s in self.shifts:
      asleep += s.asleepminutes()
    return asleep

  def sleepiestMinute(self):
    max = 0
    minute = 0
    for i in range(60):
      asleep = 0
      for s in self.shifts:
        if s.status[i] == 'S':
          asleep += 1
      if asleep > max:
        max =  asleep
        minute = i
    return minute, max;
 
class Shift(object):
  def __init__(self):
    self.status = []
    self.wakestatus = 'W'
    self.pos = 0

  def addState(self, line):
    fields = line.split()
    for i in range(self.pos, int(fields[2])):
      self.status.append(self.wakestatus)
    if fields[3] == "falls":
      self.wakestatus = 'S'
    if fields[3] == "wakes":
      self.wakestatus = 'W'
    self.pos = int(fields[2])

  def finalizeShift(self):
    for i in range(self.pos, 60):
      self.status.append(self.wakestatus)
    self.pos = 60
    
  def awakeminutes(self):
    m = 0
    for s in self.status:
      if s == 'W':
        m += 1
    return m
      
  def asleepminutes(self):
    m = 0
    for s in self.status:
      if s == 'S':
        m += 1
    return m

  def pretty(self):
    o = ""
    for s in self.status:
      o += s
    return o
    

guards = {}
current_guard = False
with open("d4p1input_sorted.txt", "r") as input:
  for line in input.read().split('\n'):
    fields = line.split()
    if len(fields) > 2:
      if fields[3] == "Guard":
        if current_guard:
          guards[current_guard].shifts[-1].finalizeShift()
        if fields[4] not in guards.keys():
          guards[fields[4]] = Guard(fields[4])
        current_guard = fields[4]
        guards[current_guard].addShift()
      else:
        guards[current_guard].shifts[-1].addState(line)
guards[current_guard].shifts[-1].finalizeShift()

for guard in guards.keys():
  minute, asleep = guards[guard].sleepiestMinute()
  print guard + " " + str(guards[guard].sleepiness()) + " " + str(minute) + " " + str(asleep)
#  for shift in guards[guard].shifts:
#    print shift.pretty()

