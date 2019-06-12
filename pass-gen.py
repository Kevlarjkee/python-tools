#!/bin/python3.6

import random
import logging
import time
import os
import sys

#file_1 = open('example.log','a',)


chars = 'ABCDEFGHIKJKLMNOPRSTUVXYZabcdefghijklmoprstuvwxyz1234567890#@#@'

quant = input('number of passwords? ')
quant = int(quant)
lenght = input('password(s) lenght? ')
lenght = int(lenght)

for p in range(quant):
        password = ''
        for c in range(lenght):
                password += random.choice(chars)
        print(password)

#file_1.write(password)

#file_1.close()
