import datetime



def annee_bissextile(annee):
    if date_anterieure(1, 1, annee, 15, 10 ,1582):
        return annee % 4 == 0
    return annee%400 == 0 or (annee%4 == 0 and annee%100 != 0)

def nb_jour_mois(mois, annee):
    if mois == 2:   
        if annee_bissextile(annee):
            return 29
        else:
            return 28  
    elif mois <8:
        if mois%2 == 0:
            return 30
        else:
            return 31
    else:
        if mois%2 == 0:
            return 31
        else:
            return 30

def date_valide(jour, mois, annee):
    if mois<1 or mois>12:
        return False
    elif jour > nb_jour_mois(mois, annee) or jour<1:
        return False
    elif mois == 10 and annee == 1582 and jour>=5 and jour<=14:
        return False
    return True

def chaine_date(jour, mois, annee):
    liste_mois = ['Janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre'] 

    return ('1er' if jour == 1 else str(jour)) +' '+ liste_mois[mois-1] +' '+ str(annee)


def nb_jour_annee(annee):
    if annee_bissextile(annee):
        return 366
    return 365

def nb_jour_fin_annee(jour, mois, annee):
    nb_jour = nb_jour_mois(mois, annee) - jour

    for i in range(mois+1, 13):
        nb_jour += nb_jour_mois(i, annee)

    return nb_jour + 1

def nb_jour_debut_annee(jour, mois, annee):
    nb_jour = jour

    for i in range(1, mois):
        nb_jour += nb_jour_mois(i, annee)

    return nb_jour - 1

def nb_jour_annee_entiere(annee1,annee2):
    nb_jour_annee_entiere = 0

    for annee in range(annee1+1,annee2):
        nb_jour_annee_entiere += nb_jour_annee(annee)

    return nb_jour_annee_entiere

def nb_jour_mois_entier(mois1, mois2,annee):
    nb_jour_mois_entier = 0

    for mois in range(mois1+1,mois2):
        nb_jour_mois_entier += nb_jour_mois(mois,annee)

    return nb_jour_mois_entier

def date_anterieure(jour1, mois1, annee1, jour2, mois2 ,annee2):
    if annee1 < annee2:
        return True
    elif annee1 == annee2 and mois1 < mois2:
        return True
    elif annee1 == annee2 and mois1 == mois2 and jour1 < jour2:
        return True
    return False

def nb_jour_entre_dates(jour1, mois1, annee1, jour2, mois2 ,annee2):
    nb_jour_entre_dates = 0
    
    if date_anterieure(jour1, mois1, annee1, jour2, mois2 ,annee2):
        if annee1 == annee2:
            if annee1 == annee2 and mois1 == mois2:
                nb_jour_entre_dates = jour2 - jour1
            else:
                nb_jour_entre_dates = nb_jour_mois(mois1, annee1) - jour1 + nb_jour_mois_entier(mois1, mois2, annee1) + jour2
        else:
            nb_jour_entre_dates = nb_jour_fin_annee(jour1, mois1, annee1) + nb_jour_annee_entiere(annee1,annee2) + nb_jour_debut_annee(jour2, mois2, annee2)
    
    elif date_anterieure(jour1, mois1, annee1, jour2, mois2 ,annee2) is False:
        if annee1 == annee2:
            if annee1 == annee2 and mois1 == mois2:
                nb_jour_entre_dates = jour2 - jour1
            else:
                nb_jour_entre_dates = -(nb_jour_mois(mois2, annee2) - jour2 + nb_jour_mois_entier(mois2, mois1, annee2) + jour1)
    
        else:
            nb_jour_entre_dates = -(nb_jour_fin_annee(jour2, mois2 ,annee2) + nb_jour_annee_entiere(annee2,annee1) + nb_jour_debut_annee(jour1, mois1, annee1))
    
    if date_anterieure(jour1, mois1, annee1, 15, 10 ,1582) and date_anterieure(15, 10 ,1582, jour2, mois2, annee2):
        return nb_jour_entre_dates - 10
    elif date_anterieure(jour2, mois2, annee2, 15, 10 ,1582) and date_anterieure(15, 10 ,1582, jour1, mois1, annee1): 
        return nb_jour_entre_dates + 10
    return nb_jour_entre_dates



if __name__ == "__main__":
    Ouverture_menu = True

    while Ouverture_menu:
        choix = int(input("\necrire le chiffre correspondant a votre choix : \n\n1. Calcul du jour de la semaine correspondant a une date\n2. Calcul du nombre de jours separant deux dates\n3. Calcul du nombre de jours ecoules depuis votre naissance\n4. Sortie du programme\n... "))

        if choix == 4:
            Ouverture_menu = False

        elif choix == 1:
            date_invalide = True
            liste_jour = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

            while date_invalide:
                annee = int(input("Entre l'annee : "))
                mois = int(input("Entre le mois : "))
                jour = int(input("Entre le jour : "))

                if date_valide(jour, mois, annee):
                    date_invalide = False
                else:
                    print("date invalide...")

            print('\nLe', chaine_date(jour, mois, annee), 'est un',
                liste_jour[nb_jour_entre_dates(21, 7, 1969, jour, mois ,annee)%7], end='.')

        elif choix == 2:    
            date_invalide = True

            while date_invalide:
                annee1 = int(input("Entre l'annee de ta premiere date : "))
                mois1 = int(input("Entre le mois de ta premiere date : "))
                jour1 = int(input("Entre le jour de ta premiere date : "))
                annee2 = int(input("Entre l'annee de ta deuxieme date : "))
                mois2 = int(input("Entre le mois de ta deuxieme date : "))
                jour2 = int(input("Entre le jour de ta deuxieme date : "))

                if date_valide(jour1, mois1, annee1) is False:
                    print("premiere date invalide...")
                if date_valide(jour2, mois2, annee2) is False:
                    print("deuxieme date invalide...")
                if date_valide(jour1, mois1, annee1) and date_valide(jour2, mois2, annee2):
                    date_invalide = False

            print('\nEntre le', chaine_date(jour1, mois1, annee1), 'et le', chaine_date(jour2, mois2, annee2),
                'il y a', nb_jour_entre_dates(jour1, mois1, annee1, jour2, mois2 ,annee2), 'jours.')
            
        elif choix == 3:
            aujourd_hui = datetime.date.today()
            date_invalide = True

            while date_invalide:
                annee = int(input("Entre ton annee de naissance : "))
                mois = int(input("Entre ton mois de naissance : "))
                jour = int(input("Entre ton jour de naissance : "))

                if date_valide(jour, mois, annee):
                    date_invalide = False
                else:
                    print("date invalide...")

            print('\nEntre le', chaine_date(jour, mois, annee), 'et le',
                chaine_date(aujourd_hui.day, aujourd_hui.month, aujourd_hui.year),'il y a',
                    nb_jour_entre_dates(jour, mois, annee, aujourd_hui.day, aujourd_hui.month, aujourd_hui.year), 'jours.')
                