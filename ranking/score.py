import string


def calculer_score(recherche, resultat):
    """
    calcule le score en fonction du nombre de mots correspondants
    entre la recherche et le resultat
    """
    POINTS_MOT_TITRE = 10
    POINTS_MOT_AUTEUR = 5
    # Bonus pour un résultat qui contient tous les mots de la recherche
    POINTS_BONUS_CORRESPONDANCE = 10
    score = 0
    titre = resultat['titre'].lower().translate(
        str.maketrans("", "", string.punctuation)).split()
    print(f"titre: {titre}")

    auteur = resultat['auteur'].lower().translate(
        str.maketrans("", "", string.punctuation)).split()
    print(f"auteur: {auteur}")

    liste_mots_recherche = recherche.lower().translate(
        str.maketrans("", "", string.punctuation)).split()
    print(f"liste_mots_recherche: {liste_mots_recherche}")

    liste_correspondances = []

    for mot_recherche in liste_mots_recherche:
        if mot_recherche in titre:
            score += POINTS_MOT_TITRE
            liste_correspondances.append(True)
        elif mot_recherche in auteur:
            score += POINTS_MOT_AUTEUR
            liste_correspondances.append(True)
        else:
            liste_correspondances.append(False)

    if all(liste_correspondances):
        score += POINTS_BONUS_CORRESPONDANCE

    return score


resultat = {
    "titre": "Get Lucky()",
    "auteur": "Daft Punk",
    "lien": "...",
    "source": "deezer",
    "type": "musique"
}

print(calculer_score("daft punk - get lucky", resultat))
