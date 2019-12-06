# First simple command:
# python -c 'import crypt; print(crypt.crypt("test", crypt.mksalt(crypt.METHOD_SHA512)))'
# 
# TODO: modify to linux-like.

import hashlib
import crypt

password = input("password: ")
print("md5: " + hashlib.md5(f'{password}'.encode('utf-8')).hexdigest())
print("sha512: " + crypt.crypt(f'{password}', crypt.mksalt(crypt.METHOD_SHA512)))
