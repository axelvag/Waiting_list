# -*- coding: utf-8 -*-
"""
@author: david Granjon
"""

# ********************************************************************************************************
#   CLASSE FILE - IMPLEMENTATION D'UNE STRUCTURE DE DONNEES TYPE FILE AVEC TABLEAU DTNAMIQUE (LIST PYTHON) 
# ********************************************************************************************************

class File:
    '''Classe définissant une structure de données de type File (FIFO: First In First Out) avec méthodes.
    Cette classe utilise les tableaux dynamiques (list python)'''

    def __init__(self,L=[]):
        '''Méthode "constructeur"qui construit une structure de type File à partie d'une liste vide ou pas'''
        self.liste=list(L)      # Attribut 'liste' de type list python
        
    def __str__(self):
        '''Surcharge de l'affichage: méthode qui redéfinie l'affichage de la File de façon personnalisée lors d'un print'''
        if self.estVide():
            return "File vide !!"
        else:
            chaine="File: "
            chaine+=" ".join(map(str, self.liste))
            return chaine
    
    def estVide(self):
        '''Méthode qui renvoie True si la File est vide, False sinon'''
        return (len(self.liste)==0)
    
    def vider(self):
        '''Méthode qui vide le contenu de la file, et renvoi False si elle est vide'''
        if not self.estVide():
            del self.liste[:]       # Supprime tous les éléments de la liste
    
    def longueur(self):
        '''Méthode qui renvoie le nombre d'éléments dans la file'''
        return len(self.liste)
    
    def enfiler(self,elem):
        '''Méthode qui enfile(ajoute) un élément à la file en fin de file(liste)'''
        self.liste.append(elem)
    
    def defiler(self):
        '''Méthode qui renvoie le premier de la file et le supprime de la file'''
        if not self.estVide():
            return self.liste.pop(0)
        else:
            return False
               
    def DixProchains(self):
        '''Méthode qui renvoie les 10 prochains éléments à sortir (qui seront défilés) de la File sans les supprimer de la File'''
        Dix = []
        if not self.estVide():
            if len(self.liste)<10:
                for i in range(len(self.liste)):
                    Dix.append(self.liste[i])
            else:
                for i in range(10):
                    Dix.append(self.liste[i])
        return Dix