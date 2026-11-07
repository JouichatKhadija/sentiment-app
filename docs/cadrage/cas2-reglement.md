# Fiche de cadrage : questions sur le règlement intérieur d'une école

## Besoin en une phrase
Répondre automatiquement aux questions des étudiants sur le règlement intérieur, en citant l'article concerné.

## Utilisateur final
Les étudiants et le personnel administratif de l'école.

## Approche retenue
- [x] RAG (recherche dans les documents)

## Justification
Les documents existent déjà et sont stables : (b) une réponse doit être vérifiable en citant l'article source, et (a) peu de questions étiquetées sont disponibles au départ, ce qui exclut un apprentissage supervisé. Le RAG s'appuie sur les textes officiels sans les réécrire.

## Données nécessaires
Le règlement intérieur au format texte ou PDF, découpé en articles, et un index de recherche (embeddings).

## Métrique de succès
Taux de réponses correctes avec citation de l'article exact, mesuré sur 50 questions de test, cible 90 %.

## Conséquence d'une erreur
Une réponse fausse sur une règle (sanctions, absences) peut induire l'étudiant en erreur ; la citation de l'article permet de vérifier.

## Risques éthiques ou de confidentialité (obligatoire)
Les questions des étudiants peuvent révéler des situations personnelles ; l'outil ne doit pas conserver l'historique des requêtes.

## Approche écartée et pourquoi (facultatif)
Le modèle génératif seul : il inventerait des articles, ce qui est inacceptable pour un règlement officiel.