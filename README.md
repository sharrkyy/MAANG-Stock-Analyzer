# 📊 Stock Analyzer

This project has two versions:

- **Version 1** → Basic procedural design with a single loop and if/elif menu (see folder `v1/`)
- **Version 2** → Updated OOP design with classes, recursion, and dictionary dispatch (see folder `v2/`)

## ✨ Key Highlights (Version 2)
- 🔄 Menu replay uses recursion (no loops at all).
- 📑 Menu choices handled with dictionary dispatch (no long if/elif chains).
- 🧩 Modular design with separate classes (`Stock`, `Summary`, `Plot`, `Menu`).
- 📊 Candlestick chart plotting with **mplfinance** and custom styles.
- 📝 Summary values extracted directly from the dataframe (manual filtering).
- 😎 Casual error and exit messages add personality to the program.

## 🔀 Difference from Version 1
- **Version 1**: Used a `while True` loop with if/elif for menu handling, all logic mixed together.
- **Version 2**: Removes loops entirely, uses recursion + dictionary dispatch, and organizes functionality into modular classes for summary and plotting.

## ▶️ How to Run
Go into the folder you want and run:
