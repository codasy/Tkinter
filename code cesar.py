from tkinter import *
from tkinter import filedialog
import os, os.path
from tkinter import messagebox



###CODE PYTHON###

###FONCTION D'OUVERTURE D'UN FICHIER TXT###
reps=os.getcwd()
fics=""
    
def ouvrir(whichWindow):
    repfic = filedialog.askopenfilename(title="Ouvrir le fichier:", initialdir=reps, \
        initialfile=fics, filetypes = [("All", "*"),("Fichiers texte","*.txt")]) 
    if len(repfic) > 0:
        rep=os.path.dirname(repfic)
        fic=os.path.basename(repfic)
    if whichWindow == "crypt":
        textBoxMsgTxtCrypt.config(state='normal')
        textBoxMsgTxtCrypt.insert(0, repfic)
        textBoxMsgTxtCrypt.config(state='disabled')
    elif whichWindow == "decrypt":
        textBoxMsgTxtDecrypt.config(state='normal')
        textBoxMsgTxtDecrypt.insert(0, repfic)
        textBoxMsgTxtDecrypt.config(state='disabled')
        
    
###########################################



    

####FONCTIONS DE CRYPTAGE ET DECRYPTAGE MESSAGE CODE CESAR####
    
def split(word):
    return [char for char in word]

def verif(num_char):
    if num_char>90 :
        num_char = num_char-25
    return num_char

def Crypto_Cesar(word_clair, cle_cesar, whichWindow):
    
    if (whichWindow == "crypt"):   ######## Si l'utilisateur a cliqué sur le bouton "Valider" de la fenêtre de cryptage
        word_clair = word_clair.upper()
        tab_char = split(word_clair)
        tab_num = [ord(char) for char in tab_char]
        tab_crypto = [chr(verif((num - 1) + cle_cesar)) for num in tab_num]
        return ''.join(tab_crypto)
    
    elif (whichWindow == "decrypt"):  ######## Si l'utilisateur a cliqué sur le bouton "Valider" de la fenêtre de décryptage
        return "blabla" ###test de passage

################################################

####FONCTIONS DE CRYPTAGE ET DECRYPTAGE FICHIER TXT CODE CESAR####

def Crypto_CesarTXT(pathFichierTxt, cle_cesar, whichWindow):
    if (whichWindow == "crypt"):
        
        ###CODE CRYPTAGE VIA FICHIER TXT###
        return pathFichierTxt ###test de passage
    
    elif (whichWindow == "decrypt"):
        
        ###CODE DECRYPTAGE VIA FICHIER TXT###
        
        return pathFichierTxt###test de passage

##################################################







###FONCTION GESTION DES SAISIES ET ERREURS DE CRYPTAGE###


def cesarCodeCrypt():

    
    ###Gestion des erreurs de saisie###
    
    if(MsgTxtCrypt.get() == "" and messageCrypt.get() == ""):
        messagebox.showerror(title="Erreur", message="Veuillez saisir au moins un message à crypter ou selectionnez un fichier txt !")
        return
    
    if (cleCrypt.get() == ""):
        messagebox.showerror(title="Erreur", message="Veuillez saisir une clé de cryptage !")
        return

    try:
        int(cleCrypt.get())
    except ValueError:
        messagebox.showerror(title="Erreur", message="La clé doit être un chiffre !")
        return
    
    ####################################

    fichierTxtSaisie = MsgTxtCrypt.get() ###Variable contenant le chemin complet vers le fichier séléctionné depuis l'interface
    messageSaisie = messageCrypt.get() ###Variable contenant la saisie du message depuis l'interface
    cleSaisie = int(cleCrypt.get()) ###Variable contenant la saisie de la clé depuis l'interface

    ###Gestion des erreurs de saisie du message + fichier txt à crypter###

    if (messageSaisie and fichierTxtSaisie == ""):
        
        CryptedMessage = Crypto_Cesar(messageSaisie, cleSaisie, "crypt") ###Variable qui contient le message une fois crypté via la fonction de cryptage d'un message saisie
        
    elif (fichierTxtSaisie and messageSaisie == ""):
        
        CryptedMessage = Crypto_CesarTXT(fichierTxtSaisie, cleSaisie, "crypt") ###Variable qui contient le message une fois crypté via la fonction fichier txt
        
    else:
        
        messagebox.showerror(title="Erreur", message="Veuillez choisir soit le cryptage par message ou soit le cryptage d'un fichier txt ")
        return
    
    
    
    resultTextCrypt.set("Code crypté : "+CryptedMessage)
    
    ########################################################
    

#########################################################

    

###FONCTION GESTION DES SAISIES ET ERREURS DE DECRYPTAGE###


def cesarCodeDecrypt():

    
    ###Gestion des erreurs de saisie###
    
    if(MsgTxtDecrypt.get() == "" and messageDecrypt.get() == ""):
        messagebox.showerror(title="Erreur", message="Veuillez saisir au moins un message à decrypter ou selectionnez un fichier txt !")
        return
    
    if (cleDecrypt.get() == ""):
        messagebox.showerror(title="Erreur", message="Veuillez saisir une clé de decryptage !")
        return

    try:
        int(cleDecrypt.get())
    except ValueError:
        messagebox.showerror(title="Erreur", message="La clé doit être un chiffre !")
        return
    
    ####################################

    fichierTxtSaisie = MsgTxtDecrypt.get() ###Variable contenant le chemin complet vers le fichier séléctionné depuis l'interface
    messageSaisie = messageDecrypt.get() ###Variable contenant la saisie du message depuis l'interface
    cleSaisie = int(cleDecrypt.get()) ###Variable contenant la saisie de la clé depuis l'interface

    ###Gestion des erreurs de saisie du message + fichier txt à décrypter###

    if (messageSaisie and fichierTxtSaisie == ""):
        
        DeryptedMessage = Crypto_Cesar(messageSaisie, cleSaisie, "decrypt") ###Variable qui contient le message une fois decrypté via la fonction de cryptage d'un message saisie
        
    elif (fichierTxtSaisie and messageSaisie == ""):
        
        DeryptedMessage = Crypto_CesarTXT(fichierTxtSaisie, cleSaisie, "decrypt") ###Variable qui contient le message une fois decrypté via la fonction fichier txt
        
    else:
        
        messagebox.showerror(title="Erreur", message="Veuillez choisir soit le decryptage par message ou soit le decryptage d'un fichier txt ")
        return
    
    
    
    resultTextDecrypt.set("Code decrypté : "+DeryptedMessage)
    
    ########################################################
    

#########################################################

###DEFINITION DES FENETRE DE CRYPTAGE ET DECRYPTAGE###


windowCrypt=Tk()
windowCrypt.geometry("1350x400")
windowCrypt.title("Code césar")
windowCrypt.resizable(False, False)

###Variables cryptage###

messageCrypt = StringVar()
MsgTxtCrypt = StringVar()
cleCrypt = StringVar()
resultTextCrypt = StringVar()

########################

###Variables Décryptage###

messageDecrypt = StringVar()
MsgTxtDecrypt = StringVar()
cleDecrypt = StringVar()
resultTextDecrypt = StringVar()

##########################

###OPTION CRYPTAGE###

labelTitleCrypt=Label(windowCrypt,text="Cryptage d'un message en code césar",fg="blue",font=("arial",16,"bold"))
labelTitleCrypt.place(x=90,y=50)

labelMsgCrypt = Label(windowCrypt,text="Message à crypter :",font=("arial",12)).place(x=100,y=107)
textBoxMsgCrypt = Entry(windowCrypt, width=30, textvariable = messageCrypt)
textBoxMsgCrypt.place(x=280, y=110)

labelOrCrypt = Label(windowCrypt,text="OU",font=("arial",12)).place(x=160,y=133)

labelMsgTxtCrypt = Label(windowCrypt,text="Selectionner un fichier :",font=("arial",12)).place(x=100,y=157)
textBoxMsgTxtCrypt = Entry(windowCrypt, width=30, textvariable = MsgTxtCrypt)
textBoxMsgTxtCrypt.place(x=280, y=160)
textBoxMsgTxtCrypt.config(state='disabled')

labelCleCrypt = Label(windowCrypt,text="Clé de cryptage :",font=("arial",12)).place(x=100,y=197)
textBoxCleCrypt = Entry(windowCrypt, width=30, textvariable = cleCrypt)
textBoxCleCrypt.place(x=280, y=200)

labelResultCrypt = Label(windowCrypt,text="", fg = "green", font=("arial",12), textvariable=resultTextCrypt)
labelResultCrypt.config(anchor=CENTER)
labelResultCrypt.place(x=180, y=320)

boutonCrypt=Button(windowCrypt,text="Valider",relief=RAISED,font=("arial",12,"bold"),command=cesarCodeCrypt)
boutonCrypt.config(anchor=CENTER)
boutonCrypt.place(x=235, y=250)

    

boutonCryptOpen=Button(windowCrypt,text="...",height=1,relief=RAISED,font=("arial",8),command=lambda: ouvrir("crypt"))
boutonCryptOpen.place(x=475, y=155)

########################

###OPTION DECRYPTAGE###

labelTitleDecrypt=Label(windowCrypt,text="Decryptage d'un message en code césar",fg="blue",font=("arial",16,"bold"))
labelTitleDecrypt.place(x=790,y=50)

labelMsgDecrypt = Label(windowCrypt,text="Message à décrypter :",font=("arial",12)).place(x=800,y=107)
textBoxMsgDecrypt = Entry(windowCrypt, width=30, textvariable = messageDecrypt)
textBoxMsgDecrypt.place(x=980, y=110)

labelOrDecrypt = Label(windowCrypt,text="OU",font=("arial",12)).place(x=860,y=133)

labelMsgTxtDecrypt = Label(windowCrypt,text="Selectionner un fichier :",font=("arial",12)).place(x=800,y=157)
textBoxMsgTxtDecrypt = Entry(windowCrypt, width=30, textvariable = MsgTxtDecrypt)
textBoxMsgTxtDecrypt.place(x=980, y=160)
textBoxMsgTxtDecrypt.config(state='disabled')

labelCleDecrypt = Label(windowCrypt,text="Clé de decryptage :",font=("arial",12)).place(x=800,y=197)
textBoxCleDecrypt = Entry(windowCrypt, width=30, textvariable = cleDecrypt)
textBoxCleDecrypt.place(x=980, y=200)

labelResultDecrypt = Label(windowCrypt,text="", fg = "green", font=("arial",12), textvariable=resultTextDecrypt)
labelResultDecrypt.config(anchor=CENTER)
labelResultDecrypt.place(x=880, y=320)

boutonDecrypt=Button(windowCrypt,text="Valider",relief=RAISED,font=("arial",12,"bold"),command=cesarCodeDecrypt)
boutonDecrypt.config(anchor=CENTER)
boutonDecrypt.place(x=935, y=250)


boutonDecryptOpen=Button(windowCrypt,text="...",height=1,relief=RAISED,font=("arial",8),command=lambda: ouvrir("decrypt"))
boutonDecryptOpen.place(x=1175, y=155)

########################

windowCrypt.mainloop()



#################


