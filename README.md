# Tic-Tac-Toe-with-AI-Python-Terminal-Game
A fully-featured, terminal-based Tic-Tac-Toe game written in Python, built as a hands-on practice project in implementing small-scale Artificial Intelligence using the classic Minimax algorithm. This project explores the fundamentals of game-tree search and decision-making logic within a simple, well-structured Python application.

---

## 👤 Author

**Mark Droeid Mendoza**
Bachelor of Science in Information Technology
Batangas State University — JPLPC Malvar Campus

- 📧 Email: [markdroeidmendoza@gmail.com](mailto:markdroeidmendoza@gmail.com)
- 🐙 GitHub: [@mendoza-mark](https://github.com/mendoza-mark)

---

## 🧠 About This Project

This project was developed as a **practice exercise in building a small AI opponent in Python**. The core AI is powered by the **Minimax algorithm** — a well-known decision-making algorithm used in two-player zero-sum games. When set to *Hard* difficulty, the AI is theoretically unbeatable, always choosing the optimal move by recursively evaluating all possible future game states.

This makes the project an excellent starting point for understanding:
- How game trees work
- How an AI can "look ahead" to anticipate outcomes
- The difference between a naive (random) agent and an optimal one

---

## ✨ Features

### 🎮 Two Game Modes
- **Local Multiplayer** — Two human players take turns on the same machine.
- **Single Player vs AI** — One human player faces off against a computer opponent.

### 🤖 AI Opponent with Two Difficulty Levels
- **Easy Mode** — The AI picks moves completely at random, making it a suitable opponent for beginners or casual play.
- **Hard Mode (Unbeatable)** — The AI uses the **Minimax algorithm** to evaluate every possible board state and always play the optimal move. It cannot be beaten — only tied at best.

### 🪙 Symbol Selection
- In Single Player mode, the human player can choose to play as **X** (goes first) or **O**.
- The AI is automatically assigned the remaining symbol.

### 👤 Custom Player Names
- Players can enter custom names before the game starts.
- Names are displayed on the board header and in win/tie announcements.

### 📊 Persistent Score Tracking
- Scores for both players (and ties) are tracked across multiple rounds within the same session.
- The scoreboard is displayed on the board at all times.

### 🔁 Replay System
- After each round, players are prompted to **play again with the same settings** or **return to the mode selection screen**.
- This allows for quick rematches without re-entering names or settings.

### 🎨 Colored Terminal Output
- **X** is displayed in **red** and **O** in **green** using ANSI escape codes for a more visually distinct board.
- ANSI-aware centering ensures the board stays properly aligned despite invisible color characters.

### 🖥️ Clean Terminal UI
- The screen is cleared between turns for a clean, distraction-free display.
- The board layout, scores, current turn, and game mode are all shown in a structured, centered format on every refresh.

---

## 🗂️ Project Structure

```
tiktaktoe.py       # Single-file Python application, no external dependencies
README.md          # Project documentation
```

---

## 🚀 How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python tiktaktoe.py
```

> On some systems, use `python3` instead of `python`.

---

## 🔬 How the AI Works

The AI in Hard Mode uses the **Minimax algorithm**, a recursive strategy where the AI simulates every possible sequence of moves until the end of the game. For each terminal state (win, loss, or tie), it assigns a score:

| Outcome       | Score |
|---------------|-------|
| AI wins       | `+1`  |
| Human wins    | `-1`  |
| Tie           | `0`   |

The AI then works backwards through the game tree:
- When it's the **AI's turn**, it picks the move with the **highest** score.
- When it's the **human's turn**, it assumes the **lowest** score (worst case for AI).

This guarantees that the AI will never lose — it always finds the path that leads to a win or, at minimum, a draw.

```python
# Simplified view of the core Minimax logic
def minimax(board, current_player, ai_player, human_player):
    if is_winner(board, ai_player):   return 1
    if is_winner(board, human_player): return -1
    if is_board_full(board):          return 0

    # Maximize for AI, minimize for human
    ...
```

---

## 📌 Notes

- This is a **learning/practice project** and is not intended for production use.
- The Minimax implementation runs without pruning (no Alpha-Beta optimization), which is intentional for simplicity and readability.
- The project is entirely self-contained in a single `.py` file with no third-party dependencies.

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 GROUP 2 - BSIT-1203

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
