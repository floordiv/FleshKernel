# import threading
# from time import sleep
#
#
# def first_thread():
#     while True:
#         print('I am first thread!')
#         sleep(2)
#
#
# def second_thread(a):
#     while True:
#         print(f'I am second thread: {a}')
#         sleep(2)
#
#
# class third:
#
#     def third_thread(self):
#         print('I\'m third thread...')
#         sleep(1.5)
#
#     third_thread(0)
#
#
# thread1 = threading.Thread(target=first_thread)
# thread2 = threading.Thread(target=second_thread, args=['rgrg'])
# thread3 = threading.Thread(target=third)
#
# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()

# import random


# for element in range(int(input('Len of the password: '))):
#     print(random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
import os

folder = []

for element in os.walk('/home/floordiv/py/flesh_kernel/system'):
    folder.append(element)

print(folder)

print('-' * 50)

for address, dirs, files in folder:
    for file in files:
        print(address+'/'+file)

