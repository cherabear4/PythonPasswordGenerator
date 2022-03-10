import hashlib
import sys

text_file = open("password.txt", "r")
lines = text_file.readline()
text_file.close()

password = lines

def check():
    verify = input('Input MasterPass: ')
    if hashlib.md5(verify.encode()).hexdigest() == password:
        print('Correct')


while True:
    check()
    sys.exit()