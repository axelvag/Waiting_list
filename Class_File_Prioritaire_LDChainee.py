# -*- coding: utf-8 -*-
"""
@author: david Granjon
"""

class cellule:
    '''Classe qui créée une cellule de la liste doublement chainée'''
    def __init__(self,info,suiv,prec):
        '''Méthode "constructeur" qui créée l'instance et initialise les attributs'''
        self.info=info
        self.suivant=suiv
        self.precedent=prec
            
   
     
class FilePrioritaireLDC:
    '''Classe qui créée une File prioritaire avec une liste doublement chainée'''
    
    def __init__(self):
        '''Méthode "constructeur", création de l'instance et initialisation des attributs'''
        self.prem=None
        self.dern=None
    
    def __str__(self):
        '''Surcharge de l'affichage: Affiche tous les éléments de la liste doublement chainée'''
        if self.prem==None:
            return "vide !"
        else:
            cellActuelle=self.prem
            chaine="<"
            while (cellActuelle.suivant!=None):
                chaine+=eval("f' {cellActuelle.info} :'")  # execute la f-strings
                cellActuelle=cellActuelle.suivant
            chaine+=eval("f' {cellActuelle.info} >'")
        return chaine
    
    
    def _estVide(self):
        '''Méthode privée (pas appelée en dehors de l'instance): Teste si la liste doublement chainée est vide'''
        return self.prem==None
             
           
    def enfiler(self,infoAInserer):
        '''Méthode qui ajoute un élément dans la File (liste doublement chainée) en fonction de sa priorité
        On remonte la File en partant du dernier élément tant que la priorité est inférieure à l'élément courant'''
        if self._estVide():
            self.dern=self.prem=cellule(infoAInserer,None,None)
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
       

    def defiler(self):
        '''Méthode qui renvoie puis supprime le premier élément de la File (élément de tête de la liste doublement chainée)'''
        if not self._estVide():    
            donnee=self.prem.info
            self.prem = self.prem.suivant
            if self.prem:
                self.prem.precedent = None
            else:
                self.dern = None
            return donnee


    def vider(self):
        '''Méthode qui vide proprement la File (liste doublement chainée) en effacant toutes les cellules'''
        while self.prem:
            cell = self.prem
            self.prem = cell.suivant
            del cell
        self.dern=None
            
        
    def DixProchains(self):
        '''Méthode qui renvoie les 10 prochains éléments à sortir (qui seront défilés) de la File sans les supprimer de la File'''
        liste=[]
        cell=self.prem
        while (cell and len(liste)<10):
            liste.append(cell.info)
            cell=cell.suivant
        return liste
        
























