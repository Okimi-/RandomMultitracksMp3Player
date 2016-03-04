# -*- coding: utf-8 -*-



import	glob
import	pygame
import	os
import	random

from	AudioTrack import *
from	Parameters import *



# Define BandMaster class
# -----------------------
class BandMaster :

	# Constructor
	# -----------
	# Initialise a new playing track
	def __init__( self ):

		# Initialize sound mixer
		pygame.mixer.init( frequency=22050, size=-16, channels=2, buffer=4096 )


		# Initialize max playing channels/tracks
		self.tabTracks = []
		pygame.mixer.set_num_channels( Parameters.iAudioTracksMax )
		for i in xrange( 0, Parameters.iAudioTracksMax ):
			self.tabTracks.append( None )


		# Get ogg files list
		sDirectory = os.getcwd() + "/" + Parameters.sOggFilesDirectory
		tabOggFiles = glob.glob( sDirectory + """/*.ogg""" )			# http://python.developpez.com/faq/?page=Fichier#osListeFichiers


		# Create Sound objects list
		self.tabAudios = []
		for sOggFile in tabOggFiles:
			oSound = pygame.mixer.Sound( sOggFile )
			self.tabAudios.append( oSound )


	# Methodes
	# --------
	def CheckTracks( self ) :

		# Check and free ended playing tracks
		self.FreeEndedTracks()

		# Check for free Track available
		iFreeTrackIndex = self.iGetFreeTrackIndex()
		if iFreeTrackIndex == -1:
			return

		# Start an new track ?
		if self.bIsCreatingNewTrack() == False :
			return

		oAudio = self.GetRandomAudio()
		
		# Create the audio track
		oTrack = AudioTrack( oAudio, Parameters.iHubbubVolume, self.bIsPumpUpTheVolume() )
		self.tabTracks[iFreeTrackIndex] = oTrack



	def FreeEndedTracks( self ) :

		# Check ended playing tracks
		for i in xrange( 0, len(self.tabTracks) ) :
			if self.tabTracks[i] is not None :
				if self.tabTracks[i].bIsPlaying() == False :
					# Free track if endend playing
					self.tabTracks[i] = None



	def bIsCreatingNewTrack( self ) :

		if Parameters.iHubbubQuantity == 0 :
			return False

		if random.randint( 1, 100 ) <= Parameters.iHubbubQuantity :
			return True

		return False



	def bIsPumpUpTheVolume( self ) :

		if Parameters.iPumpUpQuantity == 0 :
			return False

		# Is there an other Pump up track ?
		for oTrack in self.tabTracks :
			if oTrack is not None :
				if oTrack.bVolumeIsUp :
					return False

		if random.randint( 1, 100 ) <= Parameters.iPumpUpQuantity :
			return True

		return False



	def iGetFreeTrackIndex( self ) :

		for i in xrange( 0, len(self.tabTracks) ) :
			if self.tabTracks[i] is None :
				return i

		return -1



	def GetRandomAudio( self ) :

		return self.tabAudios[ random.randint( 0, len(self.tabAudios)-1 ) ]



	def sReportStates( self ) :

		sReport = ""

		for i in xrange( 0, len(self.tabTracks) ) :

			sTrackNumber = " " + str(i)
			sReport += "Track " + sTrackNumber[-2:] + " - "

			if self.tabTracks[i] is None :
				sReport += "None"
			else :
				sReport += "Playing"
				if self.tabTracks[i].bVolumeIsUp :
					sReport += " (Pump up the volume)"

			sReport += "\n"

		return sReport
