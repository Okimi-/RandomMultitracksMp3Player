# -*- coding: utf-8 -*-

import	pygame
import	os
import	time

from	AudioTrack import *
from	BandMaster import *



#
oBandMaster = BandMaster()

# Lecture d'un fichier 
sDirectory = os.getcwd() + "/ogg"
sound = pygame.mixer.Sound( sDirectory + "/1005.ogg" )
track = AudioTrack( sound, 1.0, False )


# Boucle en continue
while True:
	print track.bIsPlaying()
	# Wait for 250ms
	pygame.time.delay(250)
	
