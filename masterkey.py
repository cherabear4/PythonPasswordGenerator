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


#Kivy App
class MasterKey(App):
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
                        text= "Enter Your MasterKey Password (REMEMBER IT, this does not save it as plain text)",
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

    def callback(self, instance):
        print("callback")
        master = self.user.text
        with open('masterkey.txt', 'w') as f:
            #store as hashed
            hash_object = hashlib.md5(str(master).encode())
            hex_dig = hash_object.hexdigest()
            f.write(hex_dig)

#=======================================================================================================================


if __name__ == "__main__":
    me()
    MasterKey().run()
    #gen_password()