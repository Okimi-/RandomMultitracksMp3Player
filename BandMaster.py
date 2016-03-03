# -*- coding: utf-8 -*-



import	pygame
import	os

from	Parameters import *



# Define BandMaster class
# -----------------------
class BandMaster:

	# Constructor
	# -----------
	# Initialise a new playing track
	def __init__( self ):

		# Initialize sound mixer
		pygame.mixer.init( frequency=22050, size=-16, channels=2, buffer=4096 )

		# Initialize max playing channels
		pygame.mixer.set_num_channels( Parameters.iAudioTracksMax )


		# Get ogg files list
		sDirectory = os.getcwd() + "/" + Parameters.sOggFilesDirectory


	# Methodes
	# --------
