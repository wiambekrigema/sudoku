class Sudoku :
  def __init__(self, nb):
        self.nb = nb
        self.grille = [[0 for i in range (9)] for j in range(9)]

  def put_number(self):
     row = int(input("Entrer le nombre de lignes (0-8): "))
     col = int(input("Entrer le nombre de colonnes (0-8): "))
     num = int(input("Entrer un numéro (1-9): "))
     if self.is_valid(row, col, num):
         self.grille[row][col] = num
     else:
         print(" Le numéro saisi n'est pas valid, réessayer ...")

  def is_valid(self, row, col, num):
     for x in range(9):
         if self.grille[row][x] == num or self.grille[x][col] == num:
             return False
     start_row, start_col = row - row % 3, col - col % 3
     for i in range(3):
         for j in range(3):
             if self.grille[i + start_row][j + start_col] == num:
                return False
     return True
