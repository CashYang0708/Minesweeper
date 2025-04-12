import pytest
from src.minesweeper import Minesweeper

@pytest.fixture
def game():
    return Minesweeper(5, 5)

def test_minesweeper_initialization():
    """Test if Minesweeper initializes correctly"""
    assert game.dimension == 5
    assert game.num_mines == 5
    assert len(game.board) == 5
    assert len(game.dug) == 0
    assert game.dimension>= game.num_mines
    """Test if correct number of mines are placed"""
    mine_count = sum(row.count(-1) for row in game.board) 
    assert mine_count == 5

def test_invalid_position(game):
    """Test digging at invalid positions"""
    assert not game.dig(-1, 0)  
    assert not game.dig(0, -1)
    assert not game.dig(5, 0)
    assert not game.dig(0, 5)

def test_neighbor_bombs():
    """Test counting neighboring bombs"""
    test_board = [
        [-1, 0, 0],
        [0, 0, 0], 
        [0, -1, 0]
    ]
    game = Minesweeper(3, 2)
    game.board = test_board
    assert game.get_neighbor_bombs(test_board, 1, 1) == 2
    assert game.get_neighbor_bombs(test_board, 0, 1) == 1

def test_dig_empty_cell():
    """Test digging an empty cell"""
    test_board = [
        [1, 1, 0],
        [1, -1, 0],
        [1, 1, 0]
    ]
    game = Minesweeper(3, 1) 
    game.board = test_board
    assert game.dig(0, 2)
    assert (0, 2) in game.dug

def test_dig_mine():
    """Test digging a mine"""
    test_board = [
        [1, 1, 0],
        [1, -1, 0],
        [1, 1, 0]
    ]
    game = Minesweeper(3, 1)
    game.board = test_board
    assert not game.dig(1, 1)
    assert (1, 1) in game.dug

def test_recursive_dig():
    """Test recursive digging of empty cells"""
    test_board = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, -1]
    ]
    game = Minesweeper(3, 1)
    game.board = test_board
    game.dig(0, 0)
    assert (0, 0) in game.dug
    assert (0, 1) in game.dug
    assert (1, 0) in game.dug
    assert (1, 1) in game.dug

def test_board_string_representation():
    """Test string representation of the board"""
    game = Minesweeper(2, 1)
    game.dig(0, 0)
    board_str = str(game)
    assert any(char in board_str for char in ['0','1','2','3','4','5','6','7','8'])
    assert 'X' in board_str
