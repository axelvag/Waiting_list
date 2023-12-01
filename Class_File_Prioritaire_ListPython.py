# -*- coding: utf-8 -*-
"""
@author: david Granjon
"""

# *******************************************************************************************************************************
# ----------------------------------  CREATION D'UNE STRUCTURE DE TYPE FILE PRIORITAIRE --------------------------------------
# *******************************************************************************************************************************

class FilePrioritaire:
    '''Classe définissant une structure de données de type File Prioritaire avec méthodes
    Cette classe utilise les tableaux dynamiques (listes python): Liste de tuples (priorité,info)
    La priorité doit être un entier, et l'info de n'importe quel type
    Plus la valeur de la priorité est faible, plus l'info est prioritaire'''
    
    def __init__(self,uneListe=[]):
        '''Méthode "Constructeur": Construit l'instance et initialise les attributs'''
        self.elements=list(uneListe)
    
    def __str__(self):
        '''Méthode qui personnalise l'affichage par un print de la file prioritaire (Surcharge de l'affichage)'''
        if self.estVide():
            return "File vide !!"
        else:
            chaine="File Prioritaire: "
            for elem in self.elements:
                chaine += eval("f'{elem}  '")
            return chaine
       
    def __del__(self):
        '''Surcharge de la méthode destruction'''
        self.vider()
        return "File prioritaire détruite"    
    
    def _valide(self, elem):
        '''Méthode privée (pas sensée être appelée par l'utilisateur de la classe)
        Cette méthode permet de garantir que le format tuple(entier,string) est respecté,
        ainsi que la valeur de la priorité qui doit être dans la plage [1 à 5]
        Elle prend une variable en entrée et renvoie True si le format attendu est convenable,
        ou False sinon'''
        if (type(elem) is tuple and type(elem[0]) is int and type(elem[1]) is str):
            return (len(elem)==2 and elem[0]>=1 and elem[0]<=5)
        return False
        
    def estVide(self):
        '''Méthode qui teste si la file prioritaire est vide: renvoie True si vide, False sinon'''
        return len(self.elements)==0
    
    def enfiler(self, elem):
        '''Méthode qui insère au bon endroit dans la liste prioritaire un couple (priorité,info), en fonction de sa priorité.
        La priorité est un entier de [1 à 5], plus sa valeur est faible, plus l'info est prioritaire'''
        if self._valide(elem):
            if self.estVide():
                self.liste.append(elem)
            else:
                priorite=infoAInserer[0]
                cell=self.dern
                while (cell and priorite < cell.info[0]):
                    cell=cell.precedent
                if not cell:                        # Ajout en tête de File prioritaire (Liste doublement chainée)
                    cellSuiv=self.prem
                    self.prem=cellSuiv.precedent=cellule(infoAInserer,cellSuiv,None)
                elif not cell.suivant:              # Ajout en fin de File prioritaire (Liste doublement chainée)
                    cellPrec=self.dern
                    cellPrec.suivant=self.dern=cellule(infoAInserer,None,cellPrec)         
                else:
                    cellSuiv=cell.suivant
                    cell.suivant=cellSuiv.precedent=cellule(infoAInserer,cellSuiv,cell)
        
    def vider(self):
        '''Méthode qui vide la liste prioritaire de ses éléments et laisse une liste vide'''
        del self.elements[:]
        
    def longueur(self):
        '''Méthode qui renvoie le nombre d'éléments dans la liste prioritaire'''
        return len(self.elements)
    
    def defiler(self):
        '''Méthode qui renvoie l'élément le plus prioritaire de la File et le supprime de la File'''
        if not self.estVide():
            return self.elements.pop()
    
    def DixProchains(self):
        '''Méthode qui renvoie les 10 prochains éléments à sortir (qui seront défilés) de la File sans les supprimer de la File'''
        dixProchains=self.elements[-10:]
        return list(reversed(dixProchains))
        


















