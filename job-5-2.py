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

a=int(sys.argv[1])
b=int(sys.argv[2])

def clean_list(l):
	output_list=[]
	for i in l:
		if i not in output_list:
			output_list.append(i)
	return(output_list)

def counter(x, y):
	x=str(x); y=str(y); con = 0
	for i in clean_list(y):
		if i in clean_list(x):
			con+=1
	return(con)

print counter(a, b)

