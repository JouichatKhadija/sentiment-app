"""Tests du modèle de sentiment (TP2)."""
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
METRIQUES = RACINE / "models" / "metrics.json"


def lire_metriques() -> dict:
    import json
    assert METRIQUES.exists(), "models/metrics.json absent : lancez python src/train.py"
    return json.loads(METRIQUES.read_text(encoding="utf-8"))


def test_metriques_completes():
    m = lire_metriques()
    for cle in ("source", "f1_macro", "n_train", "n_test"):
        assert cle in m, f"clé absente : {cle}"


def test_f1_au_dessus_du_seuil():
    m = lire_metriques()
    assert m["f1_macro"] >= 0.85


@pytest.fixture(scope="module")
def predicteur():
    import sys
    sys.path.insert(0, str(RACINE / "src"))
    from predict import predict
    return predict


def test_prediction_evidente(predicteur):
    # predict() applique l'abstention et met en majuscules ; ici le score est élevé
    sortie = predicteur("Service impeccable, livraison rapide, je recommande")
    assert sortie["label"] in {"POSITIVE", "INDETERMINE"}


def test_format_de_sortie(predicteur):
    sortie = predicteur("Conforme à la description")
    assert {"label", "score"} <= set(sortie)
    assert sortie["label"] in {"POSITIVE", "NEGATIVE", "INDETERMINE"}
    assert 0.0 <= sortie["score"] <= 1.0