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
        num_char = num_char-26
    return num_char

def verif_inverse(num_char):
    if num_char<65 :
        num_char = num_char+26
    return num_char

def Crypto_Cesar(word_clair, cle_cesar, whichWindow):
    
    if (whichWindow == "crypt"):   ######## Si l'utilisateur a cliqué sur le bouton "Valider" de la fenêtre de cryptage
        word_clair = word_clair.upper()
        tab_char = split(word_clair)
        tab_num = [ord(char) for char in tab_char]
        tab_crypto = [chr(verif((num) + cle_cesar)) for num in tab_num]
        return ''.join(tab_crypto)
    
    elif (whichWindow == "decrypt"):  ######## Si l'utilisateur a cliqué sur le bouton "Valider" de la fenêtre de décryptage
        word_clair = word_clair.upper()
        tab_char = split(word_clair)
        tab_num = [ord(char) for char in tab_char]
        tab_crypto = [chr(verif_inverse(num - cle_cesar)) for num in tab_num]
        return ''.join(tab_crypto)
        

################################################

####FONCTIONS DE CRYPTAGE ET DECRYPTAGE FICHIER TXT CODE CESAR####

def Crypto_CesarTXT(pathFichierTxt, cle_cesar, whichWindow):
    
    ###Compter le nombre de ligne###
    txt = open(pathFichierTxt)
    lineCount = 0

    for line in txt:
        if line != "\n":
            lineCount += 1
    ################################
            
    if (whichWindow == "crypt"):
          
        with open(pathFichierTxt) as f:
            content = f.read().splitlines()
            
        file = [ 0 for _ in range(lineCount)]
        cpt = 0
    
        for line in content:
            file[cpt] = Crypto_Cesar(line, cle_cesar, whichWindow)
            cpt += 1
        return file

    
    elif (whichWindow == "decrypt"):
        
        with open(pathFichierTxt) as f:
            content = f.read().splitlines()
        file = [ 0 for _ in range(lineCount)]
        cpt = 0
    
        for line in content:
            file[cpt] = Crypto_Cesar(line, cle_cesar, whichWindow)
            cpt += 1
        return file
        

##################################################







###FONCTION GESTION DES SAISIES ET ERREURS DE CRYPTAGE###


def cesarCodeCrypt():

    listResultCrypt.delete(0, END)
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

        resultTextTitleCrypt.set("Code crypté : ")
        listResultCrypt.insert(0,CryptedMessage)
        
    elif (fichierTxtSaisie and messageSaisie == ""):
        
        CryptedMessage = Crypto_CesarTXT(fichierTxtSaisie, cleSaisie, "crypt") ###Variable qui contient le message une fois crypté via la fonction fichier txt

        
        
        resultTextTitleCrypt.set("Code crypté : ")
        for lignes in CryptedMessage:
            cpt = 0
            listResultCrypt.insert(cpt, lignes)
            cpt += 1
        
    else:
        
        messagebox.showerror(title="Erreur", message="Veuillez choisir soit le cryptage par message ou soit le cryptage d'un fichier txt ")
        return
    
    
    
    
    
    ########################################################
    

#########################################################

    

###FONCTION GESTION DES SAISIES ET ERREURS DE DECRYPTAGE###


def cesarCodeDecrypt():

    listResultDecrypt.delete(0, END)
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
        
        DecryptedMessage = Crypto_Cesar(messageSaisie, cleSaisie, "decrypt") ###Variable qui contient le message une fois decrypté via la fonction de cryptage d'un message saisie

        resultTextTitleCrypt.set("Code crypté : ")
        listResultDecrypt.insert(0,DecryptedMessage)
        
    elif (fichierTxtSaisie and messageSaisie == ""):
        
        DecryptedMessage = Crypto_CesarTXT(fichierTxtSaisie, cleSaisie, "decrypt") ###Variable qui contient le message une fois decrypté via la fonction fichier txt

        resultTextTitleDecrypt.set("Code crypté : ")
        for lignes in DecryptedMessage:
            cpt = 0
            listResultDecrypt.insert(cpt, lignes)
            cpt += 1
        
    else:
        
        messagebox.showerror(title="Erreur", message="Veuillez choisir soit le decryptage par message ou soit le decryptage d'un fichier txt ")
        return
    
    
    
    resultTextTitleDecrypt.set("Code décrypté : ")
    resultTextDecrypt.set(DecryptedMessage)
    
    ########################################################
    

#########################################################

def clearMsgTxt(whichWindow):
    if (whichWindow == "crypt"):
        textBoxMsgTxtCrypt.config(state="normal")
        textBoxMsgTxtCrypt.delete(0, END)
        textBoxMsgTxtCrypt.config(state="disabled")
    elif (whichWindow == "decrypt"):
        textBoxMsgTxtDecrypt.config(state="normal")
        textBoxMsgTxtDecrypt.delete(0, END)
        textBoxMsgTxtDecrypt.config(state="disabled")
        

###DEFINITION DES FENETRE DE CRYPTAGE ET DECRYPTAGE###


windowCrypt=Tk()
windowCrypt.geometry("1350x600")
windowCrypt.title("Code césar")
windowCrypt.resizable(False, False)

###Variables cryptage###

messageCrypt = StringVar()
MsgTxtCrypt = StringVar()
cleCrypt = StringVar()
resultTextCrypt = StringVar()
resultTextTitleCrypt = StringVar()

########################

###Variables Décryptage###

messageDecrypt = StringVar()
MsgTxtDecrypt = StringVar()
cleDecrypt = StringVar()
resultTextDecrypt = StringVar()
resultTextTitleDecrypt = StringVar()

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

labelResultTitleCrypt = Label(windowCrypt,text="", fg = "green", font=("arial",12), textvariable=resultTextTitleCrypt)
labelResultTitleCrypt.config(anchor=CENTER)
labelResultTitleCrypt.place(x=220, y=300)
listResultCrypt = Listbox(windowCrypt, width=30)
listResultCrypt.place(x=180, y=340)

boutonCrypt=Button(windowCrypt,text="Valider",relief=RAISED,font=("arial",12,"bold"),command=cesarCodeCrypt)
boutonCrypt.config(anchor=CENTER)
boutonCrypt.place(x=235, y=250)

    

boutonCryptOpen=Button(windowCrypt,text="...",height=1,relief=RAISED,font=("arial",8),command=lambda: ouvrir("crypt"))
boutonCryptOpen.place(x=475, y=155)

boutonCryptClear=Button(windowCrypt,text="clear",height=1,relief=RAISED,font=("arial",8),command=lambda: clearMsgTxt("crypt"))
boutonCryptClear.place(x=505, y=155)

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

labelResultTitleDecrypt = Label(windowCrypt,text="", fg = "green", font=("arial",12), textvariable=resultTextTitleDecrypt)
labelResultTitleDecrypt.config(anchor=CENTER)
labelResultTitleDecrypt.place(x=915, y=300)
listResultDecrypt = Listbox(windowCrypt, width=30)
listResultDecrypt.place(x=880, y=340)

boutonDecrypt=Button(windowCrypt,text="Valider",relief=RAISED,font=("arial",12,"bold"),command=cesarCodeDecrypt)
boutonDecrypt.config(anchor=CENTER)
boutonDecrypt.place(x=935, y=250)


boutonDecryptOpen=Button(windowCrypt,text="...",height=1,relief=RAISED,font=("arial",8),command=lambda: ouvrir("decrypt"))
boutonDecryptOpen.place(x=1175, y=155)

boutonDecryptClear=Button(windowCrypt,text="clear",height=1,relief=RAISED,font=("arial",8),command=lambda: clearMsgTxt("decrypt"))
boutonDecryptClear.place(x=1205, y=155)

########################

windowCrypt.mainloop()



#################


