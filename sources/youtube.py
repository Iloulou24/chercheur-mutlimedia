from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from pathlib import Path
import os

chemin_env = Path(__file__).parent.parent / ".env"
load_dotenv(chemin_env)

clé_api_yt = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=clé_api_yt)


def recherche_youtube(recherche, nb_resultat):
    try:
        reponses = youtube.search().list(
            # le groupe de données qu'on veut, snippet: titre, description, chaîne, miniature...
            part="snippet",
            q=recherche,  # la recherche
            type="video",  # le type de fichier
            maxResults=nb_resultat  # nombre de résultat max
        ).execute()
    except HttpError as error:
        print(error)
        return []

    if not reponses["items"]:
        return []
    dico_résultats = []
    for resultat in reponses["items"]:
        titre = resultat["snippet"]["title"]
        auteur = resultat["snippet"]["channelTitle"]
        type = "video"
        Id_video = resultat["id"]["videoId"]
        url = "https://www.youtube.com/watch?v=" + Id_video
        source = "youtube"
        dico_resultat = {"titre": titre, "auteur": auteur,
                         "lien": url, "source": source, "type": type}
        dico_résultats.append(dico_resultat)
    return dico_résultats
