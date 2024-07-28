from PIL import ImageTk, Image
import os
import shutil
import tkinter as tk
import webbrowser

from tkinter import (
    NORMAL, DISABLED, WORD, FLAT, END, LEFT,
    X, Y, RIGHT, LEFT, BOTH, CENTER, NONE,
    TOP, SUNKEN, HORIZONTAL, BOTTOM, W,
    VERTICAL, YES, NO, N, E, SE, S, W,
    Text, Toplevel, Menu, Pack, Grid, Tk,
    Place, IntVar, StringVar, Label, Frame,
    filedialog, messagebox, TclError, ttk, scrolledtext
)


TkLabel = Label
from tkinter.ttk import (
    Entry, Button, Label, LabelFrame, Frame, Labelframe,
    Widget, Notebook, Radiobutton, Checkbutton,
    Scrollbar, Progressbar, Separator, Combobox,
    Treeview
)

def selected_tab(event):
    active_tab = event.widget.select()
    tab_name = event.widget.tab(active_tab, "text")

    if tab_name == "Home":
        print("Home is On")
    
    if tab_name == "Encryption":
        print("Encryption is On")

    if tab_name == "Decryption":
        print("Decryption is On")

def encrypt_tab():
    tab_Main.select(tab_Encrypt)

def decrypt_tab():
    tab_Main.select(tab_Decrypt)

def home_tab():
    tab_Main.select(tab_Home)


interface = tk.Tk()
interface.title("Text Encryption Decryption for Free")
height = 580
width = 800
interface.geometry(f"{width}x{height}")
interface.resizable(height=False, width=False)


tab_Main = ttk.Notebook(interface)
tab_Home = ttk.Frame(tab_Main)
tab_Encrypt = ttk.Frame(tab_Main)
tab_Decrypt = ttk.Frame(tab_Main)

#determine tab that is active
tab_Main.bind("<<NotebookTabChanged>>",selected_tab)

tab_Main.add(tab_Home, text="Home")
tab_Main.add(tab_Encrypt, text="Encryption")
tab_Main.add(tab_Decrypt, text="Decryption")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MENU 
menuBar = Menu(interface)
mainMenu = Menu(menuBar, tearoff=0)
mainMenu.add_command(label="Encryption",
                 accelerator="Ctrl+E",
                 command=encrypt_tab,
                 underline=0)

mainMenu.add_command(label="Decryption",
                 accelerator="Ctrl+D",
                 command=decrypt_tab,
                 underline=0)

mainMenu.add_command(label="Home",
                 accelerator="Ctrl+H",
                 command=home_tab,
                 underline=0)

mainMenu.add_command(label="Help",
                     accelerator="Ctrl+K",
                     command=lambda: webbrowser.open("https://github.com/rivful/cs361/blob/main/README.md"),
                     underline=0)

mainMenu.add_separator()

mainMenu.add_command(label="Exit",
                     accelerator="Alt+F4",
                     command=interface.quit)

menuBar.add_cascade(label="Menu",menu=mainMenu)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#HOME
#welcoming message
welcome_message = tk.Label(tab_Home,
                            text = "Welcome to free text encryption/decryption application!",
                            width=40,
                            height=5,
                            font=('Times New Roman',15,'bold'))

welcome_message.place(relx=0.5,
                      rely=0.25,
                      anchor='center')

#introduction
intro_text = "The application provides encryption service and decryption service at no cost to you. Select the buttons below to get started"
intro_message = tk.Label(tab_Home,
                         text=intro_text
                         )
intro_message.place(relx=0.5,
                    rely=0.35,
                    anchor='center')

#buttons to Encrypt or Decrypt
buttonEncryption = tk.Button(tab_Home,
                             text="Encryption",
                             width=14,
                             command=encrypt_tab)
buttonDecryption = tk.Button(tab_Home,
                             text="Decryption",
                             width=14,
                             command=decrypt_tab)
buttonEncryption.place(x=220,
                       y=240)
buttonDecryption.place(x=450,
                       y=240)

#text to readme on github
readMe_text = "If you want to learn more about encryption/decryption and the algorithm used in this application, click the below button to learn more"
readMe_message = tk.Label(tab_Home,
                          text=readMe_text)
readMe_message.place(relx=0.5,
                    rely=0.55,
                    anchor='center')

#link to readme
buttonReadMe = tk.Button(tab_Home,
                         text="ReadMe",
                         width=14,
                         command=lambda: webbrowser.open("https://github.com/rivful/cs361/blob/main/README.md"))
buttonReadMe.place(relx=0.5,
                   rely=0.65,
                   anchor='center')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ENCRYPTION

#seperator between input and output
separator = ttk.Separator(tab_Encrypt,
                          orient='vertical')
separator.place(relx=0.47, rely=0,relwidth=0.2,relheight=1)

#text option
option_text = "Step 1: Select the Symmetric Key Encryption standard"
option_message = tk.Label(tab_Encrypt,
                          text=option_text)
option_message.place(x=8, y=2)



#button for encryption option
check_AESButton = IntVar()
check_TripleButton = IntVar()

AESButton = Checkbutton(tab_Encrypt,
                        text="AES (Advanced Encryption Standard)",
                        variable=check_AESButton,
                        onvalue=1,
                        offvalue=0,
                        width=55)
TripleButton = Checkbutton(tab_Encrypt,
                           text="3DES (Triple Data Encryption Standard)",
                           variable=check_TripleButton,
                           onvalue=1,
                           offvalue=0,
                           width=55)
AESButton.place(x=11,y=22)
TripleButton.place(x=11,y=42)

#text input
input_string = tk.StringVar()
text_input = tk.Label(tab_Encrypt,
                    text="Step 2: Input your text here:")
text_input.place(x=8,y=72)

scroll_text_area = scrolledtext.ScrolledText(tab_Encrypt,
                                             width=42,
                                             height=4,
                                             )
scroll_text_area.place(x=11,y=90)


#button to clear input text
clearTextButton = Button(tab_Encrypt,
                         text="Clear Text",
                         width=20)
clearTextButton.place(x=190,y=170)

#random passphrase
input_key = tk.StringVar()
passPhrase_message = tk.Label(tab_Encrypt,
                              text="Step 3: Enter passphrase")
randomPassPhrase = Radiobutton(tab_Encrypt,
                               text="Generate a random key")
randomPPAES = Radiobutton(tab_Encrypt,
                          text="AES (Advanced Encryption Standard)")
randomAES128 = Radiobutton(tab_Encrypt,
                           text="128 bits")
randomAES192 = Radiobutton(tab_Encrypt,
                           text="192 bits")
randomPP3DES = Radiobutton(tab_Encrypt,
                           text="3DES 128 bits")
ownPassPhrase = Radiobutton(tab_Encrypt,
                            text="Provide your own passphrase:")
passPhrase_inputSpace = Entry(tab_Encrypt,
                        width=50,
                        textvariable=input_key)

passPhrase_message.place(x=8, y=200)
randomPassPhrase.place(x=15, y=220)
randomPPAES.place(x=25, y=240)
randomAES128.place(x=40, y=260)
randomAES192.place(x=40, y=280)
randomPP3DES.place(x=25, y=300)
ownPassPhrase.place(x=15,y=340)
passPhrase_inputSpace.place(x=22,y=370)




#clear pk button
clearPKButton = Button(tab_Encrypt,
                         text="Clear Text",
                         width=20)
clearPKButton.place(x=190,y=400)


#encrypt button
encryptButton = Button(tab_Encrypt,
                       text="ENCRYPT MY TEXT",
                       width=20)
encryptButton.place(x=120,y=450)

#output
output_text = tk.Label(tab_Encrypt,
                       text="View your result here")
output_text.place(x=420,y=2)

output_space = tk.Text(tab_Encrypt,
                       wrap='word',
                       height=10,
                       width=40)
output_space.place(x=420,y=24)
sample_output = "sample output"
output_space.insert(tk.END,sample_output)
output_space.config(state=tk.DISABLED)


#output copy button
output_copyButton = Button(tab_Encrypt,
                           text="Copy result to clipboard",
                           width=25)
output_copyButton.place(x=420,y=200)

#output passkey
output_passkey = tk.Label(tab_Encrypt,
                          text="Random Generated Passkey")
output_passkey.place(x=420, y=230)

output_pk_space= tk.Text(tab_Encrypt,
                       wrap='word',
                       height=5,
                       width=40)
output_pk_space.place(x=420,y=255)
output_pk_space.insert(tk.END,"sample key")
output_pk_space.config(state=tk.DISABLED)

#output copy passkey
output_pk_button=Button(tab_Encrypt,
                        text="Copy passkey to clipboard",
                        width=25)
output_pk_button.place(x=420,y=350)

#encrypt button
closeButton = Button(tab_Encrypt,
                       text="Close Application",
                       width=20,
                       command = interface.destroy)
closeButton.place(x=500,y=450)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DECRYPTION

#text option
option_decryptMessage = tk.Label(tab_Decrypt,
                          text="Step 1: Select the Symmetric Key Decryption standard")
option_decryptMessage.place(x=8, y=2)



#button for decryption option
check_decrypt_AESButton = IntVar()
check_decrypt_TripleButton = IntVar()

AESDecryptButton = Checkbutton(tab_Decrypt,
                        text="AES (Advanced Encryption Standard)",
                        variable=check_decrypt_AESButton,
                        onvalue=1,
                        offvalue=0,
                        width=60)
TripleDecryptButton = Checkbutton(tab_Decrypt,
                           text="3DES (Triple Data Encryption Standard)",
                           variable=check_decrypt_TripleButton,
                           onvalue=1,
                           offvalue=0,
                           width=60)
AESDecryptButton.place(x=11,y=22)
TripleDecryptButton.place(x=11,y=42)

#text input
input_decrypt_string = tk.StringVar()
text_decrypt_input = tk.Label(tab_Decrypt,
                    text="Step 2: Input your text here:")
text_decrypt_inputSpace = Entry(tab_Decrypt,
                        width=50,
                        textvariable=input_decrypt_string)
text_decrypt_input.place(x=8,y=72)
text_decrypt_inputSpace.place(x=11,y=90)

#button to clear input text
clearDecryptedTextButton = Button(tab_Decrypt,
                         text="Clear Text",
                         width=20)
clearDecryptedTextButton.place(x=190,y=120)


#random passphrase
input_decrypt_key = tk.StringVar()
passPhrase_decrypt_message = tk.Label(tab_Decrypt,
                              text="Step 3: Enter passphrase")
passPhrase_decrypt_inputSpace = Entry(tab_Decrypt,
                        width=50,
                        textvariable=input_decrypt_key)

passPhrase_decrypt_message.place(x=8, y=160)
passPhrase_decrypt_inputSpace.place(x=11,y=180)


#button to clear input pk
clearDecryptedPK= Button(tab_Decrypt,
                         text="Clear Text",
                         width=20)
clearDecryptedPK.place(x=190,y=210)

#encrypt button
decryptButton = Button(tab_Decrypt,
                       text="DECRYPT MY TEXT",
                       width=20)
decryptButton.place(x=120,y=260)

#output
output_decrypted_text = tk.Label(tab_Decrypt,
                       text="View your result here")
output_decrypted_text.place(x=420,y=2)

output_decrypted_space = tk.Text(tab_Decrypt,
                       wrap='word',
                       height=10,
                       width=40)
output_decrypted_space.place(x=420,y=26)
output_decrypted_space.insert(tk.END,"sample output")
output_decrypted_space.config(state=tk.DISABLED)


#output copy button
output_decrypted_copyButton = Button(tab_Decrypt,
                           text="Copy result to clipboard",
                           width=25)
output_decrypted_copyButton.place(x=420,y=200)


#encrypt button
closeButtonDecrypt = Button(tab_Decrypt,
                       text="Close Application",
                       width=20,
                       command = interface.destroy)
closeButtonDecrypt.place(x=500,y=260)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tab_Main.pack(expand=1, fill='both')
interface.config(menu=menuBar)
interface.mainloop()
