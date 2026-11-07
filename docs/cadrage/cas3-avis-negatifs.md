# Fiche de cadrage : prioriser les avis négatifs d'un site e-commerce

## Besoin en une phrase
Classer automatiquement les avis clients en positifs et négatifs pour que le service client traite d'abord les avis négatifs.

## Utilisateur final
L'équipe du service client du site e-commerce.

## Approche retenue
- [x] Machine learning supervisé

## Justification
Des milliers d'avis sont disponibles et peuvent être étiquetés : (a) les données étiquetées sont nombreuses, et (c) le coût par requête est faible une fois le modèle entraîné. (d) Un avis négatif mal classé retarde la prise en charge d'un client mécontent.

## Données nécessaires
Un jeu d'avis clients déjà étiquetés positifs/négatifs, et éventuellement les notes en étoiles comme signal faible.

## Métrique de succès
F1 macro sur la classe négative, mesuré sur un jeu de test, cible 0,85.

## Conséquence d'une erreur
Un avis négatif classé positif est ignoré par le service client : le client mécontent n'est pas rappelé, ce qui dégrade la satisfaction.

## Risques éthiques ou de confidentialité (obligatoire)
Les avis peuvent contenir des données personnelles ; le modèle ne doit pas les mémoriser et l'interface doit anonymiser les noms.

## Approche écartée et pourquoi (facultatif)
Les règles à base de mots-clés : trop fragiles face aux avis ironiques ou mitigés, qui sont justement les plus urgents à traiter.