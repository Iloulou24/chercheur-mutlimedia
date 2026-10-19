def calculer_score(recherche, resultat):
    """
    calcule le score en fonction du nombre de mots correspondants
    entre la recherche et le resultat
    """
    POINTS_MOT_TITRE = 10
    POINTS_MOT_AUTEUR = 5
    score = 0
    titre = resultat['titre'].lower()
    auteur = resultat['auteur'].lower()
    liste_mots_recherche = recherche.lower().split()
    for mot in liste_mots_recherche:
        if mot in titre:
            score += POINTS_MOT_TITRE
        elif mot in auteur:
            score += POINTS_MOT_AUTEUR

    # Add logic to calculate the score here
    return score


resultat = {
    "titre": "Get Lucky",
    "auteur": "Daft Punk",
    "lien": "...",
    "source": "deezer",
    "type": "musique"
}

print(calculer_score("mozart symphony", resultat))
