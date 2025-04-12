# Minesweeper Game

A command-line implementation of the Minesweeper game in Python.

## Requirements

- Python 3.x
- pytest (for running tests)

## Installation

1. Clone the repository
2. Virtual enviroment setup and activate

```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```sh
pip install -r requirements.txt
```

## Play game

Run the game with default settings (default 5x5 board with 5 mines):

```sh
python main.py
```

You can modify the `dimension` and `num_mines` variables in `main.py` to change the board size and number of mines.

### How to Play

1. Enter row and column numbers to dig at that position
2. Numbers indicate how many mines are adjacent to that cell
3. Avoid hitting mines (-1)
4. Clear all non-mine cells to win

## Testing

Run the test suite:

```sh
pytest
```

## Project Structure

```
├── main.py           # Game entry point
├── requirements.txt  # Project dependencies
├── src/
│   └── minesweeper.py  # Core game logic
└── test/
    └── __init__.py
    └── test_minesweeper.py  # Test suite
```
