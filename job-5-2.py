#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити функцію counter(a, b), 
 яка приймає 2 аргументи -- цілі невід'ємні числа a та b, 
 та повертає число -- кількість різних цифр числа b, які містяться у числі а.

Наприклад
 Виклик функції: counter(12345, 567)
 Повертає: 1
 Виклик функції: counter(1233211, 12128)
 Повертає: 2
 Виклик функції: counter(123, 45)
 Повертає: 0
 """
 
import sys

a=sys.argv[1]
b=sys.argv[2]
def counter(x, y):
	def clean_list(l):
		output_list=[]
		for i in l:
			if i not in output_list:
				output_list.append(i)
		return(output_list)
	def lis_for(x):
		l=[]
		for i in x:
			l.append(i)
		return(l)
	con = 0
	for i in clean_list(y):
		if i in clean_list(x):
			con+=1
	print(con)
counter(a, b)

