from main import *
from tkinter import *
import datetime



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

        if choix == 1:
            liste_jour = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

            text = 'Le ' + chaine_date(int(jour.get()), int(mois.get()), int(annee.get())) + ' est un ' + liste_jour[nb_jour_entre_dates(21, 7, 1969, int(jour.get()), int(mois.get()), int(annee.get()))%7] + '.'
            reponse = Label(boite_affichage, text=text, font=('Courrier', 10, 'bold'))   
            reponse.pack()    
        elif choix == 3:
            aujourd_hui = datetime.date.today()
            text = 'Entre le ' + chaine_date(int(jour.get()), int(mois.get()), int(annee.get())) + ' et le ' + chaine_date(aujourd_hui.day, aujourd_hui.month, aujourd_hui.year) + ' il y a ' + str(nb_jour_entre_dates(int(jour.get()), int(mois.get()), int(annee.get()), aujourd_hui.day, aujourd_hui.month, aujourd_hui.year)) + ' jours.'
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

    global boite_affichage
    global choix

    choix = 3

    global annee
    global mois
    global jour

    boite_affichage.destroy()

    boite_affichage = Frame(fenetre)
    boite_affichage.pack(side=RIGHT)
    
    label_naissance = Label(boite_affichage, text='Entrez votre date de naissance :', font=('Courrier',12))
    label_naissance.pack()

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

def choix4():
    fenetre.destroy()


fenetre = Tk()
fenetre.title("Calendrier Python")
fenetre.geometry("560x360")
fenetre.minsize(560, 360)

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