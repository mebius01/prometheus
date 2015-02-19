#!/usr/bin/env python
# -*- coding: utf-8 -*-

s="wELcO MeToT heHOt ELcaL iFORN IaSUc HALoV eLYPL aCEsu cHaLO vely"

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

print l

dic={"aaaaa":'a', "aaaab":'b', "aaabb":'c', 
	"aabbb":'d', "abbbb":'e', "bbbbb":'f', 
	"bbbba":'g', "bbbaa":'h', "bbabb":'i', 
	"babbb":'j', "abbba":'k', "bbbaa":'l', 
	"bbaab":'m', "baabb":'n', "aabba":'o', 
	"abbab":'p', "bbaba":'q', "babab":'r', 
	"ababb":'s', "babba":'t', "abbaa":'u', 
	"bbaaa":'v', "baaab":'w', "aaaba":'x', 
	"aabab":'y', "ababa":'z'}

for i in dic.keys():
	for a in l:
		if i == a:
			print dic.get(i)
"""
dic={'a':"aaaaa", 'b':"aaaab", 'c':"aaabb", 
	'd':"aabbb", 'e':"abbbb", 'f':"bbbbb", 
	'g':"bbbba", 'h':"bbbaa", 'i':"bbabb", 
	'j':"babbb", 'k':"abbba", 'l':"bbbaa", 
	'm':"bbaab", 'n':"baabb", 'o':"aabba", 
	'p':"abbab", 'q':"bbaba", 'r':"babab", 
	's':"ababb", 't':"babba", 'u':"abbaa", 
	'v':"bbaaa", 'w':"baaab", 'x':"aaaba", 
	'y':"aabab", 'z':"ababa"}
"""
