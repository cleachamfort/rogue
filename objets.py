#on commence par créer le sac et une classe objets 

def class(sac):
    def __init__(self,taille,capacite,contenu):
        #contenu est une liste, la taille est le nb actuel d'elts dans le sac
        self.taille = taille 
        self.capacite = capacite
        self.contenu = contenu
    def isfull (self):
        if self.taille>=self.capacite :
            return ("Le sac est plein")
    def add(self, objet):
        if self.taille<self.capacite :
            self.contenu.append(objet)
            self.taille +=1
        else : 
            return ("Le sac est plein")
    def jeter (self, objet):
        if objet in self.contenu : 
            self.contenu.remove(objet)
            self.taille-=1
        else : 
            return ("Vous ne possédez pas l'objet")
    
def class(objet):
    def __init__(self,nature,valeur):
        self.nature = nature
        self.valeur = valeur 
    def manger(self):
        if self.nature == "nourriture":
            if #le personnage a fait l'action de ramasser et que tu es devant:
                perso.satiete += self.valeur