# -*- coding: utf-8 -*-
"""
@author: david Granjon
"""

# Import des librairies et classes nécessaires
from random import randint
from Class_File_ListPython import File


print ("1ère instance créée: ma_File")
# Création d'une instance de votre classe File avec tableau dynamique (list python)
ma_File=File()

# test vide ou pas ?
print (ma_File.estVide())

# Ajout d'un élément dans la File ?
ma_File.enfiler(42)

# Affichage de la File
print (ma_File)

# Suppression cette instance de File
del ma_File

print ("\n2ème instance créée: ma_File1")
# Création d'une liste elements avec quelques valeurs
elements=[randint(0,10) for x in range (6)]

# Création d'une nouvelle instance de votre classe File avec tableau dynamique (list python)
# et remplissage à la création avec la liste des éléments précédemment céées
ma_File1=File(elements)
print (ma_File1)

# test vide ou pas ?
print (ma_File1.estVide())

# defile des éléments
element=ma_File1.defiler()
print (element)
print (ma_File1)
element=ma_File1.defiler()
print (element)
print (ma_File1)

# defile un élément
ma_File1.enfiler(42)
ma_File1.enfiler(84)
print (ma_File1)

# vide la liste
ma_File1.vider()

# Tentative de défiler une file vide
element=ma_File1.defiler()

# test vide ou pas ?
print (ma_File1.estVide())


print ("\n3ème instance créée: ma_File2")
# Création d'une liste elements avec quelques valeurs
elements=[randint(0,100) for x in range (20)]
ma_File2=File(elements)
print (ma_File2)
# Affichage des 10 prochains éléments qui vont être défilés
print (ma_File2.DixProchains())












