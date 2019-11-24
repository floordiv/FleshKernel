import os
import textwrap
import decimal

symbols = list(' \nqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,./?;:\'"[]{}-_=+()1234567890~!@#$%^&*')
numbers = [x + 100 for x in range(len(symbols))]
code = dict(zip(symbols, numbers))
decode = dict(map(reversed, code.items()))

finished = False
while not finished:
    # filename = input('File to compress> ')
    filename = 'hello'
    temp = ''
    if filename in ['quit', 'exit']:
        finished = False
        break
    if os.path.exists(filename):
        with open(filename, 'r') as content:
            content = content.read()

        for each in content:
            temp += str(code[each])
        # print(temp)
        result = decimal.Decimal(int(temp) / 15250)
        print(result)

        # print(int(decimal.Decimal(result * 15250)), True)
        # print(int(complex(int(temp)) / 15250))

        content = textwrap.wrap(temp, 3)
        # print(content)
        for each in textwrap.wrap(temp, 3):
            print(decode[int(each)], end='')
        input()
