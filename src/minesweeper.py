import random
from typing import List

class Minesweeper:
    def __init__(self, dimension: int, num_mines: int):
        self.dimension = dimension
        self.num_mines = num_mines
        self.board =self.make_board()
        self.dug = set() # store the positions that have been dug
    
    def make_board(self):
        # Create a board with all zeros
        board = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        
        # Place mines randomly on the board
        mine_positions = random.sample(range(self.dimension * self.dimension), self.num_mines)
        for pos in mine_positions:
            row = pos // self.dimension
            col = pos % self.dimension
            board[row][col] = -1 # Mark mine positions with -1
        
        # Update the board with the number of mines around each position
        for row in range(self.dimension):
            for col in range(self.dimension):
                if board[row][col] == -1:
                    continue
                board[row][col] = self.get_neighbor_bombs(board, row, col)
        
        return board
    
    def get_neighbor_bombs(self, board:List[List[int]], row: int, col: int):
        # Check if the position is valid
        if row < 0 or row >= self.dimension or col < 0 or col >= self.dimension:
            return 0
        
        # Count the number of mines around the position
        count = 0
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r == row and c == col:
                    continue
                if 0 <= r < self.dimension and 0 <= c < self.dimension and board[r][c] == -1:
                    count += 1
        return count
    
    def dig(self, row: int, col:int):
        
        self.dug.add((row, col))

        # Check if the position is a mine
        if self.board[row][col] == -1:
            print("Game Over! You hit a mine.")
            for i in range(self.dimension):
                print(self.board[i])
            return False
        elif self.board[row][col] == 0:
            # If the position is empty, dig recursively
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if (r,c) in self.dug:
                        continue
                    if 0 <= r < self.dimension and 0 <= c < self.dimension:
                        self.dig(r, c)

        return True
    
    def __str__(self):
        # Create a string representation of the board
        board_str = "  "
        for j in range(self.dimension):
            board_str += str(j) + " "
        board_str += "\n"

        for row in range(self.dimension):
            for col in range(self.dimension):
                if col == 0:
                    board_str += str(row) + " "
                if (row, col) in self.dug:
                    board_str += str(self.board[row][col]) + " "
                else:
                    board_str += "X "
            board_str += "\n"
        return board_str
    
    def play(self):
        # Main game loop
        while len(self.dug) < self.dimension * self.dimension - self.num_mines:
            print("Current board:")
            print(self)
            
            # Keep asking for valid coordinates
            while True:
                try:
                    row = int(input("Enter row to dig: "))
                    col = int(input("Enter column to dig: "))
                    
                    # Check if position is valid
                    if 0 <= row < self.dimension and 0 <= col < self.dimension:
                        break
                    else:
                        print(f"Invalid position! Please enter numbers between 0 and {self.dimension-1}")
                except ValueError:
                    print("Please enter valid numbers!")
            
            if not self.dig(row, col):
                break
            if len(self.dug) == self.dimension * self.dimension - self.num_mines:
                print("Congratulations! You cleared the board.")
                break
        

if __name__ == "__main__":
    dimension = 3
    num_mines = 2
    game = Minesweeper(dimension, num_mines)
    game.play()
    