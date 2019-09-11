# a = 'hello world'
# lol = 'test'
# b = 20 / 10
# print(a, lol, b)
#
# printer()
import os
os.system('clear')

sentences = []

try:
    while True:
        sentences.append(input(': '))
except KeyboardInterrupt:
    print('\n', sentences)

while True:
    for element in sentences:
        input(element)
    os.system('clear')
