from Plateau import Plateau
from Terrain import Terrain
from Joueur import Joueur
from Case_speciale import Case_speciale

class Partie:
    def __init__(self, liste_joueurs):
        self.liste_joueurs = liste_joueurs
        self.plateau = Plateau()
        self.joueur_actuel = 0
        self.partie_terminee = False

    def avoir_joueur_avec_nom(self, nom):
        """
            Renvoie le joueur ayant pour nom nom
        """
        for joueur in self.liste_joueurs:
            if joueur.nom == nom:
                return joueur

    def choix_action(self, joueur):
        while True:
            print("Que voulez-vous faire ?")
            print("1: Tirer le dé")
            print("2: Consulter mon Compte")
            print("3: Voir sur quelle case je suis")
            print("4: Voir mes terrains")
            
            choix =input("Votre Choix : ")
            
            if choix.strip() == "" or not choix.isdigit():
                print("Choix incorrect. Veuillez entrer un numéro entre 1 et 4.")
                continue  

            choix = int(choix)  
            
            if choix == 1:
                return "tirer_de"
            
            elif choix == 2:
                print(f"{joueur.nom} a {joueur.compte} sur son compte")
                continue
            
            elif choix == 3:
                self.voir_case(joueur)
                continue

            elif choix == 4:
                self.afficher_terrains_joueur(joueur)
                continue

            else:
                print("Choix invalide, veuillez réessayer.")

    def voir_case(self, joueur):
        i = joueur.position // 6
        j = joueur.position % 6 

        case = self.plateau.liste_terrains[i][j]

        if case is not None:
            print(f"Vous êtes sur : {case.nom}")
        else:
            print("Cette case n'existe pas.")

    def deplacement(self, joueur):
        de_resultat = joueur.tirer_de()
        print(f"{joueur.nom} a fait {de_resultat} avec le dé.")
        
        position_initiale = joueur.position  
        joueur.deplacement(de_resultat) 

        case_arrivee = self.plateau.avoir_terrain_i_j(joueur.position // 6, joueur.position % 6)

        if case_arrivee is None:
            print("Erreur : case_arrivee est None.")
            return None

          # Vérifie si le joueur a fait un tour complet
        if joueur.position < position_initiale: 
            montant_gain = 200 
            joueur.compte += montant_gain
            print(f"{joueur.nom} a fait un tour de terrain et reçoit {montant_gain} €")
        
        print(f"{joueur.nom} est maintenant sur {case_arrivee.nom}")  
        return case_arrivee

    def traitement_post_deplacement(self, joueur, case):
        """
            Une fois que le joueur s'est déplacé, fait le traitement (cf. le sujet)
            
             Aide : isinstance(case, Terrain) -> True si case est de la classe Terrain, False sinon
        """
        if isinstance(case, Terrain):
            if case.proprietaire is None:
                if joueur.compte >= case.prix:
                    print(f"Le Terrain est disponible à l'achat pour {case.prix} ")
                    achat = input(f"Voulez-vous acheter {case.nom} pour un montant de {case.prix} (1 = Oui / 0 = Non) ? ")
                    if achat == "1":
                        joueur.acheter(case)
                        case.proprietaire = joueur
                        print(f"La propriété {case.nom} est maintenant détenue par {joueur.nom}")
                    else:
                        print(f"{joueur.nom} n'a pas acheté la propriété")
                else: 
                    print(f"{joueur.nom} n'a pas assez d'argent pour acheter la propriété.")
            else:
                if case.proprietaire != joueur:
                    montant_loyer = case.loyer
                    if joueur.compte >= montant_loyer:
                        joueur.compte -= montant_loyer
                        case.proprietaire.compte += montant_loyer
                        print(f"{joueur.nom} paie {montant_loyer}€ de loyer à {case.proprietaire.nom} pour {case.nom}.")
                    else:
                        self.gestion_faillite(joueur)
                else:
                    self.gerer_amelioration(joueur, case)
        
        elif isinstance(case, Case_speciale):
            case.appliquer_action(joueur)

    def gestion_faillite(self, joueur):
        while joueur.compte < 0 and joueur.terrains:
            print(f"{joueur.nom}, vous n'avez pas assez d'argent pour payer.")
            print(f"Votre compte est à {joueur.compte}€.")
        
            choix = input(f"Voulez-vous vendre un terrain pour éviter la faillite ? (oui/non) ").lower()
        
            if choix == "oui":
                print("Voici vos terrains :")
                for i, terrain in enumerate(joueur.terrains):
                    print(f"{i + 1}: {terrain.nom} - Prix d'achat : {terrain.prix_achat}€")

                # Sélection du terrain à vendre
                choix_terrain = int(input("Entrez le numéro du terrain que vous souhaitez vendre : ")) - 1
            
                if 0 <= choix_terrain < len(joueur.terrains):
                    terrain_a_vendre = joueur.terrains[choix_terrain]
                    montant_vente = terrain_a_vendre.prix_achat * 0.8
                    joueur.compte += montant_vente
                    joueur.terrains.remove(terrain_a_vendre)
                    print(f"{joueur.nom} a vendu {terrain_a_vendre.nom} pour {montant_vente}€.")
                    print(f"Votre nouveau solde est de {joueur.compte}€.")
                else:
                    print("Choix invalide.")
            else:
                print(f"{joueur.nom} a décidé de ne pas vendre de terrains.")
                break

        if joueur.compte < 0:
            print(f"{joueur.nom} est en faillite et quitte la partie.")
            self.liste_joueurs.remove(joueur)
            self.verifier_fin_partie()
                
            # Vérifier si la partie doit se terminer
            self.verifier_fin_partie()


    def verifier_fin_partie(self):
        if len(self.liste_joueurs) == 1:
            gagnant = self.liste_joueurs[0]
            print(f"Le jeu est terminé ! {gagnant.nom} a gagné.")
            self.partie_terminee = True
    
    def gerer_amelioration(self, joueur, case):
        if case.nb_maisons < 4:
            if joueur.compte >= case.cout_construction_maison:
                choix = input(f"Voulez-vous construire une maison sur {case.nom} pour {case.cout_construction_maison} (1 = Oui / 0 = Non) ? ")
                if choix == "1":
                    joueur.compte -= case.cout_construction_maison
                    case.ameliorer_terrain(joueur)
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour construire une maison.")
        elif not case.hotel:
            if joueur.compte >= case.cout_construction_hotel:
                choix = input(f"Voulez-vous construire un hôtel sur {case.nom} pour {case.cout_construction_hotel} (1 = Oui / 0 = Non) ? ")
                if choix == "1":
                    joueur.compte -= case.cout_construction_hotel
                    case.ameliorer_terrain(joueur)
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour construire un hôtel.")
        else:
            print(f"{joueur.nom} a déjà construit un hôtel sur {case.nom}.")    


    def tour(self, joueur):
        
        print(f"\nTour de {joueur.nom}")

        if joueur.en_faillite:
            print(f"{joueur.nom} est en faillite et ne peut pas jouer.")
            return  # Ne pas continuer le tour
    
        while True:  # Tant que le joueur n'a pas tiré le dé
            action = self.choix_action(joueur)
            if action == "tirer_de":
                case_joueur = self.deplacement(joueur)
                self.traitement_post_deplacement(joueur, case_joueur)
                break 

            if action == "se rendre":
                joueur.en_faillite = True
                print(f"{joueur.nom} a choisi de se rendre. Il est maintenant en faillite.")
                return  

    def prochain_joueur(self, joueur_encours):
        # Passe au joueur suivant
        joueur_encours += 1
        if joueur_encours >= len(self.liste_joueurs):
            joueur_encours = 0 
        return joueur_encours
    
    def afficher_terrains_joueur(self, joueur):
        """Affiche la liste des terrains possédés par le joueur"""
        if joueur.proprietes:
            print(f"{joueur.nom} possède les terrains suivants :")
            for terrain in joueur.proprietes:
                print(f"- {terrain.nom} {terrain.couleur} (Prix d'achat : {terrain.prix} et le loyer coute : {terrain.loyer}) il possède {terrain.nb_maisons} Maisons | A-t-il un hôtel ? : ", end="")
                if terrain.hotel:
                    print("Oui")
                else:
                    print("Non")

        else:
            print(f"{joueur.nom} ne possède aucun terrain.")

    def calculer_terrain(self, joueur, de_value):
        """
        Calcule le terrain sur lequel le joueur va atterrir
        après avoir tiré le dé.
        """
        nouvelle_position = joueur.position + de_value
        if nouvelle_position >= len(self.plateau.liste_terrains) * 6:  
            nouvelle_position %= len(self.plateau.liste_terrains) * 6  
            return self.plateau.avoir_terrain_i_j(nouvelle_position // 6, nouvelle_position % 6)
        
    def verifier_etat_joueurs(self):
        joueurs_en_vie = [joueur for joueur in self.joueurs if not joueur.en_faillite]

        if len(joueurs_en_vie) < 2:  
            gagnant = joueurs_en_vie[0] if joueurs_en_vie else None
            if gagnant:
                print(f"{gagnant.nom} a gagné la partie!")
            else:
                print("Tous les joueurs sont en faillite. La partie est terminée.")
            return True  
        return False 

    def jouer_tour(self, joueur):
        """Logique du tour pour un joueur."""
        if not self.partie_terminee: 
            print(f"Tour de {joueur.nom}")
            
            joueur.lancer_de()

        if joueur.compte < 0:
            print(f"{joueur.nom} est en faillite et quitte la partie.")
            self.liste_joueurs.remove(joueur)
            self.verifier_fin_partie()