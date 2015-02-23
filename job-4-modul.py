#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
string_input=sys.argv[1]
string_output=''
z=0
l=[]
dic={"aaaaa":'a', "aaaab":'b', "aaabb":'c', 
	"aabbb":'d', "abbbb":'e', "bbbbb":'f', 
	"bbbba":'g', "bbbab":'h', "bbabb":'i', 
	"babbb":'j', "abbba":'k', "bbbaa":'l', 
	"bbaab":'m', "baabb":'n', "aabba":'o', 
	"abbab":'p', "bbaba":'q', "babab":'r', 
	"ababb":'s', "babba":'t', "abbaa":'u', 
	"bbaaa":'v', "baaab":'w', "aaaba":'x', 
	"aabab":'y', "ababa":'z'}

for i in string_input:
	if i == " ":
		string_input=string_input.replace(i, '')
	elif i.islower() == True:
		string_input=string_input.replace(i, "a")

for i in string_input:
	if i.isupper() == True:
		string_input=string_input.replace(i, "b")

while z < len(string_input):
	l.append(string_input[z:z+5])
	z+=5
	for i in l:
		if len(i) < 5:
			del l[l.index(i)]

for a in l:
	for i in dic.keys():
		if i == a:
			string_output=string_output + dic.get(i)

print(string_output)

"""
dic={'a':"aaaaa", 'b':"aaaab", 'c':"aaabb", 
	'd':"aabbb", 'e':"abbbb", 'f':"bbbbb", 
	'g':"bbbba", 'h':"bbbab", 'i':"bbabb", 
	'j':"babbb", 'k':"abbba", 'l':"bbbaa", 
	'm':"bbaab", 'n':"baabb", 'o':"aabba", 
	'p':"abbab", 'q':"bbaba", 'r':"babab", 
	's':"ababb", 't':"babba", 'u':"abbaa", 
	'v':"bbaaa", 'w':"baaab", 'x':"aaaba", 
	'y':"aabab", 'z':"ababa"}
"""
