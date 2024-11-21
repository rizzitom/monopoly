from Terrain import Terrain
from random import randint


class Joueur:

    def __init__(self, nom, compte_initial=1500):
        self.nom = nom
        self.compte = compte_initial
        self.proprietes = []
        self.position = 0  
        self.en_faillite = False

    def tirer_de(self):
        return randint(1, 6)
    
    def choisir_terrains_a_vendre(self, montant_a_payer):
        terrains_a_vendre = []
        total_prix = 0

        while self.compte < montant_a_payer :
            print(f"{self.nom}, vous devez payer {montant_a_payer}€. Votre compte est à {self.compte}€. Montant à couvrir : {montant_a_payer - self.compte}€.")
            
            if not self.proprietes:
                print("Vous n'avez pas de terrains à vendre.")
                return []

            print("Terrains disponibles :")
            for index, terrain in enumerate(self.proprietes):
                prix_vente = terrain.prix * 0.8  # Le prix de vente est 80% du prix d'achat
                print(f"{index}: {terrain.nom} ({terrain.couleur}) - Prix de vente: {prix_vente}€")

            choix = input("Sélectionnez les terrains à vendre (séparés par des virgules) ou (taper : se rendre) : ")

            if choix.strip().lower() == "se rendre":
                self.en_faillite = True
                return # pas réussi à faire rendre

            try:
                indexes = [int(i.strip()) for i in choix.split(",")]
            except ValueError:
                print("Veuillez entrer des nombres valides.")
                continue

            terrains_a_vendre = [self.proprietes[i] for i in indexes if i < len(self.proprietes)]
            total_prix = sum(terrain.prix * 0.8 for terrain in terrains_a_vendre)

            if total_prix >= montant_a_payer - self.compte :
                break
            else:
                print(f"Le montant total des terrains sélectionnés est {total_prix}€, ce qui est inférieur à {montant_a_payer - self.compte}€. Veuillez sélectionner d'autres terrains.")

        for terrain in terrains_a_vendre:
            self.proprietes.remove(terrain)
            self.compte += terrain.prix * 0.8
            terrain.proprietaire = None
            print(f"{self.nom} a vendu {terrain.nom} pour {terrain.prix * 0.8}€.")

        return terrains_a_vendre

    def deplacement(self, de_resultat):
        self.position += de_resultat
        if self.position >= 24:  # Remplace 24 par le nombre total de cases du plateau
            self.position %= 24  # Revenir à une position valide

    def acheter(self, terrain):
        # Le joueur achète le terrain
        if self.compte >= terrain.prix and terrain.est_achetable():
            self.compte -= terrain.prix
            self.proprietes.append(terrain)
            terrain.proprietaire = self
            print(f"{self.nom} a acheté {terrain.nom} pour {terrain.prix}.")
        else:
            print(f"{self.nom} ne peut pas acheter {terrain.nom}.")

    def payer(self, terrain, autre_joueur):
        # Le joueur paye le loyer du terrain à un autre joueur
        if terrain.proprietaire and terrain.proprietaire != self:
            montant = terrain.loyer
            self.compte -= montant
            autre_joueur.compte += montant
            print(f"{self.nom} a payé {montant} à {autre_joueur.nom} pour {terrain.nom}.")

    def gerer_faillite(self, montant_a_payer):
        if self.compte < 0:
            print(f"{self.nom} est en faillite!")
            if not self.proprietes:  # Si le joueur n'a plus de propriétés -> essayer de faire écrire au joueur se rendre pour dire que le joueur est éléminée
                print(f"{self.nom} ne peut pas payer et n'a plus de terrains. Il est éliminé.")
                self.en_faillite = True
                return True
            else:
                self.vendre_terrains(self.proprietes)  # Essaie de vendre les propriétés
                if self.compte < montant_a_payer: 
                    print(f"{self.nom} ne peut pas se relever de la faillite.")
                    self.en_faillite = True
                    return True 
        return False

    def vendre_terrains(self, proprietes_a_vendre):
        montant_total = 0
        for propriete in proprietes_a_vendre:
            montant_total += propriete['valeur']
            self.proprietes.remove(propriete)
            print(f"{self.nom} a vendu {propriete['nom']}.")

        self.compte += montant_total
        print(f"{self.nom} a maintenant {self.compte}€ après la vente des terrains.")

    def declarer_faillite(self):
        self.en_faillite = True
        self.compte = 0
        self.proprietes.clear()
        print(f"{self.nom} est déclaré en faillite.")


#joueur1 = Joueur("J1")
#print(joueur1.nom)