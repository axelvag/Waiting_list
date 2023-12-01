# -*- coding: utf-8 -*-
"""
@author: david Granjon
"""

class cellule:
    '''Classe qui défini une cellule de la liste doublement chainée'''
    # Constructeur
    def __init__(self,info,suiv,prec):
        self.info=info
        self.suivant=suiv
        self.precedent=prec
            
   
     
class FileLDC:
    '''Classe qui créée une File avec une liste doublement chainée'''
    
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
        return (self.prem==None and self.dern==None)
    
    
    def vider(self):
        '''Méthode qui vide proprement la File (liste doublement chainée) en effacant toutes les cellules'''
        while self.prem:
            cell = self.prem
            self.prem = cell.suivant
            del cell
        self.dern=None
    
    
    def _longueur(self):
        '''Méthode privée (pas appelée en dehors de l'instance): Affiche le nombre d'éléments dans la File (liste doublement chainée) et renvoie un entier ou un le texte "vide"'''
        nb = 0            
        cell=self.prem
        while cell:
            nb+=1
            cell=cell.suivant
        return nb
    
    
    def _ajouterEnTete(self,infoAInserer):
        '''Méthode privée (pas appelée en dehors de l'instance): Ajoute un élément en tête de la liste chainée'''
        if self._estVide():
            self.prem=self.dern=cellule(infoAInserer,None,None)
        else:
            cellSuiv=self.prem
            self.prem=cellSuiv.precedent=cellule(infoAInserer,cellSuiv,None)
    
    
    def enfiler(self,infoAInserer):
        '''Méthode qui ajoute un élément dans la File (liste doublement chainée) en bout de file'''
        if self._estVide():
            self._ajouterEnTete(infoAInserer)
        else:
            cell=self.dern
            cell.suivant=self.dern=cellule(infoAInserer,None,cell)


    def defiler(self):
        '''Méthode qui renvoie puis supprime le premier élément de la File (élément de tête de la liste doublement chainée)'''
        if not self._estVide():    
            cell = self.prem
            self.prem = cell.suivant
            if self.prem:
                self.prem.precedent = None
            else:
                self.dern = None
            return cell.info


    def vider(self):
        '''Méthode qui vide proprement la File (liste doublement chainée) en effacant toutes les cellules'''
        # A COMPLETER
    
        
    def DixProchains(self):
        '''Méthode qui renvoie les 10 prochains éléments à sortir (qui seront défilés) de la File sans les supprimer de la File'''
        liste=[]
        cell=self.prem
        while (cell and len(liste)<10):
            liste.append(cell.info)
            cell=cell.suivant
        return liste
        
























