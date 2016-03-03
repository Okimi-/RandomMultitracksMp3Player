# -*- coding: utf-8 -*-

# Retrouve la répertoire courant
#
http://www.developpez.net/forums/d1122205/autres-langages/python-zope/reseau-web/trouver-automatiquement-nom-repertoire-courant/

import  glob
import  random



class FichiersOgg():

    def __init__(self, repertoireDesFichiersOgg):

        # Attributs de la classe
        self.repertoireDesFichiersOgg = repertoireDesFichiersOgg

        # Liste et enregistre les fichiers .ogg dans le répertoire
        # http://python.developpez.com/faq/?page=Fichier#osListeFichiers
        self.fichiersOgg = glog.glob( repertoireDesFichiersOgg + """/*.ogg""" )



    def NombreDeFichiers():
        return len(self.fichiersOgg)



    def UnFichierAuHasard():

        n = self.NombreDeFichiers()
        if n == 0:  return ""

        return self.fichiersOgg[random.randint(0,n-1)]


