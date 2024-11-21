class Terrain:

    def __init__(self, nom, couleur, prix, loyer, cout_construction_maison, cout_construction_hotel):
        """
        Constructeur de Terrain
        """
        self.nom = nom
        self.couleur = couleur
        self.prix = prix
        self.loyer = loyer
        self.cout_construction_maison = cout_construction_maison
        self.cout_construction_hotel = cout_construction_hotel
        self.proprietaire = None
        self.nb_maisons = 0
        self.hotel = False
        

    def est_achetable(self):
        """
        Renvoie vrai si le terrain est achetable
        """        
        if self.proprietaire is None:
            return True
        else:
            print(f"{self.nom} appartient déjà à {self.proprietaire}.")
            return False

    def ameliorer_terrain(self, joueur):
        if self.proprietaire is None:
            print(f"{self.nom} n'appartient à personne.")
            return
        
        if self.proprietaire != joueur:
            print(f"{self.nom} n'est pas à vous.")
            return
        
        # Ajouter une maison si le joueur a assez d'argent
        if self.nb_maisons < 4:
            if joueur.compte >= self.cout_construction_maison:
                joueur.compte -= self.cout_construction_maison
                self.nb_maisons += 1
                print(f"Une maison a été ajoutée sur {self.nom}. Il y a maintenant {self.nb_maisons} maison(s).")
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour construire une maison sur {self.nom}.")
                
        # Construire un hôtel si le joueur a 4 maisons
        elif self.nb_maisons == 4 and not self.hotel:
            if joueur.compte >= self.cout_construction_hotel:
                joueur.compte -= self.cout_construction_hotel
                self.hotel = True
                self.nb_maisons = 0  # On ne peut plus avoir de maisons si on a un hôtel
                print(f"Un hôtel a été construit sur {self.nom}.")
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour construire un hôtel sur {self.nom}.")
        else:
            print(f"{self.nom} ne peut plus être amélioré.")


""" Test pour la couleur Bleur
couleur = "bleu"
details = prix_terrains.obtenir_prix(couleur)

if details:
    print(f"Détails pour {couleur} : {details}")
else:
    print(f"Couleur {couleur} non trouvée.")

"""