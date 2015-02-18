#!/usr/bin/env python
# -*- coding: utf-8 -*-

s="qwERqTYqwR lblbDUDT KJVBHljbb KJBH lkjbnj"

z=0
l=[]
#~ while z < len(s):
	#~ l.append(s[z:z+5])
	#~ z+=5
#~ for i in l:
	#~ if len(i) < 5:
		#~ del l[l.index(i)]

for i in s:
	if i == " ":
		s=s.replace(i, '')
	elif i.islower() == True:
		s=s.replace(i, "a")
	elif i.isupper() == True:
		s=s.replace(i, "b")

for i in s:
	if i.isupper() == True:
		s=s.replace(i, "b")
print s
