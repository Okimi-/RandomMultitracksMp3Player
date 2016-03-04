# RandomMultitracksOggPlayer
Lecteur aléatoire de fichier ogg sur une ou plusieurs pistes audio simultanées.
-------------------------------------------------------------------------------
Ce lecteur a été initialement crée pour une oeuvre d'art contemporain appellée "Le trou qui cri", lors du festival In-Ouïe, à La Roche-sur-Yon, en 2013.  
Ce lecteur est développé à l'aide du language Python (version 2.7) et de la librairie logiciel PyGame, pour fonctionner sur carte Raspberry PI.  
RandomOggPlayer est distribué sous licence CeCILL-C

Comment l'utiliser ?
--------------------

Il faut vérifier les pré-requis suivants :
* Avoir Python et la librairie PyGame, installés sur le système qui va exécuter RandomOggPlayer,

Installation
------------

* Dans un répertoire de votre choix, mettre les fichier *.py et le répertoire /ogg
* Dans le répertoire /ogg, placer les fichiers Ogg vorbis qui seront joués par le player
* Exécuter la commande python RandomOggPlayer.py

Paramétrage
-----------

Vous pouvez intervenir sur le paramétrage du player en modifiant les valeurs du fichier Parameters.py

**iAudioTracksMax**  
Nombre de piste audio jouées simultanément. Valeur de 1 à 20.

**iHubbubQuantity**  
Quantité de bruit de fond. Agit sur la fréquence de création de nouvelles pistes audios. Valeur de 1 à 100%. 0 pour aucun.

**iHubbubVolume**  
Volume sonore du bruit de fond. Valeur de 1 à 100%

**iPumpUpQuantity**  
Agit sur la fréquence d'apparition de piste audio où le volume au maximum. Valeur de 1 à 100%. 0 pour aucun.

*Copyright Okimi (Emmanuel Fort), 2016 (contact at okimi dot net)*
