#!/usr/bin/env python
# -*- coding: utf-8 -*-

s="Hot sUn BEATIng dOWN bURNINg mY FEet JuSt WalKIng arOUnD HOt suN mAkiNG me SWeat"

z=0
l=[]



for i in s:
	if i == " ":
		s=s.replace(i, '')
	elif i.islower() == True:
		s=s.replace(i, "a")

for i in s:
	if i.isupper() == True:
		s=s.replace(i, "b")
print s

while z < len(s):
	l.append(s[z:z+5])
	z+=5
	for i in l:
		if len(i) < 5:
			del l[l.index(i)]


l_key={'a':"aaaaa", 'b':"aabbb", 'c':"aaabb", 'd':"aaaab", 'e':"abbbb", 'f':"", 'g':"", 'h':"", 'i':"bbabb", 'j':"", 'k':"abbba", 'l':"bbbaa", 
'm':"", 'n':"", 'o':"", 'p':"", 'q':"", 'r':"", 's':"", 't':"", 'u':"", 'v':"", 'w':"", 'x':"", 'y':"", 'z':""]

