
class Rectangle:

    def __init__(self , longueur , largeur):
        #Attribut 
        self.longueur = longueur
        self.largeur = largeur

    def Perimetre (self):
        return (int(self.longueur)*2) + (int(self.largeur)*2)

    def Air (self):
        return (int(self.longueur) * int(self.largeur))

    def EstCarre (self):
        if self.longueur == self.largeur:
            return True
        return False