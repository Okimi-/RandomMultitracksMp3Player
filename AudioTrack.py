# -*- coding: utf-8 -*-

import	pygame



# Define AudioTrack class
# -----------------------
class AudioTrack:


	# Constructor
	# -----------
	# Initialise a new playing track
	def __init__( self, oSound, eVolume, bUpVolume ):

		# Attributes
		# ----------

		if bUpVolume :
			self.bVolumeIsUp = True
			eVolume = 100
		else :
			self.bVolumeIsUp = False

		# Play once the sound object
		self.oChannel = oSound.play(0)
		self.oChannel.set_volume( float(eVolume)/100 )



	# Methodes
	# --------

	# Return true if the Audio track is playing sound
	def bIsPlaying( self ):

		if self.oChannel.get_busy() == 1:
			return True
		else:
			return False


