"""
Author: Mostafa Ramadan 
Start Date: 20th August 10:30 PM
"""
from playfair import PlayFair
from rsa import RSA
from des import SDES
from rc4 import RC4
from diffie import DiffieHellman
from tkinter import *
import time

class Window():
    
    """
    This Class Represents a Tkinter Window
    """
   

    def __init__(self,title="CS401 Project",dimensions="640x480",\
                            bg="white"):
       
        self.text_widgets=list()
        self.radio_buttons = list()
        
        self._window = Tk()
        self._window.configure(background=bg)
        self._window.title(title)

        self._window.geometry(dimensions)

        self.add_button(color="green",text="Encrypt",x=10,y=150,\
                         binding=self.encrypt)

        self.add_button(color="red",text="Decrypt",x=340,y=150,\
                         binding=self.decrypt)

        ## radio button variable        
        self.r_var = IntVar(self._window)
        self.r_var.set(0)
        self.add_radiobutton(x=450,y=25,text="play Fair")

        self.add_radiobutton(x=450,y=50,text="SDES")

        self.add_radiobutton(x=450,y=75,text="RC4")

        self.add_radiobutton(x=450,y=100,text="RSA")

        self.add_radiobutton(x=450,y=125,text="Diffie-Hellman")

        ### Message
        self.add_text()
        ### Key
        self.add_text(x=450,y=150,width=18,height=1)
       
        


    def start(self)-> None:
        """ Starts the window Loop """
        self._window.mainloop()
    
    def add_button(self,color="gray",binding=None,text="button",x=0,y=0):

        button = Button(self._window,text=text,command=lambda:binding())
        button.configure(background=color)
        button.pack()

        button.place(x=x,y=y)

    def add_text(self,color="#edebe6",x=10,y=25,height=6,width=50):

        text_widget = Text(self._window,height=height,width=width)
        text_widget.configure(background=color)
        text_widget.pack()

        text_widget.place(x=x,y=y)
        self.text_widgets.append(text_widget)

    def add_radiobutton(self,x=10,y=25,text="r_button"):

        r_button = Radiobutton(self._window,text=text,padx=20,\
                                value=len(self.radio_buttons),width=10\
                                ,variable=self.r_var)

        r_button.pack()
        r_button.place(x=x,y=y)

        self.radio_buttons.append(r_button)

    def encrypt(self):
        text = self.text_widgets[0].get(1.0,"end")
        key  = self.text_widgets[1].get(1.0,"end")
        cipher_text = ""
        if self.r_var.get() ==   0:
            cipher_text = PlayFair.encrypt(text,key)

        elif self.r_var.get() == 1:
            cipher_text = SDES.encrypt(text,key)
            
        elif self.r_var.get() == 2:

            text = text.strip()
            text = [int(value) for value in text.split(",")]

            key = key.strip()
            key = [int(value) for value in key.split(",")]

            cipher_text = str(RC4.encrypt(text,key))
            
        elif self.r_var.get() == 3:
            text = int(text.strip())
            params = [int(value) for value in key.split(" ")]

            cipher_text = RSA.encrypt(M=text,p=params[0],q=params[1],\
                e=params[2])

        elif self.r_var.get() == 4:
            private_a, private_b = text.split(" ")
            a , q = key.split(" ")

            private_a, private_b = int(private_a), int(private_b)
            a, q = int(a), int(q)

            ## unpacking result ##
            public_a,public_b,\
            shared_a,shared_b=DiffieHellman.calculate(a,q,private_a,private_b)
            #################
            cipher_text = "public keyA is "+str(public_a)+\
                          " public keyB is "+str(public_b)+\
                          " Shared A and B are the same and is  "+str(shared_a)

        self.text_widgets[0].delete(1.0,"end")
        self.text_widgets[0].insert(1.0,cipher_text)

    def decrypt(self):
        text = self.text_widgets[0].get(1.0,"end")
        key  = self.text_widgets[1].get(1.0,"end")
        cipher_text = ""
        if self.r_var.get() == 0:
            cipher_text = PlayFair.decrypt(text,key)
        elif self.r_var.get() == 1:
            cipher_text = SDES.encrypt(text,key)
        elif self.r_var.get() == 2:
            cipher_text = RC4.encrypt(text,key)
        elif self.r_var.get() == 3:
            text = int(text.strip())
            params = [int(value) for value in key.split(" ")]

            cipher_text = RSA.encrypt(C=text,p=params[0],q=params[1],\
                e=params[2])

        self.text_widgets[0].delete(1.0,"end")
        self.text_widgets[0].insert(1.0,cipher_text)


if __name__ == "__main__":
    window = Window()
    window.start()