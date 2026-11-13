"""Tests d'intégration : l'API telle qu'elle tourne (TP4, étape D)."""
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from api import main as api_main
from src import predict


@pytest.fixture
def client():
    with TestClient(api_main.app) as c:
        yield c


def test_demarrage_reel(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "OK"


def test_modele_absent_refuse_de_demarrer(monkeypatch):
    monkeypatch.setattr(predict, "MODELE", Path("nexiste-pas.joblib"))
    predict.charger_modele.cache_clear()
    with pytest.raises(FileNotFoundError):
        predict.charger_modele()
    predict.charger_modele.cache_clear()


def test_modele_retire_renvoie_503(client):
    ancien = api_main.app.state.classifier
    api_main.app.state.classifier = None
    try:
        r = client.post("/predict", json={"text": "test"})
        assert r.status_code == 503
    finally:
        api_main.app.state.classifier = ancien


def test_modele_plante_renvoie_500_sans_message_interne(client):
    class Panne:
        model_name = "panne"
        def predict(self, text):
            raise ValueError("bug interne")

    ancien = api_main.app.state.classifier
    api_main.app.state.classifier = Panne()
    try:
        r = client.post("/predict", json={"text": "test"})
        assert r.status_code == 500
        assert "bug interne" not in r.text
    finally:
        api_main.app.state.classifier = ancien