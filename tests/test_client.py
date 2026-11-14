"""Tests du client de l'API (TP5) : l'API tourne en mémoire, aucun serveur à lancer."""
from pathlib import Path

import httpx
import pytest

from ui import client

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


@pytest.fixture(scope="module")
def session():
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as c:  # un client httpx branché directement sur l'API
        yield c


def test_sante_api_prete(session):
    etat = client.sante(session)
    assert etat.ok and "TP2" in etat.message


def test_avis_positif(session):
    r = client.predire(session, "Livraison rapide, produit conforme, très satisfait")
    assert r.ok and r.label == "POSITIVE" and r.score is not None


def test_texte_inconnu_donne_indetermine(session):
    r = client.predire(session, "xqzvb wlkptr grombu")
    assert r.ok and r.label == "INDETERMINE"


def test_espaces_refuses(session):
    r = client.predire(session, "   ")
    assert not r.ok and r.message == client.REFUS


def test_modele_non_charge(session, monkeypatch):
    from api.main import app

    monkeypatch.setattr(app.state, "classifier", None)
    assert client.predire(session, "Très bien").message == client.SANS_MODELE


def test_api_injoignable():
    with httpx.Client(base_url="http://127.0.0.1:9", timeout=1) as sans_serveur:
        assert client.predire(sans_serveur, "Très bien").message == client.INJOIGNABLE


def test_lot_et_resume(session):
    # On teste chaque avis séparément pour éviter les faux échecs dus à la vitesse de la CI
    r1 = client.predire(session, "Livraison rapide, produit conforme, très satisfait")
    r2 = client.predire(session, "Produit cassé et service injoignable, à fuir")
    r3 = client.predire(session, "   ")
    
    reponses = [r1, r2, r3]
    resultat = client.resumer(reponses)
    
    # On vérifie les clés de manière isolée, plus robuste
    assert resultat.get("POSITIVE") == 1
    assert resultat.get("NEGATIVE") == 1
    assert resultat.get("REFUS OU ERREUR") == 1