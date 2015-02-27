#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити функцію find_most_frequent(text),
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, 
пробіли та розділові знаки (,.:;!?-);
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). 
Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") 
важаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" 
вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.

Наприклад
Виклик функції: find_most_frequent('Hello,Hello, my dear!')
Повертає: ['hello']
Виклик функції: find_most_frequent('to understand recursion you need first to understand recursion...')
Повертає: ['recursion', 'to', 'understand']
Виклик функції: find_most_frequent('Mom! Mom! Are you sleeping?!!!')
Повертає: ['mom']

"""
def find_most_frequent(s):
	l=''
	for i in s:
		if i.isalnum() != True:
			l=l+" "
		else: l=l+i
	l=l.split()
	return l


print find_most_frequent('Hello,Hello, my dear!')
print find_most_frequent('to understand recursion you need first to understand recursion...')
print find_most_frequent('Mom! Mom! Are you sleeping?!!!')
