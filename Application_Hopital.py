# -*- coding: utf-8 -*-
"""
@author: david Granjon
"""

# Import des librairies et classes nécessaires
from timeit import timeit
from random import randint
import tkinter as tk
from tkinter import ttk


# 1ère Partie
#from Class_File_ListPython import File
#fileAttente=File()     # Création d'une instance de la classe File (implémentée à partir d'un tableau dynamique (list python))


# # 2ème Partie
#from Class_File_LDChainee import FileLDC
#fileAttente=FileLDC()  # Création d'une instance de la classe FileLDC (implémentée par une liste doublement chainée)


# # 3ème Partie
#from Class_File_Prioritaire_ListPython import FilePrioritaire
#fileAttente=FilePrioritaire()      # Création d'une instance de la classe FilePrioritaire (implémentée à partir d'un tableau dynamique (list python))

# # 4ème Partie
from Class_File_Prioritaire_LDChainee import FilePrioritaireLDC
fileAttente=FilePrioritaireLDC()  # Création d'une instance de classe FilePrioritaireLDC (implémentée par une liste doublement chainée)






# =====================================================================================================================
#               FONCTIONS ET PROCEDURES
# =====================================================================================================================

def metEnAttente():
    nom=nomPatient.get()
    nomClasseObjet=fileAttente.__class__.__name__
    if (nomClasseObjet=='FilePrioritaire' or nomClasseObjet=='FilePrioritaireLDC'):
        valPriorite=int(choixPriorite.get())
        fileAttente.enfiler((valPriorite,nom))
    else:
        fileAttente.enfiler(nom)
    majListeAttente()
    
def prendEnCharge():
    fileAttente.defiler()
    majListeAttente()
    
def viderListeAttente():
    fileAttente.vider()
    majListeAttente()
   
def remplirListeAttente():
    liste=fileAttente.DixProchains()
    nomClasseObjet=fileAttente.__class__.__name__
    if (nomClasseObjet=='FilePrioritaire' or nomClasseObjet=='FilePrioritaireLDC'):
        listePatientsEnAttente=[f'MTS{noms[0]} - {noms[1]}' for noms in liste]
    else:
        listePatientsEnAttente=[f'{noms}' for noms in liste]
    for i in range(len(listePatientsEnAttente)):
        label=tk.Label(FrameListeAttente, text=listePatientsEnAttente[i], font=("tahoma", 13), fg='blue')
        label.grid(row=i, sticky='w')

def majListeAttente():
    for widget in FrameListeAttente.winfo_children():
        widget.destroy()
    remplirListeAttente()
    
def testEnfileTimeit():
    # Enfile nbRepeat patients dans la file, puis les défile
    nbRepeat=int(choixrepeat.get())
    nomClasseObjet=fileAttente.__class__.__name__
    if (nomClasseObjet=='FilePrioritaire' or nomClasseObjet=='FilePrioritaireLDC'): 
        tempsTest = timeit(lambda: fileAttente.enfiler((randint(1,5),'unNom')), number=nbRepeat)
    else:
        tempsTest = timeit(lambda: fileAttente.enfiler('unNom'), number=nbRepeat)
    tempsTest+= timeit(lambda: fileAttente.defiler(), number=nbRepeat)
    # Affiche le temps en ms mis pour enfiler et défiler les nbRepeat patients avec un arrondi à 2 chiffres après la virgule
    print(f'Temps pour enfiler/défiler {nbRepeat} patients: {1000*tempsTest:.2f} ms')

    
# =====================================================================================================================
#               PROGRAMME PRINCIPAL
# =====================================================================================================================


# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Gestion de l'attente aux urgences")
fenetre.geometry('640x640')


# Création d'un widget Canvas (zone graphique) et de l'image de fond
fichierImage = tk.PhotoImage(master=fenetre, file = "hopital.gif") 
labelImageDeFond = tk.Label(fenetre, image=fichierImage) 
labelImageDeFond.place(x=0, y=0)

# -----
# Création de la colonne de gauche de saisi du nom et de la priorité de l'urgence
# -----
# Titre colonne
yTitres=20
labelTitreAccueil = tk.Label(fenetre, text="Interface accueil", font=("tahoma Bold", 20))
labelTitreAccueil.place(x=50, y=20)

# Ligne d'insertion du nom du patient
yNom=90
labelNom = tk.Label(fenetre, text="Nom du patient:", font=("tahoma Bold", 13))
labelNom.place(x=0, y=yNom)
nomPatient= tk.StringVar()
txtNom = tk.Entry(fenetre, width=18, textvariable=nomPatient, font=("tahoma", 13))
txtNom.place(x=130, y=yNom)

# Ligne de choix de la priorité
yPriorite=130
labelPriorite = tk.Label(fenetre, text="MTS (urgence):", font=("tahoma Bold", 13))
labelPriorite.place(x=0, y=yPriorite)

choixPriorite = ttk.Combobox(fenetre)
choixPriorite['values']= (1, 2, 3, 4, 5)
choixPriorite.current(4)
choixPriorite.place(x=130, y=yPriorite)

# Lignes d'information priorité
yPriorite+=25
labelInfPriorite = tk.Label(fenetre, text="Prise en charge MTS:\n1: Immédiate     2: Très urgente (<10min)     3: Urgente (<60min)\n4: Standard (<120min)     5: Non urgente (<240min)", font=("tahoma", 7), justify=("left"))
labelInfPriorite.place(x=0, y=yPriorite)

# Bouton Mettre en attente
yBouton=220
btnAjoute = tk.Button(fenetre, text="Mettre en attente", font=("tahoma Bold", 13), command=metEnAttente)
btnAjoute.place(x=100, y=yBouton)

# Bouton Prendre en charge un patient
yBouton+=160
btnEnleve = tk.Button(fenetre, text="Prendre en charge patient", font=("tahoma Bold", 13), fg='red', command=prendEnCharge)
btnEnleve.place(x=10, y=yBouton)

# Bouton Vider liste d'attente
btnEnleve = tk.Button(fenetre, text="Vider la liste", font=("tahoma Bold", 13), fg='red', command=viderListeAttente)
btnEnleve.place(x=230, y=yBouton)


# -----
# Création de la colonne de droite d'affichage dans la salle d'attente
# -----
# Titre colonne
labelTitreAccueil = tk.Label(fenetre, text="Affichage salle d'attente", font=("tahoma Bold", 20))
labelTitreAccueil.place(x=330,y=yTitres)

# Création de la liste d'attente (Frame dans lequel il y'a la liste d'attente)
FrameListeAttente = tk.Frame(fenetre)
FrameListeAttente.place(x=360,y=65)
remplirListeAttente()
# Affichage <- Prochain
labelProchain = tk.Label(fenetre, text='<-- prochain', font=("tahoma Bold", 13), fg='maroon')
labelProchain.place(x=530,y=70)


# -----
# Création de la partie test Timeit
# -----
# Titre partie test
ytest=540
labelTitreAccueil = tk.Label(fenetre, text="Test de l'efficacité de la Structure de données (timeit)", font=("tahoma Bold", 14))
labelTitreAccueil.place(x=0, y=ytest)
ytest+=45
choixrepeat = ttk.Combobox(fenetre)
choixrepeat['values']= (100, 1000, 5000, 10000, 20000)
choixrepeat.current(1)
choixrepeat.place(x=20, y=ytest)
ytest-=5
# Bouton test
btnTestAlgo = tk.Button(fenetre, text="Tester", font=("tahoma Bold", 13), command=testEnfileTimeit)
btnTestAlgo.place(x=250, y=ytest)



fenetre.mainloop()















  