"""Tic Tac Toe game - two players take turns on a 3x3 board."""

from typing import Optional

BOARD_SIZE = 3
EMPTY = " "
PLAYERS = ("X", "O")
# Cells a-i map left-to-right, top-to-bottom: a b c / d e f / g h i
CELL_LETTERS = "abcdefghi"


def create_board() -> list[list[str]]:
    """Create an empty 3x3 board."""
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board: list[list[str]]) -> None:
    """Print the board; empty cells show their letter (a-i), taken cells show X or O."""
    print()
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            cell = board[row][col]
            display = CELL_LETTERS[row * BOARD_SIZE + col] if cell == EMPTY else cell
            print(f" {display} ", end="")
            if col < BOARD_SIZE - 1:
                print("|", end="")
        print()
        if row < BOARD_SIZE - 1:
            print("---+" * (BOARD_SIZE - 1) + "---")


def letter_to_position(letter: str) -> tuple[int, int]:
    """Convert a-i to (row, col)."""
    idx = CELL_LETTERS.index(letter.lower())
    return idx // BOARD_SIZE, idx % BOARD_SIZE


def get_move(board: list[list[str]], player: str) -> tuple[int, int]:
    """Ask the player for a letter a-i for the cell to play."""
    while True:
        choice = input(f"Player {player}, choose a cell (a-i): ").strip().lower()
        if len(choice) != 1:
            print("Enter a single letter (a-i). Try again.")
            continue
        if choice not in CELL_LETTERS:
            print("Letter must be a, b, c, d, e, f, g, h, or i. Try again.")
            continue
        row, col = letter_to_position(choice)
        if board[row][col] == EMPTY:
            return row, col
        print("That cell is already taken. Try again.")


def check_winner(board: list[list[str]]) -> Optional[str]:
    """Return the winning player (X or O), or None if no winner yet."""
    # Rows
    for row in range(BOARD_SIZE):
        if board[row][0] != EMPTY and all(
            board[row][c] == board[row][0] for c in range(BOARD_SIZE)
        ):
            return board[row][0]
    # Columns
    for col in range(BOARD_SIZE):
        if board[0][col] != EMPTY and all(
            board[r][col] == board[0][col] for r in range(BOARD_SIZE)
        ):
            return board[0][col]
    # Diagonals
    if board[0][0] != EMPTY and all(
        board[i][i] == board[0][0] for i in range(BOARD_SIZE)
    ):
        return board[0][0]
    if board[0][BOARD_SIZE - 1] != EMPTY and all(
        board[i][BOARD_SIZE - 1 - i] == board[0][BOARD_SIZE - 1]
        for i in range(BOARD_SIZE)
    ):
        return board[0][BOARD_SIZE - 1]
    return None


def is_full(board: list[list[str]]) -> bool:
    """Return True if every cell is filled."""
    return all(board[r][c] != EMPTY for r in range(BOARD_SIZE) for c in range(BOARD_SIZE))


def main() -> None:
    print("Welcome to Tic Tac Toe!")
    print("Players X and O take turns. Type a letter (a-i) to place your mark.")
    print("  a b c")
    print("  d e f")
    print("  g h i\n")
    board = create_board()
    turn = 0

    while True:
        player = PLAYERS[turn % 2]
        print_board(board)
        row, col = get_move(board, player)
        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"\nPlayer {winner} wins!")
            break
        if is_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        turn += 1


if __name__ == "__main__":
    main()