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
#~ def file_search(lis, fil):
	#~ pat=lis[0]+'/'
	#~ if fil in lis:
		#~ return pat+fil
	#~ elif fil not in lis:
		#~ pat=lis[0]+'/'
		#~ for i in lis:
			#~ if isinstance(i, list):
				#~ recursion=file_search(i, fil)
				#~ if recursion != None:
					#~ pat=pat+recursion
					#~ return(s)

"""
Напишу Вам алгоритм моей программы, а Вы уж сами его адаптируйте под свои нужды.

    Сразу записываю в переменную path=folder[0]+'/'

    Проверяю, есть ли нужный файл в папке ( ну чтобы лишний раз не гонять), и если да, 
    то return path+filename

    Если файла в папке нет, опять записываю в переменную path=folder[0]+'/'. 
    Затем пробегаю по всем элементам в папке. Если какой-то из элементов тоже папка, 
    то результат рекурсивного запроса записываю в переменную res=file_search(element, filename) 
    и сразу же проверяю не пустой ли запрос. Если запрос не пустой, 
    то к пути добавляю результат запроса и возвращаю путьpath=path+res; return path

Все это навеяно изучением вопросов по этой теме здесь в обсуждениях. Кстати, моя прога долго не хотела работать, пока я не добавил return path :)

Надеюсь помог. Удачи!
http://edx.prometheus.org.ua/courses/KPI/Programming101/2015_T1/discussion/forum/89da7e34a21749489846de4da3a7447f/threads/54ec466ff652d84b690000a9
"""
 
#~ def file_search(a, b):
	#~ s=a[0]+"/"
	#~ for i in a:
		#~ if isinstance(i, str):
			#~ if i == b:
				#~ return(i+b)
		#~ elif isinstance(i, list)== True:
			#~ if len(i) > 1:
				#~ recursion=file_search(i, b)
				#~ if s != None:
					#~ s = s + recursion
					#~ return(s)
#~ def file_search(folder, filename):
    #~ if isinstance(folder, list):
        #~ path = ''
        #~ for item in folder:
            #~ if isinstance(item, list):
                #~ if filename in item:
                    #~ path = folder[0] + '/' + filename
                #~ else: print 'False'
            #~ else: file_search(item, path)
        #~ print path
        #~ return path
    #~ else:
        #~ path = folder + '/' + filename
        #~ return path

print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')

#~ def file_search(a, b):
	#~ s=a[0]+"/"
	#~ if b in a:
		#~ return(s+b)
	#~ if len(a) > 1:
		#~ for i in a:
			#~ if isinstance(i, list):
				#~ recursion = file_search(i, b)
				#~ if recursion != None:
					#~ s = s + recursion
					#~ return(s)


#~ s=a[0]+'/'
