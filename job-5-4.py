#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити функцію file_search(folder, filename), 
яка приймає 2 аргументи -- список folder та рядок filename, 
та повертає рядок -- повний шлях до файлу або папки filename в структурі folder.

Файлова структура folder задається наступним чином: 

Список -- це папка з файлами, його 0-й елемент містить назву папки, 
а всі інші можуть представляти або файли в цій папці (1 файл = 1 рядок-елемент списку), 
або вкладені папки, які так само представляються списками. Як і в файловій системі вашого комп'ютера, 
шлях до файлу складається з імен всіх папок, в яких він міститься, 
в порядку вкладеності (починаючи з зовнішньої і до папки, в якій безпосередньо знаходиться файл), 
розділених "/". 

Вважати, що імена всіх файлів є унікальними. Повернути логічне значення False, якщо файл не знайдено.

Виклик функції: file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
Повертає: 'C:/ideas.txt'

Виклик функції: file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
Повертає: False

Виклик функції: file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
Повертає: '/home/user2/desktop/new folder/hereiam.py'
"""
#~ 
def file_search(a, b):
	if isinstance(a, list):
		for i in a:
			if i == b:
				return(a[0]+"/"+i)
			elif isinstance(i, list):
				file_search(i, b)
	#~ elif b not in a:
		#~ return (a[0]+"/"+file_search(a, b))


#~ s=a[0]+'/'
print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
