from src.minesweeper import Minesweeper

if __name__ == "__main__":
    dimension = 5 # Dimension of the board, y0u can change to any number you want
    num_mines = 5 # Numbers of mines, you can change to any number that is less than dimension*dimension

    game = Minesweeper(dimension, num_mines)
    game.play()