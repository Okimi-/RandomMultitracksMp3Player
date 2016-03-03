# -*- coding: utf-8 -*-

import	pygame



# Define AudioTrack class
# -----------------------
class AudioTrack:

	# Constructor
	# -----------
	# Initialise a new playing track
	def __init__( self, oSound, fVolume, bUpVolume ):

		# Attributes
		# ----------

		if bUpVolume:
			self.bVolumeIsUp = True
			fVolume = 1.0
		else:
			self.bVolumeIsUp = False

		# Play once the sound object
		self.oChannel = oSound.play(0)
		self.oChannel.set_volume( fVolume )


	# Methodes
	# --------

	# Return true if the Audio track is playing sound
	def bIsPlaying( self ):

		if self.oChannel.get_busy() == 1:
			return True
		else:
			return False


	def bIsVolumeIsUp( self ):

		if self.bVolumeIsUp():
			return True
		else:
			return False
