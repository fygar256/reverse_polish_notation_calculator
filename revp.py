#!/usr/bin/python3
import sys
stack=[]
s=sys.argv[1:]

while(s):
  e=s[0]
  if (e=='+'):
    stack.append(stack.pop()+stack.pop())
  elif (e=='-'):
    a=stack.pop()
    stack.append(stack.pop()-a)
  elif (e=='*'):
    stack.append(stack.pop()*stack.pop())
  elif (e=='/'):
    a=stack.pop()
    stack.append(stack.pop()/a)
  else:
    stack.append(float(e))
  s=s[1:]

print(stack.pop())
