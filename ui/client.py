"""Client de l'API : traduit chaque réponse en message clair pour la page."""
from dataclasses import dataclass

import httpx

API_URL = "http://127.0.0.1:8000"

REFUS = "Texte refusé : vide, fait d'espaces, ou de plus de 2000 caractères"
SANS_MODELE = "Modèle non chargé : relancez l'API"
INJOIGNABLE = "API injoignable : lancez d'abord uvicorn api.main:app"

VERDICTS = {"POSITIVE": "Avis positif", "NEGATIVE": "Avis négatif", "INDETERMINE": "Je ne sais pas"}


@dataclass
class Reponse:
    """Ce que l'interface affiche : un verdict, ou un message d'erreur lisible."""
    ok: bool
    label: str | None = None
    score: float | None = None
    message: str = ""


def creer_session() -> httpx.Client:
    """La connexion à l'API. Les tests la remplacent par un client en mémoire."""
    return httpx.Client(base_url=API_URL, timeout=10)


def sante(session: httpx.Client) -> Reponse:
    try:
        r = session.get("/health")
    except httpx.RequestError:
        return Reponse(ok=False, message=INJOIGNABLE)
    if r.status_code == 200:
        return Reponse(ok=True, message=r.json().get("model", ""))
    return Reponse(ok=False, message=f"API en erreur (code {r.status_code})")


def predire(session: httpx.Client, texte: str) -> Reponse:
    try:
        r = session.post("/predict", json={"text": texte})
    except httpx.RequestError:
        return Reponse(ok=False, message=INJOIGNABLE)
    if r.status_code == 200:
        body = r.json()
        return Reponse(ok=True, label=body["label"], score=body["score"])
    if r.status_code == 422:
        return Reponse(ok=False, message=REFUS)
    if r.status_code == 503:
        return Reponse(ok=False, message=SANS_MODELE)
    return Reponse(ok=False, message=f"Erreur interne de l'API (code {r.status_code})")


def predire_lot(session: httpx.Client, textes: list[str]) -> list[Reponse]:
    """Envoie un avis à la fois : un refus n'invalide pas tout le lot."""
    return [predire(session, t) for t in textes]


def resumer(reponses: list[Reponse]) -> dict:
    """Compte les verdicts et les refus/erreurs."""
    resume: dict[str, int] = {}
    for r in reponses:
        if r.ok and r.label is not None:
            resume[r.label] = resume.get(r.label, 0) + 1
        else:
            resume["REFUS OU ERREUR"] = resume.get("REFUS OU ERREUR", 0) + 1
    return resume