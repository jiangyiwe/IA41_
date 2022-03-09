

import itertools

import numpy as np
from Level import start_position
from dataclasses import dataclass


# On définit une classe donnée qui va permettre de stocker à
# chaque noeud de l'arbre, la grille, la variante de la pièce
# les coordonées de positionnement de la pièce en question
# dans la grille
# Cette classe est donc le codage d'un état
@dataclass
class Donnee:

    def __init__(self, data1, data2, data3, data4, data5):
        self.grid = data1
        self.piece = data2
        self.x = data3
        self.y = data4
        self.variant = data5


# La fonction case_isolee prends en paramètre une matrice et
# renvoie un booléen pour indiquer si oui ou non une case est
# isolée. Une case isolée est une case vide (contenant 0) dans
# la grille et dont les cases voisines sont pleines.

def case_isolee(matrice):
    n = matrice.shape[0]
    m = matrice.shape[1]
    # On va parcourrir la matrice et en fonction de la case
    # sur laquelle on se trouve on va vérifier les voisins
    # existant. C'est ce qui justifie l'étude des cas
    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 0:
                if (i >= 1 and i < 4):      #sans les bordure du haut et du bas
                    if j == 0:              #avec la bordure gauche
                        if (matrice[i][j + 1] != 0
                                and matrice[i + 1][j] != 0 and matrice[i - 1][j] != 0):
                            return True
                    elif j == 10:           #avec la bordure droite
                        if (matrice[i][j - 1] != 0
                                and matrice[i + 1][j] != 0 and matrice[i - 1][j] != 0):
                            return True
                    else:
                        if (matrice[i][j + 1] != 0 and matrice[i][j - 1] != 0
                                and matrice[i + 1][j] != 0 and matrice[i - 1][j] != 0):
                            return True
                if (i == 0 and matrice[i + 1][j] != 0) or (i == 4 and matrice[i - 1][j] != 0):  #bordure du haut ou du bas
                    if j == 0:                                                  #bordure gauche
                        if matrice[i][j + 1] != 0:
                            return True
                    elif j == 10:                                               #bordure droite
                        if matrice[i][j - 1] != 0:
                            return True
                    else:
                        if matrice[i][j - 1] != 0 and matrice[i][j + 1] != 0:
                            return True

    return False


# La fonction deux_case_isolee prends en paramètre une matrice et
# renvoie un booléen pour indiquer si oui ou non deux cases sont
# isolées. Deux cases isolées sont des cases vides (contenant 0) dans
# la grille et dont les cases voisines sont pleines.

def deux_case_isolee(matrice):
    n = matrice.shape[0]
    m = matrice.shape[1]
    # On va parcourrir la matrice et en fonction de la case
    # sur laquelle on se trouve on va vérifier les voisins
    # existant. C'est ce qui justifie l'étude des cas

    # On va d'abord chercher 2 cases vides, voisines horizontalement
    for i in range(n):
        for j in range(m - 1):
            if matrice[i][j] == 0:
                if matrice[i][j + 1] == 0:
                    if ((i == 0 and matrice[i + 1][j] != 0 and matrice[i + 1][j + 1] != 0) or
                            (i == 4 and matrice[i - 1][j] != 0 and matrice[i - 1][j + 1] != 0) or
                            (i > 0 and i < 4 and matrice[i + 1][j] != 0 and matrice[i + 1][j + 1] != 0 and
                             matrice[i - 1][j] != 0 and matrice[i - 1][j + 1] != 0)):
                        if j == 0:
                            if matrice[i][j + 2] != 0:
                                return True
                        elif j == 9:
                            if matrice[i][j - 1] != 0:
                                return True
                        else:
                            if matrice[i][j - 1] != 0 and matrice[i][j + 2] != 0:
                                return True
    # On va d'abord chercher 2 cases vides, voisines verticalement
    for j in range(m):
        for i in range(n - 1):
            if matrice[i][j] == 0:
                if matrice[i + 1][j] == 0:
                    if ((j == 0 and matrice[i][j + 1] != 0 and matrice[i + 1][j + 1] != 0) or
                            (j == 10 and matrice[i][j - 1] != 0 and matrice[i + 1][j - 1] != 0) or
                            (j > 0 and j < 10 and matrice[i][j + 1] != 0 and matrice[i + 1][j + 1] != 0 and matrice[i][
                                j - 1] != 0 and matrice[i + 1][j - 1] != 0)):

                        if i == 0:
                            if matrice[i + 2][j] != 0:
                                return True
                        elif i == 3:
                            if matrice[i - 1][j] != 0:
                                return True
                        else:
                            if matrice[i - 1][j] != 0 and matrice[i + 2][j] != 0:
                                return True
    return False


# La fonction nb_case_vide prends en paramètre une matrice et
# renvoie le nombre de case valant 0(vide) de la matrice
def nb_case_vide(matrice):
    nb = 0
    n = matrice.shape[0]
    m = matrice.shape[1]
    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 0:
                nb = nb + 1
    return nb


# La fonction solve prends en paramètre une matrice(la grille), la liste
# des pièces non mises dans la grille et la suite des pièces qui
# a conduit à la résolution du problème.
# Elle renvoie la solution composée de la grille complète, le chemin de résolution

def solve(grid, pieces, path):
    if grid.min() > 0:
        # Il n'existe plus de case vide dans la grille
        print("Solution found:\n", grid)
        return grid

    # faire une copie locale (propre à la recursion actuelle de la fonction)
    # de la liste des pièces non mises (pieces) dans la variable my_pieces
    my_pieces = pieces.copy()

    # On retire une pièce pour tenter de la mettre
    piece = my_pieces.pop()

    # On parcours les variantes de la pièce retirée
    for i, variant in enumerate(piece.variants):
        # On parcours les emplacements possibles pour la variante de la pièce
        for r, c in itertools.product(
                range(grid.shape[0] - variant.shape[0] + 1),
                range(grid.shape[1] - variant.shape[1] + 1)):
            # On teste s'il y aura un débordement (la pose de la pièce
            # va provoquer un débordement de la grille de jeu)
            if (11 - c) < variant.shape[1]:  # Il y a débordement
                continue  # On passe à la prochaine variante de la pièce

            # On fait une copie de la grille actuelle
            test = grid.copy()
            # On ajoute la variante dans la grille à l'emplacement
            # sélectionné précédemment
            test[r:r + variant.shape[0], c:c + variant.shape[1]] += variant

            # On teste que le résultat de la mise de la pièce respecte
            # les conditions suivantes :
            #    - Il n'existe pas de chevauchement (une pièce n'est pas sur une autre)
            #    - Il n'y a pas de case une ou deux cases isolées
            if not np.any(grid[r:r + variant.shape[0],
                          c:c + variant.shape[1]] * variant) and not (case_isolee(test) or deux_case_isolee(test)):
                # En entrant ici, cela signifie que la variante pièce peut
                # être mise à cet emplacement

                # On sauvegarde l'état dans la liste de l'enchaînement
                # ayant conduit à la solution dans path
                path.append(Donnee(grid, my_pieces, r, c, variant))

                # On crèe une nouvelle grille réflétant l'état actuel de la grille
                newgrid = grid.copy()
                newgrid[r:r + variant.shape[0],
                c:c + variant.shape[1]] += variant
                print("Nouvelle Grille : \n", newgrid)
                print("pieces restantte : \n", my_pieces)
                print("Path : \n", path)
                print("{}Placement de la pièce valant {}, variante {} à {}, {}".format(
                    '    ' * (2 - len(my_pieces)), variant.max(), i, r, c))

                # On appelle la fonction(recursion) avec les nouvelles
                # valeurs (grille, pièces non mise et le chemin valide)
                solution = solve(newgrid, my_pieces, path)

                if solution is not None:
                    # Si on trouve une solution, on la renvoie et le chemin également
                    return solution, path
                else:
                    # Si on ne trouve pas de solution, on enlève la variante
                    # de la pièce dans la liste des étapes
                    path.pop()

                    # On a terminé de travailler avec cette pièce
    return None



