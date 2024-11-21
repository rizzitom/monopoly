from Terrain import Terrain
from Case_speciale import Case_speciale
from Dictionnaire import prix_terrains

class Plateau:
    def __init__(self):
        self.liste_terrains = [
            [
                Case_speciale("Départ", action="gain_depart"),
                Terrain("Boulevard de Belleville", "marron", **prix_terrains.obtenir_prix("marron")),
                Terrain("Rue Lecourbe", "marron", **prix_terrains.obtenir_prix("marron")),
                Case_speciale("GM", action="prise_train"),  
                Terrain("Rue de Vaugirard", "bleu", **prix_terrains.obtenir_prix("bleu")),
                Terrain("Rue de Courcelles", "bleu", **prix_terrains.obtenir_prix("bleu")),
                Terrain("Avenue de la République", "bleu", **prix_terrains.obtenir_prix("bleu"))
            ],
            [
                Case_speciale("Prison", action="visite_prison"),
                Terrain("Boulevard de la Vilette", "rose", **prix_terrains.obtenir_prix("rose")),
                Terrain("Avenue de Neuilly", "rose", **prix_terrains.obtenir_prix("rose")),
                Terrain("Rue de Paradis", "rose", **prix_terrains.obtenir_prix("rose")),
                Terrain("Avenue de Mozart", "orange", **prix_terrains.obtenir_prix("orange")),
                Terrain("Boulevard de Saint-Michel", "orange", **prix_terrains.obtenir_prix("orange")),
                Terrain("Place Pigalle", "orange", **prix_terrains.obtenir_prix("orange"))
            ],
            [
                Case_speciale("Parc gratuit", action="repos"),
                Terrain("Avenue Matignon", "rouge", **prix_terrains.obtenir_prix("rouge")),
                Terrain("Boulevard Malesherbes", "rouge", **prix_terrains.obtenir_prix("rouge")),
                Terrain("Avenue Henri-Martin", "rouge", **prix_terrains.obtenir_prix("rouge")),
                Terrain("Faubourg Saint-Honoré", "jaune", **prix_terrains.obtenir_prix("jaune")),
                Terrain("Place de la Bourse", "jaune", **prix_terrains.obtenir_prix("jaune")),
                Terrain("Rue la Fayette", "jaune", **prix_terrains.obtenir_prix("jaune"))
            ],
            [
                Case_speciale("Allez en prison", action="aller_prison"),
                Terrain("Avenue de Breteuil", "vert", **prix_terrains.obtenir_prix("vert")),
                Terrain("Avenue Foch", "vert", **prix_terrains.obtenir_prix("vert")),
                Terrain("Boulevard Capucines", "vert", **prix_terrains.obtenir_prix("vert")),
                Case_speciale("GSL", action="prise_train"), 
                Terrain("Avenue des Champs", "violet", **prix_terrains.obtenir_prix("violet")),
                Terrain("Rue de la Paix", "violet", **prix_terrains.obtenir_prix("violet"))
            ]
        ]
        # 28 Cases au total

    def avoir_terrain_i_j(self, i, j):
        """
        Renvoie le terrain situé à la position (i, j) sur le plateau.
        """
        if i < 0 or i >= len(self.liste_terrains) or j < 0 or j >= len(self.liste_terrains[i]):
            return None
        return self.liste_terrains[i][j]
