def annee_bissextile(annee):
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
    return True
