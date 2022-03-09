from tkinter import *
from tkinter import ttk
from Level import start_position
from solver import solve
import numpy as np
import time
from pieces import NewGridPiece

def Couleur(i):
    switcher = {
        0: "white",
        1: "#FF1493",  # pink
        2: "#FF0000",  # red
        3: "#8B0000",   #dark_red
        4: "#0161b0",       #blue
        5: "#87CEFA",       #light_blue
        6: "#011c58",       #dark_blue
        7: "#7fbe3c",       #green
        8: "#20B2AA",       #light_green
        9: "#006400",       #dark_green
        10: "#530152",      #purple
        11: "#FFFF00",      #yellow
        12: "#FFA500"       #orange
    }
    return switcher.get(i)


# fonction contenant toute l'interface graphique du jeu
def InterfaceGraphique(grid):
    # variables
    Ovale = []  # créer un liste pour stocker les ellipses créées
    OvalePieceRestante = []  # créer une liste pour stocker toutes les ellipses créés pour les petits cercles à droite
    NiveauEntier = 0  # correspond au niveau qui est selectionné convertie en entier
    PausePosePiece = 0.75

    # cercle
    PositionXPremierCercle = 40
    PositionYPremierCercle = 70
    DiamètreCercle = 45
    EspaceEntreCercle = 10

    # Nombre de cercle
    NombreDeCerclesX = 11
    NombreDeCerclesY = 5
    # fenêtre

    TailleF_X = 1100
    TailleF_Y = 550

    # coleur des ronds
    CouleurPiece = "white"

    # Coordonnés des deux rectangles (1 rectangle pour les pièces disponibles et 1 autre pour le jeu)

    StartPositionXPremierRectangle = PositionXPremierCercle - 10
    StartPositionYPremierRectangle = PositionYPremierCercle - 10
    TailleEnXRectangle2 = 345
    Espace1er2emeRectangle = 50

    # Ici, on définit la position finale en X et Y de premier rectangle. On commence par la position initiale et on rajoute le diamètre de chaque cercle avec leurs espaces afin que les cercles
    # puissent entrer dans le rectangle. A la fin, on enlève le dernier espace entre cercle qui est en trop(car on ne va pas en créer un nouveau) puis on ajoute 10 pour la distance entre le prermier cercle et le rectangle et 10 pour le dernier cercle et le rectangle
    EndPositionXPremierRectangle = StartPositionXPremierRectangle + NombreDeCerclesX * (
                DiamètreCercle + EspaceEntreCercle) - EspaceEntreCercle + 20
    EndPositionYPremierRectangle = StartPositionYPremierRectangle + NombreDeCerclesY * (
                DiamètreCercle + EspaceEntreCercle) - EspaceEntreCercle + 20
    CouleurPremierRectange = "#7c7c7d"

    StartPositionXDeuxièmeRectangle = EndPositionXPremierRectangle + Espace1er2emeRectangle  # L'espace entre premier rectangle et dernier rectangle : 50
    StartPositionYDeuxièmeRectangle = StartPositionYPremierRectangle  # les dimensions en Y seront les mêmes que le premier rectangle
    EndPositionXDeuxièmeRectangle = StartPositionXDeuxièmeRectangle + TailleEnXRectangle2  # la taille du 2ème rectange en X sera de 400
    EndPositionYDeuxièmeRectangle = EndPositionYPremierRectangle

    # Définition de l'espace entre les pieces à poser
    EspaceXEntrePiece = 85
    EspaceYEntrePiece = 85

    # première fenêtre
    window = Tk()

    # paramètres de la fenêtre
    window.title("IQ Puzzler")

    # définition de la taille mini et max
    window.minsize(TailleF_X, TailleF_Y)
    window.maxsize(TailleF_X, TailleF_Y)

    # Canvas
    canvas = Canvas(width=TailleF_X, height=TailleF_Y, bg="#e0e1e2")
    canvas.pack()  # permet de stockER les données graphiques que l'on veut appliquer à la fenêtre

    # label
    # fill désigne la couleur, anchor désigne la position du label par rapport aux coordonnées et font la police du texte
    Label_Possibilitee = canvas.create_text(StartPositionXPremierRectangle + 3, 50, font=("Courrier", 10),
                                            text="Nombre de possibilités :", anchor='w')
    Label_PieceDispo = canvas.create_text(StartPositionXDeuxièmeRectangle, 50, font=("Courrier", 10),
                                          text="Pièces disponibles", anchor='w')
    Label_Difficulte = canvas.create_text(StartPositionXPremierRectangle, EndPositionYPremierRectangle + 25,
                                          font=("Courrier", 10), text="Choisir un niveau de difficulté :", anchor='w')

    def Actualisation(grid,
                      pieces):  # fonction qui permet de faire l'actualisation de la grille lors du changement du niveau

        if len(Ovale) != 0:  # supprime la grille à chaque actualisation
            for X in range(len(Ovale)):
                canvas.delete(Ovale[X])
        if len(OvalePieceRestante) != 0:  # supprime les pièces affichées à droite à chaque changement de niveau
            for X in range(len(OvalePieceRestante)):
                canvas.delete(OvalePieceRestante[X])

        # affichage des pièces à poser

        for Z in range(len(pieces)):  # pour chaque pièces restante
            try:
                pieceActu = pieces[Z].variants[0]
                TailleYPiece = pieceActu.shape[0]
                TailleXPiece = pieceActu.shape[1]
            except:
                pieceActu = pieces[
                    Z]  # dans le cas où on récupère déjà la configuration correcte de la pièce à afficher
                TailleYPiece = pieceActu.shape[0]
                TailleXPiece = pieceActu.shape[1]

            for Y in range(TailleYPiece):  # pour Y dans les coordonnées en Y de la matrice de la piece
                for X in range(TailleXPiece):  # pour X dans les coordonnées en X de la matrice de la piece
                    if (pieceActu[Y][X] != 0):  # On affiche seulement la pièce et non pas sa matrice entière
                        CouleurPiece = Couleur(pieceActu[Y][
                                                   X])  # la grid ne peut pas être égal à 0, les autres chiffres correspondent à la piece elle-meme,
                        # il suffit donc de prendre ce chiffre et de vérifier à quelle couleur il correspond

                        # En fonction du nombre de pièces à calculer, on va modifier les coordonnées de début et de la fin.
                        # les 3 premiers pièces vont être situées sur la première ligne et le reste sur les autres
                        if (Z <= 3):
                            coordonneeDebutX = 700 + Z * EspaceXEntrePiece + X * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeDebutY = PositionYPremierCercle + Y * (DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeFinX = 700 + Z * EspaceXEntrePiece + DiamètreCercle / 3 + X * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeFinY = PositionYPremierCercle + DiamètreCercle / 3 + Y * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                        elif (Z <= 7):
                            coordonneeDebutX = 700 + (Z - 4) * EspaceXEntrePiece + X * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeDebutY = PositionYPremierCercle + EspaceYEntrePiece + Y * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeFinX = 700 + (Z - 4) * EspaceXEntrePiece + DiamètreCercle / 3 + X * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeFinY = PositionYPremierCercle + EspaceYEntrePiece + DiamètreCercle / 3 + Y * (
                                    DiamètreCercle / 3 + EspaceEntreCercle / 3)
                        elif (Z <= 11):
                            coordonneeDebutX = 700 + (Z - 8) * EspaceXEntrePiece + X * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeDebutY = PositionYPremierCercle + EspaceYEntrePiece * 2 + Y * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeFinX = 700 + (Z - 8) * EspaceXEntrePiece + DiamètreCercle / 3 + X * (
                                        DiamètreCercle / 3 + EspaceEntreCercle / 3)
                            coordonneeFinY = PositionYPremierCercle + EspaceYEntrePiece * 2 + DiamètreCercle / 3 + Y * (
                                    DiamètreCercle / 3 + EspaceEntreCercle / 3)

                        OvalePieceRestante.append(
                            canvas.create_oval(coordonneeDebutX, coordonneeDebutY, coordonneeFinX, coordonneeFinY,
                                               outline=CouleurPiece,
                                               fill=CouleurPiece))  # créer des cercles et les sauvegarde dans une liste

        # ensemble de deux boucles pour créer toutes les ellipses pour la grille
        for Y in range(5):
            for X in range(11):

                if (grid[
                    Y, X] == 0):  # pour remplir avec des cases vides c'est à dire des ronds avec coutour blanc remplis avec du gris
                    # créer une ellipse et le stocke dans la variable Ovale
                    Ovale.append(canvas.create_oval(PositionXPremierCercle + X * (DiamètreCercle + EspaceEntreCercle),
                                                    PositionYPremierCercle + Y * (DiamètreCercle + EspaceEntreCercle),
                                                    PositionXPremierCercle + DiamètreCercle + X * (
                                                            DiamètreCercle + EspaceEntreCercle),
                                                    PositionYPremierCercle + DiamètreCercle + Y * (
                                                            DiamètreCercle + EspaceEntreCercle),
                                                    outline="white"))  # créer des cercles
                else:  # dans le cas où la case porte un numéro différent de 0, ajouter un rond avec la couleur correspondante
                    # créer des ronds et les sauvgarde dans une liste(afin de pouvoir les supprimer par la suite)
                    CouleurPiece = Couleur(
                        grid[Y, X])  # grid va renvoyer le nombre correspond au coordonnées de la case dans la matrice
                    Ovale.append(canvas.create_oval(PositionXPremierCercle + X * (DiamètreCercle + EspaceEntreCercle),
                                                    PositionYPremierCercle + Y * (DiamètreCercle + EspaceEntreCercle),
                                                    PositionXPremierCercle + DiamètreCercle + X * (
                                                            DiamètreCercle + EspaceEntreCercle),
                                                    PositionYPremierCercle + DiamètreCercle + Y * (
                                                            DiamètreCercle + EspaceEntreCercle),
                                                    outline=CouleurPiece, fill=CouleurPiece))  # créer des cercles

    # éxécute cette fonction lorsque la difficulté a changé, celui-ci a été modifiée par le joueur
    def difficulty_changed(event):
        Niveau = []  # création d'une liste vide qui va contenir le niveau selectionné

        def Level_changed(event):
            grid = np.zeros((5, 11), dtype=np.uint8)  # reset de la grille à chaque clique
            Actualisation(grid, [])  # actualise la grille
            NiveauSelectionne = comboBoxNiveau.get()[
                                7:]  # on prend les dernière lettres du string. "Niveau 4" comporte 8 lettres, on va supprimé les 7 première pour avoir seulement le numéro du niveau
            NiveauEntier = int(
                NiveauSelectionne)  # convertie le niveau en entier afin de pouvoir l'afficher dans la grille
            grid = start_position(NiveauEntier)[0]  # récupère la grille en fonction du niveau selectionné
            pieces = start_position(NiveauEntier)[1]  # récupère les pièces à placer du niveau selectionné
            Actualisation(grid, pieces)  # affiche les pièces et la grille

            def LancementIA():
                if (NiveauEntier != 0):  # si un niveau est selectionné
                    grid = start_position(NiveauEntier)[0]
                    pieces = start_position(NiveauEntier)[1]

                    # path correspond au chemin parcourue, cette variable contient de nombreuses données importante,
                    # on va chercher la grille qui est résolue, pour cela, on parcoure les données de cette variable
                    path = solve(grid, pieces, [])[1]

                    i = 0  # variable qui va compter le nombre de pièces à poser
                    for W in range(len(path)):  # parcourt la liste de données contenant toutes les grilles

                        Actualisation(path[W].grid, path[W].piece)  # ajoute la pièce sauvegardé dans la grille
                        window.update()  # met à jour l'interface graphique
                        i += 1
                        time.sleep(PausePosePiece)  # effectue une pause de 0.75 secondes

                    # permet de placer la dernière pièce car la variable path ne contient pas la grille completé, toutefois,
                    # elle indique l'emplacement de la dernière pièce et sa configuration
                    grid = NewGridPiece(path[i - 1].grid, path[i - 1].variant, path[i - 1].x, path[i - 1].y)
                    ListePiecesMise = []  # Liste qui contient toutes les pièces dans la grille mise avec leur configuration
                    for S in range(len(path)):
                        ListePiecesMise.append(path[S].variant)  # ajoute la pièce dans la liste
                    Actualisation(grid,
                                  ListePiecesMise)  # affiche la configuration des pièces posées et leurs ordre de placement

            # bouton
            bouton = Button(window, text="Lancer l'IA", command=LancementIA)
            bouton.place(x=620, y=EndPositionYPremierRectangle + 17)  # permet de placer le bouton

        if (comboBoxDifficulte.get() == "STARTER"):
            for n in range(1, 12 + 1):  # le "+1" est ajouté car la fonction range(x, y) va de x à y non inclue [x, y[
                Niveau.append("Niveau " + str(
                    n))  # ajoute le texte niveau dans une liste, la fonction str permet de convertir en string
        if (comboBoxDifficulte.get() == "JUNIOR"):
            for n in range(13, 24 + 1):
                Niveau.append("Niveau " + str(n))
        if (comboBoxDifficulte.get() == "EXPERT"):
            for n in range(25, 30 + 1):
                Niveau.append("Niveau " + str(n))
        if (comboBoxDifficulte.get() == "MASTER"):
            for n in range(31, 36 + 1):
                Niveau.append("Niveau " + str(n))

        if (comboBoxDifficulte.get() == "WIZARD"):
            for n in range(37, 40 + 1):  # niveau de 37 à 40
                Niveau.append("Niveau " + str(n))
        if (Niveau):  # si la liste n'est pas vide
            comboBoxNiveau = ttk.Combobox(window, values=Niveau, width=20)  # ajoute au combobox avec les niveaux dedans
            comboBoxNiveau['state'] = 'readonly'  # empêche le joueur de changer le texte dans la combobox
            comboBoxNiveau.set("Choose a level")  # definit le niveau qui s'affiche en premier
            comboBoxNiveau.place(x=400, y=EndPositionYPremierRectangle + 15)  # placement du combobox
            comboBoxNiveau.bind('<<ComboboxSelected>>',
                                Level_changed)  # exécute du code situé dans l'event "Level_changed" lorsque la difficultée est changée

    # combobox
    # creation d'un groupe de plusieurs difficultées
    Difficulte = ('STARTER', 'JUNIOR', 'EXPERT', 'MASTER', 'WIZARD')
    comboBoxDifficulte = ttk.Combobox(window, values=Difficulte, width=15)  # créer un combobox et y ajoute les données
    comboBoxDifficulte['state'] = 'readonly'
    comboBoxDifficulte.set("Choose a difficulty")  # definit ce qui s'affiche en premier lorsque rien n'est sélectionné
    comboBoxDifficulte.place(x=230, y=EndPositionYPremierRectangle + 15)  # placement du combobox
    comboBoxDifficulte.bind('<<ComboboxSelected>>',
                            difficulty_changed)  # exécute du code situé dans l'event "difficulty_changed" lorsque la difficultée est changée

    # créer deux rectangles de jeu, ici on multiplie par 5 et 11 car c'est la dimension du puzzle (11*5 vides)
    # outline correspond à la couleur de la bordure du rectangle
    canvas.create_rectangle(StartPositionXPremierRectangle, StartPositionYPremierRectangle,
                            EndPositionXPremierRectangle, EndPositionYPremierRectangle, fill=CouleurPremierRectange,
                            outline="#3a5a92", width=2)
    canvas.create_rectangle(StartPositionXDeuxièmeRectangle, StartPositionYDeuxièmeRectangle,
                            EndPositionXDeuxièmeRectangle, EndPositionYDeuxièmeRectangle, fill=CouleurPremierRectange,
                            outline="#3a5a92", width=2)

    Actualisation(grid, [])

    # logo
    window.iconbitmap("logo_pret.ico")

    # afficher
    window.mainloop()













