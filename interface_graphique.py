from main import *
from tkinter import *



def valider():

    global boite_affichage
    global label_invalide
    global choix

    global annee
    global mois
    global jour

    label_invalide.destroy()
    label_invalide = Label(fenetre, text='Date invalide...', font=('Courrier', 10, 'bold'), fg='red')

    
    if date_valide(int(jour.get()), int(mois.get()), int(annee.get())):
        annee = int(annee.get())
        mois = int(mois.get())
        jour = int(jour.get())

        if choix == 1:
            liste_jour = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

            text = 'Le ' + chaine_date(jour, mois, annee) + ' est un ' + liste_jour[nb_jour_entre_dates(21, 7, 1969, jour, mois ,annee)%7] + '.'
            reponse = Label(boite_affichage, text=text, font=('Courrier', 10, 'bold'))   
            reponse.pack()        
    else:
        label_invalide.pack()
    

def choix1():

    global boite_affichage
    global choix

    choix = 1

    global annee
    global mois
    global jour

    boite_affichage.destroy()

    boite_affichage = Frame(fenetre)
    boite_affichage.pack(side=RIGHT)

    annee = Entry(boite_affichage)
    annee.insert(0, "Entrez l'annee...")
    annee.pack()  

    mois = Entry(boite_affichage)
    mois.insert(0, "Entrez le mois...")
    mois.pack() 

    jour = Entry(boite_affichage)
    jour.insert(0, "Entrez le jour...")
    jour.pack() 

    bouton_valider = Button(boite_affichage, text='Valider', command=valider)
    bouton_valider.pack()

def choix2():
    
    global boite_affichage

    boite_affichage.destroy()

    boite_affichage = Frame(fenetre)
    boite_affichage.pack(side=RIGHT)

    label = Label(boite_affichage, text='TACOS')
    label.pack()

def choix3():
    pass

def choix4():
    pass


fenetre = Tk()
fenetre.title("Calendrier Python")
fenetre.geometry("480x360")
fenetre.minsize(480, 360)

boite_choix = Frame(fenetre)
boite_affichage = Frame(fenetre)
boite_affichage.pack(side=RIGHT)

label_invalide = Label(fenetre, text='')
label_invalide.pack()

titre = Label(boite_choix, text="Que faire ?", font=('Courrier',20))
titre.pack()

bouton1 = Button(boite_choix, text='Jour de la semaine', font=('Courrier',10), command=choix1)
bouton1.pack(fill=X)

bouton2 = Button(boite_choix, text='Jour entre 2 dates', font=('Courrier',10), command=choix2)
bouton2.pack(fill=X)

bouton3 = Button(boite_choix, text='Jour depuis votre naissance', font=('Courrier',10), command=choix3)
bouton3.pack(fill=X)

bouton4 = Button(boite_choix, text='Sortir du programme', font=('Courrier',10), command=choix4)
bouton4.pack(fill=X)

boite_choix.pack(side=LEFT)

fenetre.mainloop()

