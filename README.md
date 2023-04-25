# Cranaruge

## Contexte du projet

**Cranaruge** est le robot Discord de HeroFactory#0311 ([HeroFactory16](https://github.com/herofactory16) sur GitHub). Initialement un projet personnel, il s'incrit aujourd'hui dans le cadre du projet de développement de deuxième année en informatique à Lyon Ynov Campus.

## Cible

Ce robot a pour vocation de servir en premier lieu sur le [serveur Discord communautaire](https://discord.gg/f77VwBX5w7) de la **[Mogapédia](http://fr.mogapedia.wikia.com/wiki/Monster_Hunter_Wiki)**, principal Wiki Monter Hunter francophone. Il devra permettre aux utilisateurs de profiter d'une base de données liée au jeu **[Monster Hunter Frontier Z Zenith](http://fr.mogapedia.wikia.com/wiki/Monster_Hunter_Frontier_Z_Zenith)** (ci-après, "MHFZZ"), un MMO exclusif au Japon, à la Corée du Sud et à la Chine, ayant fermé ses portes en 2019.

## Cahier des charges et objectifs

La base de données de MHFZZ dont nous disposons a été scrappée à partir du [Ferias English Project](https://xl3lackout.github.io/MHFZ-Ferias-English-Project/), un site contenant l'intégralité des données du jeu, partiellement traduites en anglais, dans un format plutôt chaotique. Dans le délai imposé par le projet de développement, nous avons pris le parti de nous concentrer sur les armes présentes dans le jeu. En d'autres termes, un utilisateur doit, par une simple commande, être en mesure d'accéder aux données qui ont été scrappées puis enregistrées dans notre propre base de données. Ces données comprennent le nom, l'attaque, les attributs spéciaux, le taux de coups critiques, le nombre d'emplacements de décorations, la rareté, le rang, le prix, les matériaux de création et les matériaux d'amélioration de chacune des armes.

## Difficultés techniques

Très rapidement, nous nous sommes heurtés à deux obstacles majeurs : le scrapping, et la mise en ligne du robot. Le premier point, malgré qu'il soit bien documenté, est une discipline complexe qui nécessite entre autres une bonne connaissance de la structure des pages web. Le second point, moins bien documenté, a nécessité l'utilisation de moyens détournés absents de la documentation officielle de l'API Discord. En outre, l'exploitation des données a été complexifiée par leur traduction partielle : beaucoup de caractères étaient toujours en japonais, notamment au niveau des descriptions des armes qui n'ont pas du tout été traduites.

## Tester le robot

Afin de tester le robot, il faut se rendre sur le [serveur de test](https://discord.gg/3C2HQMbJUv). Les commandes de Cranaruge liées au projet de développement peuvent être appelées en tapant ``/mhfzzweapon`` ou ``/mhfzzweaponname``.
- ``/mhfzzweapon`` prend un argument obligatoire (le type d'arme recherché) ainsi que jusqu'à 4 arguments optionnels (l'élément, l'affinité, les matériaux et la rareté), et va renvoyer la liste des armes correspondant aux critères saisis.
- ``/mhfzzweaponname`` prend deux arguments obligatoires, le type d'arme et une entrée utilisateur correspondant au nom. Cette commande va effectuer une recherche qui affichera la ou les armes dont le nom contient le texte entré par l'utilisateur.

Ces commandes sont utilisables par n'importe quel utilisateur, quelles que soient ses permissions.

Attention, Cranaruge contient aussi d'autres commandes plus ou moins fonctionnelles, mais non liées au projet de développement, y compris ``/mhfzzhelp`` et ``/mhfzzinstall``.