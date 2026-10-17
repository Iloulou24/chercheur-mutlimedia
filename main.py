from sources.youtube import recherche_youtube
from sources.deezer import recherche_deezer


def afficher_resultat(resultats):
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
            print("\n")


def rechercher(recherche, nb_resultat):
    sources = [recherche_youtube, recherche_deezer]
    tous_les_resultats = []
    for source in sources:
        resultats = source(recherche, nb_resultat)
        tous_les_resultats.extend(resultats)

    return tous_les_resultats


print(rechercher("python", 3))
print(len(rechercher("python", 3)))
