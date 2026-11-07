## Besoin en une phrase
Détecter automatiquement les ordonnances incomplètes avant leur validation par le pharmacien.

## Utilisateur final
Le pharmacien et son préparateur en officine.

## Approche retenue
- [x] Règles métier

## Justification
Les champs obligatoires d'une ordonnance sont connus et stables : (a) peu de données étiquetées sont nécessaires, et (d) une ordonnance validée à tort peut avoir des conséquences graves, ce qui impose une vérification humaine.

## Données nécessaires
La liste des champs obligatoires d'une ordonnance, fournie par l'Ordre des pharmaciens.

## Métrique de succès
Taux d'ordonnances incomplètes détectées avant validation, cible 95 %.

## Conséquence d'une erreur
Une ordonnance incomplète validée à tort peut mettre le patient en danger.

## Risques éthiques ou de confidentialité (obligatoire)
Les données de santé sont sensibles : l'outil ne doit pas conserver les ordonnances.