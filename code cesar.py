from tkinter import *

from tkinter import messagebox

import os.path


###CODE PYTHON###

####FONCTIONS DE CRYPTAGE CODE CESAR####
def split(word):
    return [char for char in word]

def verif(num_char):
    if num_char>90 :
        num_char = num_char-26
    return num_char

def Crypto_Cesar(word_clair, cle_cesar):
    word_clair = word_clair.upper()
    tab_char = split(word_clair)
    tab_num = [ord(char) for char in tab_char]
    tab_crypto = [chr(verif(num + cle_cesar)) for num in tab_num]
    return ''.join(tab_crypto)

def read_file(file_in, cle_cesar):
    if not os.path.isfile(file_in):
        print('File does not exist.')
    else:
        with open(filename) as f:
            content = f.read().splitlines()
    file = ['']
    cpt = 0
    for line in content:
        file[cpt] = Crypto_Cesar(line, cle_cesar)
        cpt += 1
    return file
##########################

###FONCTION PRINCIPALE###



def cesarCode():

    
    ###Gestion des erreurs de saisie###
    if (message.get() == ""):
        messagebox.showerror(title="Erreur", message="Veuillez saisir un message à crypter !")
        return
    elif (cle.get() == ""):
        messagebox.showerror(title="Erreur", message="Veuillez saisir une clé de cryptage !")
        return

    try:
        int(cle.get())
    except ValueError:
        messagebox.showerror(title="Erreur", message="La clé doit être un chiffre !")
        return
    ####################################

    messageSasie = message.get() ###Variable contenant la saisie du message depuis l'interface
    cleSaisie = int(cle.get()) ###Variable contenant la saisie de la clé depuis l'interface
    
    CryptedMessage = Crypto_Cesar(messageSasie, cleSaisie) ###Variable qui contient le message une fois crypté
    
    
    
    
    resultText.set("Code crypté : "+CryptedMessage)
    

    

##########################

###INTERFACE###

window=Tk()
window.geometry("500x400")
window.title("Code césar")
window.resizable(False, False)

message = StringVar()
cle = StringVar()
resultText = StringVar()

label1=Label(window,text="Cryptage d'un message en code césar",fg="blue",font=("arial",16,"bold")).place(x=50,y=50)

labelMsg = Label(window,text="Message à crypter :",font=("arial",12)).place(x=100,y=107)
textBoxMsg = Entry(window, width=20, textvariable = message).place(x=260, y=110)


labelCle = Label(window,text="Clé de crytpage :",font=("arial",12)).place(x=119,y=147)
textBoxCle = Entry(window, width=20, textvariable = cle).place(x=260, y=150)

labelResult = Label(window,text="", fg = "green", font=("arial",12), textvariable=resultText)
labelResult.config(anchor=CENTER)
labelResult.pack(pady=180)

bouton1=Button(window,text="Valider",relief=RAISED,font=("arial",12,"bold"),command=cesarCode)
bouton1.config(anchor=CENTER)
bouton1.place(x=215, y=250)





window.mainloop()

#################
