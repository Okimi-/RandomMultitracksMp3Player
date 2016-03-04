# RandomMultitracksOggPlayer
Play randomly ogg files on 1 or more sound tracks.
--------------------------------------------------
This player was originaly creted for a multimedia art installation called "Le trou qui cri", for the In-Ouïe festival, in 2013, at La Roche-sur-Yon.  
This player use Python language (in 2.7) and PyGame library. It can works on Rasperry PI, Linux, OS-X and Windows systems.  
RandomOggPlayer use CeCILL-C licence

Who use it ?
------------

* In a directory, put all *.py files and /ogg directory,
* In the /ogg directory, put Ogg Vorbis audio files you want the player use,
* Start the player with the command python RandomOggPlayer.py

Parameters
----------

Change parameters in the Parameters.py file.

**iAudioTracksMax**  
Number of audio track the player can play. Value from 1 to 20.

**iHubbubQuantity**  
Hubbub quantity. Change the new audio stack creation frequency. Value from 1 to 100%. 0 for none.

**iHubbubVolume**  
Audio volume value for hubbub. Value from 1 to 100%

**iPumpUpQuantity**  
Change the Pump up the volume on a strack frequency. Value from 1 to 100%. 0 for none.

*Copyright Okimi (Emmanuel Fort), 2016 (contact at okimi dot net)*