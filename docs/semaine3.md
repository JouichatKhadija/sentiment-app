# Semaine 3 : API FastAPI

## Deux questions

### Pourquoi l'API refuse-t-elle de démarrer sans modèle, plutôt que de répondre 503 ?

Une API sans modèle ne peut jamais répondre correctement. En refusant de démarrer, elle rend la panne visible immédiatement, au moment du déploiement, au lieu de paraître en marche et de renvoyer 503 à chaque client. Le code 503 sert aux indisponibilités passagères, quand le modèle a été retiré en cours de route.

### Un texte vide est refusé deux fois (Pydantic puis `predict()`), est-ce redondant ?

Non : Pydantic protège l'API en amont, pour toute requête HTTP, en refusant un texte vide avant même d'appeler `predict()`. `predict()` protège le modèle quand il est appelé directement, par un test ou un autre script. Les deux barrières couvrent deux contextes différents.