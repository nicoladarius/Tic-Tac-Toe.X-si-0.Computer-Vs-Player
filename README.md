# Tic-Tac-Toe Game – Player vs. Computer

By Nicola Darius - https://github.com/nicoladarius/Tic-Tac-Toe.X-si-0.Computer-Vs-Player

## The entire code, including comments and user interactions, is written in Romanian to ensure a fully localized experience.

## Description
This application implements the classic Tic-Tac-Toe game, where a player competes against the computer. The game is played on a 3x3 board, and the objective is to place three symbols in a row (horizontally, vertically, or diagonally).

**Game Rules** are:
1. The player and the computer take turns selecting cells on the game board.
2. The player plays with the X symbol, while the computer plays with the O symbol.
3. The player enters moves using coordinates (e.g., A1, B2, C3).
4. The computer makes random moves in an available cell.
5. The game ends when one of the players wins or when the game results in a draw.
   
## Technologies Used

- **Python 3** – The programming language used to implement the application.
- **Simple Algorithm** – The computer randomly selects a move from the available cells.
- **Terminal/Console** – The application runs in a terminal or command prompt.
  
## How the Application Works

The application is based on the following core functionalities:

- **Game Board**: A 3x3 matrix representing the board. Each cell can contain an X or O symbol (or remain empty).
- **Player Moves**: The player inputs the coordinates where they want to place their X symbol. Valid move examples: A1, B2, C3.
- **Computer Moves**: The computer places an O symbol randomly in an empty cell.
- **Winner Verification**: After each move, the application checks if there is a winner or if the game ends in a draw.

## How to Run the Application

1. Save the file as `tic_tac_toe.py`.
2. Open a terminal and navigate to the directory where you saved the file.
3. Run the following command:
   ```bash
   python tic_tac_toe.py
   
