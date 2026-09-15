# Projet Streamlit

## Consignes

1. Trois filtres au moins : championnat, poste, et un seuil numérique (OVR ou PAC).
2. Un bandeau de chiffres clés qui se met à jour : nombre de joueurs sélectionnés, moyennes.
3. Trois graphiques de familles différentes, chacun justifié en une phrase dans l'interface : une distribution (histogramme), une comparaison de groupes (boxplot ou barplot), une relation (nuage de points).
4. Un tableau des meilleurs profils, trié.
5. Un README de 15 lignes : la question métier, les choix de graphiques et pourquoi, une limite du dataset.

## Explications

### 1. Trois filtres au moins : championnat, poste, et un seuil numérique (OVR ou PAC).
Les filtres sont présents sur la page `analyse` de l'application Sreamlit. Ils se composent d'une sélection d'un seul ou de tous les championnats de football que l'on souhaite analyser, d'une sélection d'un seul ou de tous les postes ainsi que deux seuils numériques pour la performance globale du joueur (OVR) et de sa vitesse (PAC) à l'aide d'une sidebar allant du min au max de chacune de ces métriques. 

### 2. Un bandeau de chiffres clés qui se met à jour : nombre de joueurs sélectionnés, moyennes.
Sur la page `dataset`, les chiffres clés montrent le nombre total de joueurs, nationnalités, championnats et postes représentées par ces joueurs, présents dans le jeu de données (sans filtre).

Sur la page `analyse`, les chiffres clés montrent de façon dynamique le nombre total de joueurs sélectionnés qui respectent les filtres indiqués par l'utilisateur ainsi que la moyenne globale de chaque métrique (OVR, PAC, SHO, PAS, DRI, DEF, PHY).

### 3. Trois graphiques de familles différentes, chacun justifié en une phrase dans l'interface : une distribution (histogramme), une comparaison de groupes (boxplot ou barplot), une relation (nuage de points).

Sur la page `analyse`, on a trois types de graphes dynamiques en fonction des filtres indiqués par l'utilisateur :
- distribution des performances (OVR) des joueurs répondant aux critères ;
- comparaison des performances (OVR) des joueurs selon le poste qu'ils occupent ;
- relation entre la qualité de passe (PAS) du joueurs et sa qualité de dribbles (DRI).

### 4. Un tableau des meilleurs profils, trié.

Sur la page `analyse`, on a un tableau dynamique du top 10 des joueurs respectant la sélection de l'utilisateur.
Sur la page `meilleurs profils`, on a : 
- un tableau statique du top 10 des meilleurs joueurs selon leur perfomance globale (OVR) ;
- un tableau dynamique du top 10 des joueurs selon une qualité.

### 5. Un README de 15 lignes : la question métier, les choix de graphiques et pourquoi, une limite du dataset.

Le point de vue métier est par exemple de faire une étude de marché pour le prochain mercato et facilité le recrutement de joueurs en fonction des qualités recherchées par le club. 

Les graphes permettent d'avoir une vision d'ensemble des joueurs FIFA. En effet, on regarder la tendance générale des performances de l'ensemble des joueurs qui peut varier en fonction du nombre de sélections faites en club durant un championnat. En regardant sur un poste clé recherché, on peut avoir un ordre d'idée de la performance en générale de l'ensemble des joueurs et voir s'il y a une relation sur la qualité de passe et de dribble des joueurs sélectionnés. Un autre graphe présent sur la page `meilleurs profils`permet de sélectionner deux joueurs et de comparer de façon visuelle leurs statistiques de performance à l'aide d'un diagramme radar.

Une des limites du dataset est que pour faire une réelle étude de marché. Il faut avoir conscience de la valeur marchande du joueur. Une solution proposée est de se connecter par appel API à `PlayerElo`, afin d'établir une correspondance entre le nom des joueurs et leur coût.