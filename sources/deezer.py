import requests


def recherche_deezer(recherche, nb_resultat):

    parametres = {"q": recherche, "limit": nb_resultat}
    url = "https://api.deezer.com/search"
    reponse = requests.get(url, params=parametres,)
    donnees = reponse.json()

    if not donnees["data"]:
        return []
    dico_résultats = []
    for resultat in donnees["data"]:
        titre = resultat["title"]
        auteur = resultat["artist"]["name"]
        type = "musique"
        url = resultat["link"]
        source = "deezer"
        dico_resultat = {"titre": titre, "auteur": auteur,
                         "lien": url, "source": source, "type": type}
        dico_résultats.append(dico_resultat)
    return dico_résultats
