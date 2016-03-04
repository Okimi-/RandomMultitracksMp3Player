# -*- coding: utf-8 -*-

#
# Copyright. Okimi, 2016, contact at okimi dot net
# 
# Ce logiciel est un programme informatique servant à [rappeler les
# caractéristiques techniques de votre logiciel]. 
# 
# Ce logiciel est régi par la licence CeCILL-C soumise au droit français et
# respectant les principes de diffusion des logiciels libres. Vous pouvez
# utiliser, modifier et/ou redistribuer ce programme sous les conditions
# de la licence CeCILL-C telle que diffusée par le CEA, le CNRS et l'INRIA 
# sur le site "http://www.cecill.info".
# 
# En contrepartie de l'accessibilité au code source et des droits de copie,
# de modification et de redistribution accordés par cette licence, il n'est
# offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
# seule une responsabilité restreinte pèse sur l'auteur du programme,  le
# titulaire des droits patrimoniaux et les concédants successifs.
# 
# A cet égard  l'attention de l'utilisateur est attirée sur les risques
# associés au chargement,  à l'utilisation,  à la modification et/ou au
# développement et à la reproduction du logiciel par l'utilisateur étant 
# donné sa spécificité de logiciel libre, qui peut le rendre complexe à 
# manipuler et qui le réserve donc à des développeurs et des professionnels
# avertis possédant  des  connaissances  informatiques approfondies.  Les
# utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
# logiciel à leurs besoins dans des conditions permettant d'assurer la
# sécurité de leurs systèmes et ou de leurs données et, plus généralement, 
# à l'utiliser et l'exploiter dans les mêmes conditions de sécurité. 
# 
# Le fait que vous puissiez accéder à cet en-tête signifie que vous avez 
# pris connaissance de la licence CeCILL-C, et que vous en avez accepté les
# termes.
# 
# 
# 
# Copyright. Okimi, 2016, contact at okimi dot net
# 
# This software is a computer program whose purpose is to [describe
# functionalities and technical features of your software].
# 
# This software is governed by the CeCILL-C license under French law and
# abiding by the rules of distribution of free software.  You can  use, 
# modify and/ or redistribute the software under the terms of the CeCILL-C
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info". 
# 
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability. 
# 
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or 
# data to be ensured and,  more generally, to use and operate it in the 
# same conditions as regards security. 
# 
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL-C license and that you accept its terms.
#



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
