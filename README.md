
<h1 align="center">
  <br>
 <img src="http://www.miage.fr/wp-content/uploads/2020/02/MIAGE_LOGO-SEUL_COULEURS.png" alt="MIAGE" width="200">
    <br>
  CASTEX Nicolas & DAVAINE Louis-Amand
    <br>
</h1>

<h4 align="center">4TYE913U Données et intelligence artificielle :  REVERSI</h4>
  <br>

<p align="center">
  <a href="#key-features">Description</a> •
  <a href="#download">Points Forts</a> •
  <a href="#credits">Heuristiques</a> •
  <a href="#related">Structures de Données</a> •
  <a href="#license">Architecture du Projet</a>
</p>

<p align="center">
<img src="https://th.bing.com/th/id/R.5ac3f08cbe0822ac9d2db9993ae5801c?rik=L5gatnBOtzD%2f2A&riu=http%3a%2f%2fwww.bbcmicro.co.uk%2fgameimg%2fscreenshots%2f2648%2fDisc117-Reversi.jpg&ehk=d3Z3%2b9W9j7TZT6v10NLOGN2%2b%2ftIlmMUWZCr6jB2P%2byM%3d&risl=&pid=ImgRaw&r=0"></img>
</p>


## Description :

* ReversiMasterAI est une intelligence artificielle conçue pour le jeu de Reversi. Cette IA utilise une combinaison de techniques avancées pour optimiser ses performances.

* Évolution de notre IA :

  - Notre première version de l'IA utilisait uniquement l'algorithme Minimax sans élagage. Bien qu'elle fût capable de choisir des coups stratégiques, sa performance était limitée par le grand nombre de scénarios qu'elle devait évaluer, rendant l'IA moins efficace, surtout à des profondeurs de recherche élevées. En intégrant l'élagage Alpha-Beta, nous avons pu significativement augmenter la vitesse de l'IA tout en maintenant, voire en améliorant, la qualité des coups joués. Cette optimisation a été un tournant dans le développement de notre IA, la rendant non seulement plus rapide mais aussi plus stratégique et compétitive.

* Explications de MinMax avec Élagage :
 - Minimax est un algorithme de décision utilisé dans la théorie des jeux pour minimiser la perte potentielle dans un scénario de pire cas. Dans le contexte du Reversi, cela signifie choisir le coup qui maximise le potentiel de gain du joueur tout en minimisant l'avantage possible de l'adversaire.

 - L'élagage Alpha-Beta est une optimisation de Minimax qui élimine les branches de l'arbre de décision qui ne vont pas influencer la décision finale. Cela se fait en maintenant deux valeurs, Alpha et Beta :

 - Alpha représente la valeur minimale que le joueur maximisant est assuré.
 - Beta représente la valeur maximale que le joueur minimisant est assuré.

- Si, à un certain point, il est évident qu'une branche ne va pas influencer le résultat final (par exemple, si Alpha est supérieur à Beta), cette branche est coupée de l'arbre de recherche, ce qui réduit considérablement le nombre de scénarios à évalue
## Points Forts :

* Minimax avec Élagage Alpha-Beta :
  - Emploie un algorithme Minimax avec élagage alpha-beta pour évaluer les coups, permettant de réduire considérablement l'espace de recherche tout en trouvant les coups optimaux.

## Heuristiques :
* Différence de Pions :
  - Évalue la différence entre le nombre de pions du joueur et de l'adversaire.
* Contrôle des Coins :
  - Accorde une importance particulière à l'occupation des coins, essentiels dans Reversi.
* Stabilité :
  - Prise en compte de la stabilité des pions, favorisant ceux difficiles à capturer par l'adversaire.
* Mobilité :
  - Évalue le nombre de coups possibles pour augmenter la flexibilité et les options du joueur.
  
## Structures de Données :
* Utilisation de la classe Board pour la gestion de l'état du jeu.
* Gestion des coups et évaluation du plateau à travers la classe ReversiAI.

## Architecture du Projet :
* Classe Reversi :
  - Classe principale pour la gestion du jeu, non modifiée.
* Classe JoliReversi :
  - Utilisée pour tester l'IA avec une interface simplifiée.
* Classe ReversiAI :
  - Cœur de l'IA, implémentant Minimax avec élagage alpha-beta et heuristiques.
* Classes ReversiGameAIvsPlayer et ReversiGameAivsAi :
  - Permettent de jouer IA vs Joueur ou IA vs IA.
* Classe Main :
  - Interface pour choisir le mode de jeu.

