# -*- coding: utf-8 -*-

import	pygame
import	os
import	time
import	sys

from	AudioTrack import *
from	BandMaster import *


# Create the Band master
oBandMaster = BandMaster()



# Infinite loop
while True:

	oBandMaster.CheckTracks()


	# Clear the  console screen
	os.system('cls')	# Windows version
	#os.system('clear')	# Linux version
	print "  _____                 _                             "
	print " |  __ \               | |                            "
	print " | |__) |__ _ _ __   __| | ___  _ __ ___              "
	print " |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \             "
	print " | | \ \ (_| | | | | (_| | (_) | | | | | |            "
	print " |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_|            "
	print "   ____                _____  _                       "
	print "  / __ \              |  __ \| |                      "
	print " | |  | | __ _  __ _  | |__) | | __ _ _   _  ___ _ __ "
	print " | |  | |/ _` |/ _` | |  ___/| |/ _` | | | |/ _ \ '__|"
	print " | |__| | (_| | (_| | | |    | | (_| | |_| |  __/ |   "
	print "  \____/ \__, |\__, | |_|    |_|\__,_|\__, |\___|_|   "
	print "          __/ | __/ |                  __/ |          "
	print "         |___/ |___/                  |___/           "
	print "                                Copyright 2016 - Okimi"
	print ""
	print oBandMaster.sReportStates()
	print ""
	print "Use Ctrl+C to exit this App."

	# Wait for 250ms
	pygame.time.delay(250)


