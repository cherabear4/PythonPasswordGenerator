from distutils import text_file
import os.path
import pathlib
import os
import uuid
import hashlib

#=======================================================================================================================

def me():
     print("""______          _    _               __                  _        _     _      _                       
| ___ \        | |  | |             / /                 | |      | |   | |    | |                      
| |_/ /_   _   | |_ | |___   __    / /    ___  ___ _   _| |_ __ _| |__ | | ___| |_ _   _ ___  ___ _ __ 
| ___ \ | | |  | __|| __\ \ / /   / /    / _ \/ __| | | | __/ _` | '_ \| |/ _ \ __| | | / __|/ _ \ '__|
| |_/ / |_| |  | |_ | |_ \ V /   / /    | (_) \__ \ |_| | || (_| | |_) | |  __/ |_| |_| \__ \  __/ |   
\____/ \__, |   \__(_)__| \_/   /_/      \___/|___/\__,_|\__\__,_|_.__/|_|\___|\__|\__,_|___/\___|_|   
        __/ |                                                                                          
       |___/   """)

me()

#=======================================================================================================================

#using a uuid as a password, it works fine, at least for now

#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/23728630#23728630

#https://www.security.org/how-secure-is-my-password/ random uuid tested with security.org , average is 50 nonillion years

#https://www.pythontutorial.net/python-basics/python-check-if-file-exists/ , check if file exists

#future: password length (not hard), fix problem where it doesn't work if you enter a website without a ".", fix passwords.txt not being able to have multiple websites/passwords

#=======================================================================================================================

#password created with uuid, gets hashed, i also let there be some plain text in the passwords .txt because why not, eventaully i will remove it and add a function where you need a master password to access the passwords.txt file

#really simple

#feel free to rate my code, i would appreciate it if you would leave a star on my github page <3

#=======================================================================================================================

password = uuid.uuid1()

def gen_password():
    website = input("Enter the website: ")
    if website == "":
        print("Please enter a website")
        gen_password()
    else:
        with open('passwords.txt', 'w') as f:
            #store as plain text
            f.write(website + ": " + str(password))
            #store as hashed
            hash_object = hashlib.sha256(str(password).encode())
            hex_dig = hash_object.hexdigest()
            f.write('\nHashed Password: ' + hex_dig)

gen_password()