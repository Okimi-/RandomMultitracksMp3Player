# -*- coding: utf-8 -*-

import	pygame
import    random

import    Parametres



class ChefDOrchestre(object):

    # Constructeur
    def __init__(self, fichiersOgg):

        self.fichiersOgg = fichiersOgg

        # Initialise la liste des pistes audios
        self.pistesAudio = []
        for i in xrange( 1, Parametres.NOMBRE_DE_PISTES_SIMULTANEES ):
            self.pistesAudio.append( None )



    def	IlYATIlUnCri(self):

        """Vérifie si l'une des pistes audio est en mode crie"""

        for pisteAudio in self.pistesAudio:
            if pisteAudio.estUnCri:
                return true

        return false



    def	LanceUnDé(pourcentageDeVrai):

        if random.random() <= pourcentageDeVrai :
            return true

        return false



    def    ResteTIlUnePisteAudioDisponible():

        for pisteAudio in self.pistesAudio:
            if pisteAudio is None:
                return pisteAudio



        return None;



	def	VerificationDesPistesAudios():
	{
        for pisteAudio in self.pistesAudio:
            if pisteAudio is not None:
                pisteAudio.positionDeLaLecture =


		// Vérification sur les pistes audio terminées
		for (int i = 0; i<NOMBRE_MAXIMUM_DE_PISTE_AUDIO; i++) {
			if (this.pistesAudio [i] != null) {

				// Calcul la position de la tete de lecture
				this.pistesAudio [i].positionDeLaLecture = Bass.Position (this.pistesAudio [i].numéroDuCanal);

				if (this.pistesAudio [i].positionDeLaLecture == 1) {

					// La lecture de la piste audio est terminée, on libère la ressource
					Bass.Libère (this.pistesAudio [i].numéroDuCanal);

					this.pistesAudio[i] = null;
				}

			}
		}


    		// Le tableau des pistes audio n'est pas remplis et le hasard est avec nous, alors on crée une nouvelle piste audio
    		pisteAudioDisponible = ResteTIlUnePisteAudioDisponible ();
    		if ( (pisteAudioDisponible!=-1)  && LanceUnDé(this.quantitéDeBrouhaha) )
    		{
    			pisteAudio = new PisteAudio ();
    			pisteAudio.nomDuFichier = this.fichiersOgg.UnFichierAuHasard ();
    			pisteAudio.nomDuFichierCourt = Path.GetFileName (pisteAudio.nomDuFichier);
    			pisteAudio.volume = this.volumeBrouhaha;
    			pisteAudio.estUnCri = false;
    			pisteAudio.positionDeLaLecture = 0.0f;

    			// Cette nouvelle piste sera t'elle un cri ?
    			if ( !IlYATIlUnCri() && LanceUnDé(this.quantitéDeCri) )
    			{
    				pisteAudio.volume = this.volumeCri;
    				pisteAudio.estUnCri = true;
    			}

    			// Lance la lecture de la piste audio
    			pisteAudio.numéroDuCanal = Bass.Joue (pisteAudio.nomDuFichier, pisteAudio.volume);

    			this.pistesAudio[pisteAudioDisponible] = pisteAudio;
    		}

		System.Threading.Thread.Sleep (250);
		Console.SetCursorPosition (0, 12);
		Console.WriteLine ("             ");

	}