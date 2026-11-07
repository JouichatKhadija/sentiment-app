# Semaine 2 : le modèle de sentiment

## Mesures

| Jeu de données | Avis de test | F1 macro |
| --- | --- | --- |
| Démonstration (290 avis) | 58 | 0,879 |
| Allociné (20 000 avis) | 4 000 | 0,920 |

## Analyse des erreurs

Sur le jeu de démonstration, la matrice de confusion compte 27 négatifs et 24 positifs bien classés, 2 négatifs classés positifs et 5 positifs classés négatifs : 7 erreurs sur 58. Les 7 erreurs portent toutes sur des avis mitigés, qui commencent dans un sens et se retournent ensuite (« sauf que ensuite », « mais finalement », « avant que », « puis rapidement »). Dans chaque cas, la prédiction suit la première partie de l'avis, alors que le verdict est donné par la fin : le modèle additionne les poids des mots sans tenir compte de leur ordre, et un sac de mots ne voit pas qu'un connecteur comme « sauf que » renverse le sens de ce qui précède. Pour corriger ces erreurs, il faudrait une représentation qui tient compte de l'ordre et du contexte des mots, comme les embeddings de phrase vus en semaine 9.