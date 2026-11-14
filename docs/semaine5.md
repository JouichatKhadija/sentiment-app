# Semaine 5 : l'interface Streamlit

## 1. Pourquoi l'interface n'importe-t-elle jamais le modèle ?

L'interface ne connaît que l'API (règle 3 d'architecture). Elle envoie `POST /predict` à l'adresse de l'API et ne charge jamais `models/sentiment.joblib`. Ainsi, un modèle réentraîné ou une API déplacée sur un autre serveur ne demande aucune modification de l'interface.

## 2. Que montre-t-elle quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Quand le score est sous le seuil d'abstention (0.60), l'API renvoie `INDETERMINE`, et l'interface affiche « Je ne sais pas : à faire vérifier par un humain », avec le score (par exemple 52 %). C'est mieux qu'un verdict forcé car une prédiction peu fiable peut induire l'utilisateur en erreur ; il vaut mieux signaler l'incertitude et laisser un humain trancher.

## 3. Que voit l'utilisateur quand l'API tombe ?

En haut de la page, une erreur « API injoignable : lancez d'abord uvicorn api.main:app ». L'interface ne plante pas, elle affiche un message clair et invite à relancer l'API.