"""Prédiction unitaire : la fonction que l'API appelle.

Usage :
  python -m sentiment_app.predict "Livraison rapide, très satisfait"
"""
import os
import sys
from functools import lru_cache
from pathlib import Path

import joblib

SEUIL_ABSTENTION = 0.60


def chemin_modele() -> Path:
    """Emplacement du modèle : SENTIMENT_MODELE, ou models/sentiment.joblib par défaut."""
    env = os.environ.get("SENTIMENT_MODELE")
    if env:
        return Path(env)
    return Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"


@lru_cache(maxsize=1)
def charger_modele():
    """Chargé une seule fois par processus, pas à chaque appel."""
    m = chemin_modele()
    if not m.exists():
        raise FileNotFoundError(f"modèle introuvable : {m}")
    return joblib.load(m)


def predict(texte: str) -> dict:
    """Renvoie {'label': 'POSITIVE'|'NEGATIVE'|'INDETERMINE', 'score': float}."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette = pipeline.predict([texte])[0]
    score = float(pipeline.predict_proba([texte]).max())
    label = str(etiquette).upper()
    if score < SEUIL_ABSTENTION:
        label = "INDETERMINE"
    return {"label": label, "score": round(score, 4)}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())