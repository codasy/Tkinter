from tkinter import *

from tkinter import messagebox



window=Tk()
window.geometry("500x500")
window.title("Code césar")
window.resizable(False, False)

###CODE PYTHON###

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
    CryptedMessage = str() ###Variable qui contiendra le message une fois crypté
    
    
    
    ###Pour afficher le resultat sur l'interface : resultText.set("leResultat")
    

    
    

#################
message = StringVar()
cle = StringVar()
resultText = StringVar()

label1=Label(window,text="Cryptage d'un message en code césar",fg="blue",font=("arial",16,"bold")).place(x=50,y=110)

labelMsg = Label(window,text="Message à crypter :",font=("arial",12)).place(x=100,y=197)
textBoxMsg = Entry(window, width=20, textvariable = message).place(x=260, y=200)


labelCle = Label(window,text="Clé de crytpage :",font=("arial",12)).place(x=119,y=247)
textBoxCle = Entry(window, width=20, textvariable = cle).place(x=260, y=250)

labelResult = Label(window,text="", fg = "green", font=("arial",12), textvariable=resultText).place(x=180,y=290)

bouton1=Button(window,text="Valider",relief=RAISED,font=("arial",12,"bold"),command=cesarCode)
bouton1.place(x=210, y=350)



window.mainloop()
