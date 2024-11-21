class Case_speciale:
    def __init__(self, nom, action):
        self.nom = nom
        self.action = action 

    def appliquer_action(self, joueur):
        """
        Applique l'action associée à la case spéciale.
        """
        if self.action == "gain_depart":
            joueur.compte += 200
            print(f"Votre nouveau solde de compte est de {joueur.compte} €")

        elif self.action == "visite_prison":
            cout = 25
            if joueur.compte >= cout:
                print(f"{joueur.nom} est en visite à la Prison. Vous payez la visite qui est de {cout}€.")
                joueur.compte -= cout
                print(f"Votre nouveau solde de compte est de {joueur.compte}")
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour payer la visite à la Prison.")

        elif self.action == "aller_prison":
            cout = 150
            if joueur.compte >= cout:
                print(f"{joueur.nom} va directement en prison. Vous payez une caution de {cout}€.")
                joueur.compte -= cout
                print(f"Votre nouveau solde de compte est de {joueur.compte}")
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour payer la caution.")

        elif self.action == "repos":
            print("")

        elif self.action == "prise_train":
            if self.nom == "GM":
                cout = 40
                if joueur.compte >= cout:
                    print(f"{joueur.nom} Vous êtes à la Gare Montparnasse, vous allez prendre le train qui coûte {cout}€")
                    joueur.compte -= cout
                    print(f"Votre nouveau solde de compte est de {joueur.compte}")
                else:
                    print(f"{joueur.nom} n'a pas assez d'argent pour prendre le train à la Gare Montparnasse.")

            elif self.nom == "GSL":
                cout = 70
                if joueur.compte >= cout:
                    print(f"{joueur.nom} Vous êtes à la Gare Saint Lazare, vous allez prendre le train qui coûte {cout}€.")
                    joueur.compte -= cout
                    print(f"Votre nouveau solde de compte est de {joueur.compte}")
                else:
                    print(f"{joueur.nom} n'a pas assez d'argent pour prendre le train à la Gare Saint Lazare.")
    
    def est_achetable(self):
        return False