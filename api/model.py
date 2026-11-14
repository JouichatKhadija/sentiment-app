"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() de sentiment_app.predict, qui charge le modèle une seule fois.
"""
from sentiment_app.predict import charger_modele  # noqa: E402
from sentiment_app.predict import predict as _predict  # noqa: E402


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()  # échoue immédiatement si le joblib manque : on ne démarre pas sans modèle

    def predict(self, text: str) -> dict:
        """Renvoie {'label': 'POSITIVE'|'NEGATIVE'|'INDETERMINE', 'score': float, 'text': aperçu}."""
        r = _predict(text)  # lève ValueError si le texte est vide ; applique déjà le seuil
        return {"label": r["label"], "score": r["score"], "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans sentiment_app.predict)."""
    return SentimentClassifier()