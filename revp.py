#!/usr/bin/python
import sys
stack=[]

for e in sys.argv[1:]:
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

print(stack.pop())
