# -*- coding: utf-8 -*-

T = int(input(""))

for i in range(T):
  conv = input("")
  rgb = input("").split()
  r = int(rgb[0])
  g = int(rgb[1])
  b = int(rgb[2])
  if(conv == "eye"):
    P = int((0.30*r)+(0.59*g)+(0.11*b))
  if(conv == "mean"):
    P = int((r+g+b)/3)
  if(conv == "min"):
    P = int(min(r,g,b))
  if(conv == "max"):
    P = int(max(r,g,b))
  print("Caso #%d: %d" % (i+1,P)) 