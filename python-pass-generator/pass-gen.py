import random
import time
import os
import sys
import argparse
import datetime

wf = open("passgen.log", "a")
chars = 'ABCDEFGHIKJKLMNOPRSTUVXYZabcdefghijklmoprstuvwxyz1234567890#@!#@!'
now = datetime.datetime.now()


parser = argparse.ArgumentParser(description='help for passgen application')
parser.add_argument('-n', '--number', type=int, required=True, help="Количество паролей.")
parser.add_argument('-l', '--lenght', type=int, required=True, help="Количество символов в пароле")
args = parser.parse_args()

show_match_result(args.n, args.l)

#quant = input('number of passwords? ')
#quant = int(quant)
#lenght = input('password(s) lenght? ')
#lenght = int(lenght)
#print(quant, lenght)
#for p in range(quant):
#        password = ''
#        for c in range(lenght):
#                password += random.choice(chars)
#        print(password)
#        wf.write(now.strftime("%Y-%m-%d %H:%M ") + "new passwd is: " + password + "\n")
#wf.close()
#print(args.number)
