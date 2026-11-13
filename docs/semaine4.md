## 1. Mesures de départ (T21)

- pytest : 1 failed, 51 passed, 1 skipped (jeu d'or vide, attendu)
- Couverture : TOTAL 91 % ; 6 lignes manquantes dans api/main.py : 49, 77-79, 85-87
- ruff : 11 remarques (B904 ×2, I001 ×2, F401 ×2, B905 ×2, E741 ×3)
- mypy : Success: no issues found in 4 source files

## 5. Qualité statique au départ

- ruff : 11 remarques (B904, I001, F401, B905, E741)
- mypy : aucune remarque (predict() renvoie un dict, tout est Any)