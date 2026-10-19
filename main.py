from sources.youtube import recherche_youtube
from sources.deezer import recherche_deezer
from ranking.score import calculer_score


def afficher_resultat(resultats, recherche):
    """résultat sous la forme d'un dictionnaire contenant des dictionnaires
    [{titre:... ,chaine:... ,lien:...,source:...},
     {...},
     }
    """
    if not resultats:
        print("aucun résultat trouvé")
    else:
        for resultat in resultats:
            for info in resultat:
                print(f"{info} : {resultat[info]}")
            print(f"{calculer_score(recherche, resultat)}\n")


def rechercher(recherche, nb_resultat):
    sources = [recherche_youtube, recherche_deezer]
    tous_les_resultats = []
    for source in sources:
        resultats = source(recherche, nb_resultat)
        tous_les_resultats.extend(resultats)
    tous_les_resultats.sort(
        key=lambda resultat: calculer_score(recherche, resultat),
        reverse=True)
    return tous_les_resultats


recherche = "daft punk , get lucky"
nb_resultat = 3

afficher_resultat(rechercher(recherche, nb_resultat), recherche)
print(len(rechercher(recherche, nb_resultat)))
