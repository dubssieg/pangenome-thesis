# Logiciels développés durant la thèse

## [rs-pancat-compare (AGPL, Rust)](https://github.com/dubssieg/rs-pancat-compare) [![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:712f1f12314ccdb07e054ceb85416a5e78684a85/)](https://archive.softwareheritage.org/swh:1:dir:712f1f12314ccdb07e054ceb85416a5e78684a85)

Programme calculant la distance de segmentation entre deux fichiers GFA (\emph{Graphical Fragment Assembly}). Après identification les chemins communs entre les deux graphes, le programme lit ces chemins et énumère les différences de segmentation entre eux.
    
## [rs-pancat-paths (AGPL, Rust)](https://github.com/dubssieg/rs-pancat-paths) [![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:a746f69ce3c70a577236ec779b729274552e870a/)](https://archive.softwareheritage.org/swh:1:dir:a746f69ce3c70a577236ec779b729274552e870a)

Boîte à outils en ligne de commande permettant d'effectuer des actions telles que le renommage des chemins, l'extraction des régions partagées par un sous-ensemble de chemins, le calcul de la position des nœuds dans les chemins, le calcul des nœuds ancres et la suppression de génomes spécifiques d'un graphe.
    
## [pancat (AGPL, Python)](https://github.com/dubssieg/pancat) [![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:f5395b90fcbf2ca90c59267f1611c2cdac14ccdf/)](https://archive.softwareheritage.org/swh:1:dir:f5395b90fcbf2ca90c59267f1611c2cdac14ccdf)

Boîte à outils en ligne de commande, qui permet de parcourir, visualiser et comparer des graphes de variations. L'objectif de cet outil est de permettre de répondre à des questions techniques et biologiques sur ces structures de données. Il permet notamment de visualiser des paires de graphes avec leurs relations, extraire des sous-graphes, annoter des nœuds avec un système de positions.

## [gfagraphs (AGPL, Python)](https://github.com/dubssieg/gfagraphs) [![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:e1853ed9abff88e2b40f23caa11bdf6c57f8a128/)](https://archive.softwareheritage.org/swh:1:dir:e1853ed9abff88e2b40f23caa11bdf6c57f8a128)

Cette librairie a pour objectif d'offrir une couche d'abstraction au format de fichier GFA. Elle permet de charger, sauvegarder, modifier et annoter un fichier GFA. Écrite en Python, son objectif est d'offrir une classe Graph facile d'utilisation sur laquelle de nombreuses opérations peuvent être appelées.

## [sharepg (AGPL, Python)](https://github.com/dubssieg/sharepg) [![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:eae23c8447a97bf8b13d6691ac97c5fbe755f415/)](https://archive.softwareheritage.org/swh:1:dir:eae23c8447a97bf8b13d6691ac97c5fbe755f415)

Outil permettant d'analyser les séquences communes entre les populations dans les pangénomes. Ce petit outil en ligne de commande vise à vérifier les régions d'un graphe qui sont communes à un ensemble de génomes et qui ne sont pas traversées par un autre ensemble.
