from dataclasses import dataclass
#Importation des membres dataclasse du module dataclasses
#Importer le module entier de numpy et spécifier l'alias comme np
import numpy as np

import pieces


def NewGridPiece(grid, piece, y, x):#fonction permettant de créer une grille avec les nouvelles pièces
    # len(grid) => nombre de lignes de la piece/grille
    # len(grid[0]) => nombre de colonnes de la piece/grille

    gridPiece = grid
    TailleYPiece = len(piece)
    TailleXPiece = len(piece[0])

    #len(gridPiece) renvoie la taille de la pièce ou de la grille en Y sauf que les coordonnées de la grille vont de 0 à 10
    #car on commence à 0 et non à 1
    #le "if" sert à vérifer s'il sera possible de placer la pièce afin qu'elle ne déborde pas de la matrice
    if((x+TailleXPiece) <= (len(gridPiece[0])) and x >=0 and (y+TailleYPiece) <= (len(gridPiece))  and y >=0):
        gridPiece[y:(y+TailleYPiece), x:(x+TailleXPiece)] = gridPiece[y:(y+TailleYPiece), x:(x+TailleXPiece)] + piece
    else:
        print("Impossible de placer la pièce")
    return gridPiece






@dataclass
class Piece:
#Déclarer une classe
   def __init__(self, data):#Constructeur
       self.variants = Piece._create_variants(data)#Transmettre la valeur de data

#Faites pivoter la pièce de 90 degrés
   @classmethod
   def _create_variants(cls, data):
       variants = []
       for piece in [data, np.fliplr(data)]:  # utiliser des fonctions dans np(numpy)
           for k in range(4):  # range(4)=0,1,2,3,    4 variants dans une pièece
               candidate = np.rot90(piece, k)
               for existing in variants:  # Pour éviter les doublons
                   if np.array_equal(existing, candidate):
                       break  # candidate is equal to existing
               else:
                   variants.append(candidate)  # Ajouter candidate à la liste de varients
       # sym=symetrie(piece)#faire l'inverse
       sym = np.fliplr(data)                        #fonction qui réalise la symétrie de la pièce
       for sym in [data, np.fliplr(data)]:          # utiliser des fonctions dans np(numpy)
           for k in range(4):  # range(4)=0,1,2,3
               candidate = np.rot90(piece, k)
               for existing in variants:
                   if np.array_equal(existing, candidate):
                       break  # candidate is equal to existing
               else:
                   variants.append(candidate)  # Ajouter candidate à la liste de varients
       return variants


   def __equ__(self, other):
        if len(self.variants) != len(other.variants):
            return False
        else:
            if np.all(self.variants[0] == other.variants[0]) and np.all(self.variants[1] == other.variants[1]) and np.all(
                    self.variants[2] == other.variants[2]) and np.all(self.variants[3] == other.variants[3]):
                if len(self.variants) > 4:
                    if np.all(self.variants[4] == other.variants[4]) and np.all(
                            self.variants[5] == other.variants[5]) and np.all(
                            self.variants[6] == other.variants[6]) and np.all(self.variants[7] == other.variants[7]):
                        return True
                    else:
                        return False
                else:
                    return True

            else:
                return False

#Définir 12 pièces.
def pink(value=1):#Pour chaque pièce, attribuez une valeur différente non nulle pour distinguer
   piece = np.zeros((4, 2), dtype=np.uint8)#Définir une matrice
   piece[:2, 0] = value
   piece[1:, 1] = value
   return Piece(piece)
#Mettre des valeurs dans une matrice en fonction de la forme des différentes pièces

def red(value=2):
   piece = np.zeros((4, 2), dtype=np.uint8)
   piece[0, 0] = value
   piece[:, 1] = value

   return Piece(piece)


def dark_red(value=3):
   piece = np.zeros((3, 2), dtype=np.uint8)
   piece[:2, 0] = value
   piece[1:, 1] = value
   return Piece(piece)


def blue(value=4):
   piece = np.zeros((3, 3), dtype=np.uint8)
   piece[:, 0] = value
   piece[-1, :] = value
   return Piece(piece)


def light_blue(value=5):
   piece = np.zeros((2, 2), dtype=np.uint8)
   piece[:, 0] = value
   piece[-1, :] = value
   return Piece(piece)


def dark_blue(value=6):
   piece = np.zeros((2, 3), dtype=np.uint8)
   piece[0, :] = value
   piece[1, 0] = value
   return Piece(piece)


def green(value=7):
   piece = np.zeros((2, 3), dtype=np.uint8)
   piece[0, :] = value
   piece[1, [0, 2]] = value
   return Piece(piece)


def light_green(value=8):
   piece = np.zeros((2, 3), dtype=np.uint8)
   piece[0, :2] = value
   piece[1, :] = value
   return Piece(piece)


def dark_green(value=9):
   piece = np.zeros((3, 2), dtype=np.uint8)
   piece[:, 0] = value
   piece[1, 1] = value
   return Piece(piece)


def purple(value=10):
   piece = np.zeros((3, 3), dtype=np.uint8)
   piece[0, 0] = value
   piece[1, :2] = value
   piece[2, 1:] = value
   return Piece(piece)


def yellow(value=11):
   piece = np.zeros((2, 4), dtype=np.uint8)
   piece[0, :] = value
   piece[1, 2] = value
   return Piece(piece)


def orange(value=12):
   piece = np.zeros((3, 3), dtype=np.uint8)
   piece[0, 1] = value
   piece[1, :2] = value
   piece[2, 1:] = value
   return Piece(piece)
#pour montrer un exemple
#ajouter dans start_position.py




