class Dictionnaire:
    def __init__(self):
        self.prix_terrains = {
            "marron": {"prix": 60, "loyer": 40, "cout_construction_maison": 100, "cout_construction_hotel": 500},
            "bleu": {"prix": 100, "loyer": 80, "cout_construction_maison": 100, "cout_construction_hotel": 500},
            "rose": {"prix": 140, "loyer": 120, "cout_construction_maison": 150, "cout_construction_hotel": 700},
            "orange": {"prix": 180, "loyer": 160, "cout_construction_maison": 150, "cout_construction_hotel": 700},
            "rouge": {"prix": 220, "loyer": 200, "cout_construction_maison": 200, "cout_construction_hotel": 900},
            "jaune": {"prix": 260, "loyer": 240, "cout_construction_maison": 200, "cout_construction_hotel": 900},
            "vert": {"prix": 300, "loyer": 280, "cout_construction_maison": 300, "cout_construction_hotel": 950},
            "violet": {"prix": 350, "loyer": 330, "cout_construction_maison": 350, "cout_construction_hotel": 1000},
        }

    def obtenir_prix(self, couleur):
        return self.prix_terrains.get(couleur)

prix_terrains = Dictionnaire()
