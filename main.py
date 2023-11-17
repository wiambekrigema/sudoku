from sudoku import Sudoku
def main():
  sudoku = Sudoku(9)
  print(" la grille de jeu")
  print("Entrer les numéros dans la grille. Pour une cellule vide, il faut rentrer 0 .")
  sudoku.put_number()
  print("Résoudre le jeu...")
  sudoku.solve()

if __name__ == "__main__":
   main()
