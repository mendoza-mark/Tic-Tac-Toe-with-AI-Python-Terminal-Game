import os
import random
import re


def clear_screen():
    """Clear the terminal screen for a fresh board display."""
    os.system("cls" if os.name == "nt" else "clear")


SCREEN_WIDTH = 33
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m")


def color_mark(value):
    """Return a colored X or O, otherwise return the value unchanged."""
    if value == "X":
        return f"{RED}{value}{RESET}"
    if value == "O":
        return f"{GREEN}{value}{RESET}"
    return value


def format_cell(board, index):
    """Return the string to display for a board cell."""
    value = board[index]
    return color_mark(value) if value != " " else str(index + 1)


def print_divider(char="="):
    """Print a full-width divider line."""
    print(char * SCREEN_WIDTH)


def visible_length(text):
    """Return the visible length of text without ANSI escape codes."""
    return len(ANSI_ESCAPE.sub("", text))


def print_center(text):
    """Print centered text with fixed screen width."""
    visible = visible_length(text)
    padding = max((SCREEN_WIDTH - visible) // 2, 0)
    print(" " * padding + text)


def print_section(title):
    """Print a titled section header."""
    print_divider("-")
    print_center(title)
    print_divider("-")


def prompt_input(label):
    """Ask a single input question with a consistent prompt style."""
    return input(f"{label}: ").strip()


def prompt_choice(label, options):
    """Ask for a choice from a set of options."""
    options_text = "/".join(options)
    while True:
        choice = input(f"{label} [{options_text}]: ").strip().lower()
        if choice in options:
            return choice
        print(f"Please choose one of: {options_text}")


def display_board(board, settings, score, current_player=None):
    """Render the board and current game information."""
    clear_screen()
    title = "TIC-TAC-TOE"
    print_divider("=")
    print_center(title)
    print_divider("=")

    player_turn = ""
    if current_player:
        player_name = settings["names"][current_player]
        player_turn = f"{player_name} ({current_player})"
    print_center(f"Mode: {settings['mode_label']}   Turn: {player_turn}")
    print_divider("-")
    print_center(f"Score: {settings['names']['X']} {score['X']}  |  {settings['names']['O']} {score['O']}  |  Ties {score['Ties']}")
    print_divider("-")

    cells = [format_cell(board, i) for i in range(9)]
    print_center(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print_center("---+---+---")
    print_center(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print_center("---+---+---")
    print_center(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print_divider("=")


def initialize_board():
    """Create a new empty board."""
    return [" "] * 9


def is_winner(board, player):
    """Return True if the player has a winning line."""
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in winning_lines)


def is_board_full(board):
    """Return True if there are no empty squares."""
    return all(cell != " " for cell in board)


def get_menu_choice(prompt, options):
    """Prompt until the user enters one of the allowed options."""
    return prompt_choice(prompt, options)


def get_player_move(board, player_name, player_symbol):
    """Ask the current player for a valid move."""
    valid_moves = [str(i + 1) for i, square in enumerate(board) if square == " "]
    prompt = f"{player_name} ({player_symbol}), choose a position"
    while True:
        move = input(f"{prompt} [{', '.join(valid_moves)}]: ").strip()
        if move in valid_moves:
            return int(move) - 1
        print("Invalid selection. Pick an empty number from the board.")


def choose_game_mode():
    """Let the user choose two-player or single-player mode."""
    clear_screen()
    print_section("GAME MODE")
    print("1) Two-player local")
    print("2) Single player vs AI")
    choice = get_menu_choice("Mode", ["1", "2"])
    return "human" if choice == "1" else "ai"


def choose_ai_difficulty():
    """Let the user choose AI difficulty."""
    print_section("AI DIFFICULTY")
    print("1) Easy (random moves)")
    print("2) Hard (unbeatable)")
    choice = get_menu_choice("Difficulty", ["1", "2"])
    return "easy" if choice == "1" else "hard"


def choose_player_name(default_name):
    """Read a player name or use the default."""
    return prompt_input(f"Enter a name for {default_name} (leave blank for {default_name})") or default_name


def choose_human_symbol():
    """Ask whether the human wants to play as X or O."""
    print_section("CHOOSE SYMBOL")
    print("1) X (goes first)")
    print("2) O")
    choice = get_menu_choice("Symbol", ["1", "2"])
    return "X" if choice == "1" else "O"


def get_ai_move(board, ai_player, human_player, difficulty):
    """Choose the best move for the AI."""
    empty_cells = [idx for idx, square in enumerate(board) if square == " "]
    if difficulty == "easy":
        return random.choice(empty_cells)

    best_score = -2
    best_move = None
    for index in empty_cells:
        board[index] = ai_player
        score = minimax(board, human_player, ai_player, human_player)
        board[index] = " "
        if score > best_score:
            best_score = score
            best_move = index
    return best_move


def minimax(board, current_player, ai_player, human_player):
    """Recursively evaluate positions using minimax."""
    if is_winner(board, ai_player):
        return 1
    if is_winner(board, human_player):
        return -1
    if is_board_full(board):
        return 0

    if current_player == ai_player:
        best_score = -2
        for index, square in enumerate(board):
            if square == " ":
                board[index] = current_player
                score = minimax(board, human_player, ai_player, human_player)
                board[index] = " "
                best_score = max(best_score, score)
        return best_score

    best_score = 2
    for index, square in enumerate(board):
        if square == " ":
            board[index] = current_player
            score = minimax(board, ai_player, ai_player, human_player)
            board[index] = " "
            best_score = min(best_score, score)
    return best_score


def build_game_settings(mode):
    """Collect names, symbols, and settings for a single match."""
    settings = {"mode": mode, "names": {}, "mode_label": ""}
    if mode == "human":
        settings["names"]["X"] = choose_player_name("Player 1")
        settings["names"]["O"] = choose_player_name("Player 2")
        settings["mode_label"] = "Local Multiplayer"
        settings["ai_difficulty"] = None
    else:
        settings["names"]["X"] = choose_player_name("You")
        choice = choose_ai_difficulty()
        symbol = choose_human_symbol()
        ai_symbol = "O" if symbol == "X" else "X"
        human_symbol = symbol
        settings["names"][human_symbol] = settings["names"]["X"]
        settings["names"][ai_symbol] = "Computer"
        settings["human_symbol"] = human_symbol
        settings["ai_symbol"] = ai_symbol
        settings["ai_difficulty"] = choice
        settings["mode_label"] = f"AI ({choice.capitalize()})"
    return settings


def play_game(settings, score):
    """Execute one round of Tic-Tac-Toe using the current settings."""
    board = initialize_board()
    current_player = "X"

    while True:
        display_board(board, settings, score, current_player)

        if settings["mode"] == "ai" and current_player == settings["ai_symbol"]:
            print("AI is thinking...")
            move_index = get_ai_move(board, settings["ai_symbol"], settings["human_symbol"], settings["ai_difficulty"])
        else:
            move_index = get_player_move(board, settings["names"][current_player], current_player)

        board[move_index] = current_player

        if is_winner(board, current_player):
            score[current_player] += 1
            display_board(board, settings, score)
            winner = settings["names"][current_player]
            print(f"{winner} ({current_player}) wins! 🎉")
            break

        if is_board_full(board):
            score["Ties"] += 1
            display_board(board, settings, score)
            print("It's a tie! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"


def play_again(prompt):
    """Ask the user whether they want to continue."""
    choice = get_menu_choice(prompt, ["y", "n"])
    return choice == "y"


def main():
    """Main game loop with replay and settings selection."""
    score = {"X": 0, "O": 0, "Ties": 0}
    settings = None

    while True:
        clear_screen()
        print_divider("=")
        print_center("WELCOME TO TIC-TAC-TOE")
        print_divider("=")
        print_center("Multiplayer or single-player vs AI")
        print_divider("-")
        print_center("Board positions")
        print_center(" 1 | 2 | 3 ")
        print_center("---+---+---")
        print_center(" 4 | 5 | 6 ")
        print_center("---+---+---")
        print_center(" 7 | 8 | 9 ")
        print_divider("=")
        input("Press Enter to continue...")

        mode = choose_game_mode()
        settings = build_game_settings(mode)
        score = {"X": 0, "O": 0, "Ties": 0}

        while True:
            play_game(settings, score)
            if not play_again("Play another round with the same settings? (y/n)"):
                break

        if not play_again("Choose a different mode or quit? (y/n)"):
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
