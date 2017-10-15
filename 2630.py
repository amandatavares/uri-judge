# -*- coding: utf-8 -*-

# Last submission: Still 100% wrong answer
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
    P = int(min(rgb))
  if(conv == "max"):
    P = int(max(rgb))
  print("Caso #%d: %d" % (i,P)) 


  
# Second submission

# T = int(input(""))
# Ps = []
# for i in range(T):
#   conv = input("")
#   rgb = input("").split()
#   r = int(rgb[0])
#   g = int(rgb[1])
#   b = int(rgb[2])
#   if(conv == "eye"):
#     res = int((0.30*r)+(0.59*g)+(0.11*b))
#   if(conv == "mean"):
#     res = int((r+g+b)/3)
#   if(conv == "min"):
#     res = int(min(rgb))
#   if(conv == "max"):
#     res = int(max(rgb))
#   Ps.append(res)
  
# for x in range(T):
#   P = Ps[x]
#   print("Caso #%d: %d" % (x,P))



# First submission
# T = int(input(""))
# Ps = []
# for i in range(T):
#   conv = input("")
#   rgb = input("").split()
#   r = int(rgb[0])
#   g = int(rgb[1])
#   b = int(rgb[2])
#   if(conv == "eye"):
#     P = int((0.30*r)+(0.59*g)+(0.11*b))
#   if(conv == "mean"):
#     P = int((r+g+b)/3)
#   if(conv == "min"):
#     P = int(min(rgb))
#   if(conv == "max"):
#     P = int(max(rgb))
#   Ps.append(P)
  
# for x in range(T):
#   print("Caso #%d: %d" % (x,Ps[x]))
#   