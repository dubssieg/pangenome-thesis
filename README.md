# Logiciels développés durant la thèse

## [rs-pancat-compare (AGPL, Rust)](https://github.com/dubssieg/rs-pancat-compare)

Programme calculant la distance de segmentation entre deux fichiers GFA (\emph{Graphical Fragment Assembly}). Après identification les chemins communs entre les deux graphes, le programme lit ces chemins et énumère les différences de segmentation entre eux.
    
## [rs-pancat-paths (AGPL, Rust)](https://github.com/dubssieg/rs-pancat-paths)

Boîte à outils en ligne de commande permettant d'effectuer des actions telles que le renommage des chemins, l'extraction des régions partagées par un sous-ensemble de chemins, le calcul de la position des nœuds dans les chemins, le calcul des nœuds ancres et la suppression de génomes spécifiques d'un graphe.
    
## [pancat (AGPL, Python)](https://github.com/dubssieg/pancat)

Boîte à outils en ligne de commande, qui permet de parcourir, visualiser et comparer des graphes de variations. L'objectif de cet outil est de permettre de répondre à des questions techniques et biologiques sur ces structures de données. Il permet notamment de visualiser des paires de graphes avec leurs relations, extraire des sous-graphes, annoter des nœuds avec un système de positions.

## [gfagraphs (AGPL, Python)](https://github.com/dubssieg/gfagraphs)

Cette librairie a pour objectif d'offrir une couche d'abstraction au format de fichier GFA. Elle permet de charger, sauvegarder, modifier et annoter un fichier GFA. Écrite en Python, son objectif est d'offrir une classe Graph facile d'utilisation sur laquelle de nombreuses opérations peuvent être appelées.

## [sharepg (AGPL, Python)](https://github.com/dubssieg/sharepg)

Outil permettant d'analyser les séquences communes entre les populations dans les pangénomes. Ce petit outil en ligne de commande vise à vérifier les régions d'un graphe qui sont communes à un ensemble de génomes et qui ne sont pas traversées par un autre ensemble.
