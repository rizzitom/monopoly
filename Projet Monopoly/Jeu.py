from Joueur import Joueur
from Plateau import Plateau
from Partie import Partie

from random import randint

if __name__ == "__main__":

    # Création Partie
    nombre_joueurs = int(input("Entrez le nombre de joueurs (2 à 4) : "))
    while nombre_joueurs < 2 or nombre_joueurs > 4:
        nombre_joueurs = int(input("Veuillez entrer un nombre de joueurs valide (2-4) : "))

    liste_joueurs = []
    for i in range(nombre_joueurs):
        nom = input(f"Entrez le nom du joueur {i + 1} : ")
        while not nom.strip():
            nom = input("Le nom ne peut pas être vide. Veuillez entrer un nom : ")
        liste_joueurs.append(Joueur(nom))

    joueur_encours = randint(0, len(liste_joueurs) - 1)

    # Créer la partie
    partie = Partie(liste_joueurs)

    while True:
        joueur_actuel = liste_joueurs[joueur_encours]
        print("")
        print(f"Au tour de {joueur_actuel.nom} de jouer")
        print("")

        action = partie.choix_action(joueur_actuel)
        if action == "tirer_de":
            de_valeur = joueur_actuel.tirer_de()
            case_joueur = partie.deplacement(joueur_actuel)
            partie.traitement_post_deplacement(joueur_actuel, case_joueur)

        if hasattr(case_joueur, 'loyer') and case_joueur.proprietaire and case_joueur.proprietaire != joueur_actuel:
            # Le joueur doit payer le loyer
            if joueur_actuel.compte < case_joueur.loyer:
                print(f"{joueur_actuel.nom} n'a pas assez d'argent pour payer le loyer de {case_joueur.loyer}€!")
                
                # Proposer au joueur de vendre ses terrains
                terrains_a_vendre = joueur_actuel.choisir_terrains_a_vendre(case_joueur.loyer)
                montant_a_couvrir = case_joueur.loyer - joueur_actuel.compte 
                while montant_a_couvrir > 0:
                    terrains_a_vendre = joueur_actuel.choisir_terrains_a_vendre(montant_a_couvrir)
                    montant_total = 0
                    for terrain in terrains_a_vendre:
                        montant_vente = terrain.prix * 0.8 
                        montant_total += montant_vente
                        joueur_actuel.proprietes.remove(terrain)  # Retirer le terrain de la liste du joueur
                        joueur_actuel.compte += montant_vente
                        print(f"{joueur_actuel.nom} a vendu ses terrains pour un total de {montant_total}€.")
                
                    joueur_actuel.compte += montant_total
                    print(f"{joueur_actuel.nom} a maintenant {joueur_actuel.compte}€ après la vente des terrains.")

                    montant_a_couvrir = case_joueur.loyer - joueur_actuel.compte

                    if montant_a_couvrir > 0:
                        print(f"Il manque encore {montant_a_couvrir}€ pour payer le loyer.")
                    else:
                        print(f"{joueur_actuel.nom} a maintenant assez d'argent pour payer le loyer.")
                
                joueur_actuel.compte -= case_joueur.loyer
                case_joueur.proprietaire.compte += case_joueur.loyer
                print(f"{joueur_actuel.nom} fait donc un virement paypal à {case_joueur.proprietaire.nom} pour un montant de {case_joueur.loyer}€.")
                print(f"Le nouveau solde de {joueur_actuel.nom} est de {joueur_actuel.compte}")
                print(f"Nouveau solde de {case_joueur.proprietaire.nom} : {case_joueur.proprietaire.compte}€.")


        joueurs_restants = [joueur for joueur in liste_joueurs if not joueur.en_faillite]
        if len(joueurs_restants) == 1:
            print(f"{joueurs_restants[0].nom} a gagné la partie !")
            print("Fin de la partie !")
            break

        # Passer au joueur suivant
        joueur_encours = partie.prochain_joueur(joueur_encours)





