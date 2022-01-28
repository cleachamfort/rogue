# #on commence par créer le sac et une classe objets 

# class Sac:
#     def __init__(self,taille,capacite,contenu):
#         #contenu est une liste, la taille est le nb actuel d'elts dans le sac
#         self.taille = taille 
#         self.capacite = capacite
#         self.contenu = contenu
#     def isfull (self):
#         if self.taille>=self.capacite :
#             return ("Le sac est plein")
#     def add(self, objet):
#         if self.taille<self.capacite :
#             self.contenu.append(objet)
#             self.taille +=1
#         else : 
#             return ("Le sac est plein")
#     def jeter (self, objet):
#         if objet in self.contenu : 
#             self.contenu.remove(objet)
#             self.taille-=1
#         else : 
#             return ("Vous ne possédez pas l'objet")
    


# class Objet:
#     def __init__(self,nature,valeur,description,position):
#         self.nature = nature
#         self.valeur = valeur 
#         self.description = description
#         self.position = position
#     def manger(self):
#         if self.nature == "nourriture":
#             if np.add(perso.position,perso.direction)==self.position and #il ramasse:
#                 perso.satiete += self.valeur
#         else : 
#             return ("Ce n'est pas de la nourriture")
#     def boire(self):
#         if self.nature == "potion":
#             agir(self.valeur) #je dois implémenter la fn pour que agir marche
#             #les self.valeur vont être de classe magie 
#         else : 
#             return ("Ce n'est pas potable")
#     def attaquer(self,ennemi):
#         #une valeur d'arme est une liste ["flèche",valeur_degats]
#         if self.nature == "arme":
#             ennemi.vie-=self.valeur[1]
#         else : 
#             return ("Ceci n'est pas une arme")
#     def proteger(self):
#         if self.nature == "casque" or "armure":
#             if #un ennemi l'attaque:
#                 perso.vie += self.valeur
    
    
# class Piece(Objet):
#     def __init__(self,):
#         super(piece, self).__init__(nature,valeur,description)
#     def soudoyer(self, seuil):
#         #à partir du seuil, si la valeur en pièces est au dessus, on peut 
#         #soudoyer le gardien 
#         if self.valeur >=seuil : 
#             gardien.pop() #en vrai c'est pas une fonction mais il faut que le gardien disparaisse
#             self.valeur-=seuil
#         else : 
#             pass
#     def acheter(self,prix,objet,sac):
#         if self.valeur>=prix :
#             self.valeur-= prix
#             sac.add(sac,objet)
#         else : 
#             pass
