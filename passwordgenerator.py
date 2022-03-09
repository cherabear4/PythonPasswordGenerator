from distutils import text_file
import os.path
import pathlib
import os
import uuid
import hashlib
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

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

#Things Done

#1. Password Generator
#2. UI Generator
#3. Hashing
#4. Write To File

#=======================================================================================================================

#Things to do

#1. Add a master password to the passwords.txt file
#2. Length of password
#3. Need to Have . in the website name
#4. Fix Multiple Lines Issue In the passwords.txt file

#=======================================================================================================================








password = uuid.uuid1()

#def gen_password():
#    website = input("Enter the website: ")
#    if website == "":
#        print("Please enter a website")
#        gen_password()
#    else:
#        with open('passwords.txt', 'w') as f:
#            #store as plain text
#            f.write(website + ": " + str(password))
#            #store as hashed
#            hash_object = hashlib.sha256(str(password).encode())
#            hex_dig = hash_object.hexdigest()
#            f.write('\nHashed Password: ' + hex_dig)





#=======================================================================================================================
#Kivy App
class PasswordGenerator(App):
    def build(self):
#=======================================================================================================================
#=======================================================================================================================
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.4, 0.4)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        self.background_normal = '#00ff00'

        # label widget
        self.greeting = Label(
                        text= "Enter The Name of The Website",
                        font_size= 18,
                        color= '#ffffff'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "Save Password",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#7ddb96',
                      #remove darker overlay of background colour
                      background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def password_creation():
        with open('passwords.txt', 'w') as f:
            #store as plain text
            f.write(website + ": " + str(password))
            #store as hashed
            hash_object = hashlib.sha256(str(password).encode())
            hex_dig = hash_object.hexdigest()
            f.write('\nHashed Password: ' + hex_dig)

    def callback(self, instance):
        print("callback")
        website = self.user.text
        if website == "":
            print("Please enter a website")
            self.callback()
        else:
            with open('passwords.txt', 'w') as f:
                #store as plain text
                f.write(website + ": " + str(password))
                #store as hashed
                hash_object = hashlib.sha256(str(password).encode())
                hex_dig = hash_object.hexdigest()
                f.write('\nHashed Password: ' + hex_dig)

#=======================================================================================================================


if __name__ == "__main__":
    me()
    PasswordGenerator().run()
    #gen_password()