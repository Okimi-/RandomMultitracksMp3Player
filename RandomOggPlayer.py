# -*- coding: utf-8 -*-
"""RandomOggPlayer"""

import glob
import os
import pygame
import random

import PisteAudio



#
# Constantes
#

NOMBRE_DE_PISTES_SIMULTANEES = 5

# Volumes par défaut
VOLUME_DU_BROUHAHA = 0.3
VOLUME_DU_CRI = 1.0

QUANTITE_DE_BROUHAHA = 0.5
QUANTITE_DE_CRI = 0.2



#
# Variables globales
#
PISTES_AUDIO = []
SONS = []



##############################################################################
#
# Fonctions dédiés à la gestion des sons
#

def joue_un_son( son, volume ):
    """Joue un son"""
    canal = son.play()
    canal.set_volume( volume )
    return canal



# Vérifie si l'une des pistes audio est en mode crie
def Il_y_a_t_il_un_cri():
    """Sur l'ensemble des pistes audio, il a t'il une piste audio"""
    """qui est jouée comme un cri ?"""
    global PISTES_AUDIO
    for pisteAudio in PISTES_AUDIO:
        if pisteAudio.estUnCri:
            return True

    return False



def ResteTIlUnePisteAudioDisponible():
    """Reste t'il une piste audio disponible ?"""
    global PISTES_AUDIO
    for pisteAudio in PISTES_AUDIO:
        if pisteAudio is None:
            return True
    return False



def LanceUnDe( pourcentageDeVrai ):
    """Lance un dé"""
    if random.random() <= pourcentageDeVrai:
        return True
    return False



def UnSonAuHasard():
    global SONS
    return SONS[random.randint(0,SONS.count()-1)]



def VerificationDesPistesAudios():
    """Vérification des pistes audios"""
    global PISTES_AUDIO

    for pisteAudio in PISTES_AUDIO:
        if pisteAudio is not None:
            if not pisteAudio.canal.get_busy():
                # La lecture de ce canal audio est terminé, on libère le canal
                pisteAudio = None

        # Le tableau des pistes audio n'est pas remplis et le hasard est avec nous,
        # alors on crée une nouvelle piste audio
        if ResteTIlUnePisteAudioDisponible() and LanceUnDe( QUANTITE_DE_BROUHAHA ):
            pisteAudio = PisteAudio.PisteAudio()
            pisteAudio.son = UnSonAuHasard()
            pisteAudio.volume = VOLUME_DU_BROUHAHA
            pisteAudio.estUnCri = False
            # Cette nouvelle piste sera t'elle un cri ?
            if not Il_y_a_t_il_un_cri() and LanceUnDe(QUANTITE_DE_CRI):
                pisteAudio.volume = VOLUME_DU_CRI
                pisteAudio.estUnCri = True
                # Lance la lecture de la piste audio
                pygame.mixer.
#            pisteAudio.numéroDuCanal = Bass.Joue (pisteAudio.nomDuFichier, pisteAudio.volume);
#
#            this.pistesAudio[pisteAudioDisponible] = pisteAudio;














##############################################################################
#
# Main
#

# Initialise le mixer sonore
pygame.mixer.init( 44100, -16, 2, 4096 )
pygame.mixer.set_num_channels( NOMBRE_DE_PISTES_SIMULTANEES )


# Récupère la liste des fichiers ogg
fichiersOgg = glob.glob( os.getcwd() + """/ogg/*.ogg""" )
if fichiersOgg.count == 0:
    exit()


# Charge la liste des fichiers ogg
try:
    for fichierOgg in fichiersOgg:
        son = pygame.mixer.Sound( fichierOgg )
        son.set_volume( 1 )
        SONS.append( son )
except:
    raise UserWarning, "Erreur lors du chargment des fichiers ogg"


# Initialise les pistes audios
for i in xrange( 1, NOMBRE_DE_PISTES_SIMULTANEES ):
    PISTES_AUDIO.append( None )


