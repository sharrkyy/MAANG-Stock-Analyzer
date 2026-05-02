# 📊 Stock Analyzer (Version 2)

## ✨ Key Highlights
- 🔄 Menu replay uses **recursion** (no loops at all).
- 📑 Menu choices handled with **dictionary dispatch** (no long if/elif chains).
- 🧩 Modular design with separate classes (`Stock`, `Summary`, `Plot`, `Menu`).
- 📊 Candlestick chart plotting with **mplfinance** and custom styles.
- 📝 Summary values extracted directly from the dataframe (manual filtering).
- 😎 Casual error and exit messages add personality to the program.

## 🔀 Difference from Version 1
- **Version 1**: Used a `while True` loop with if/elif for menu handling, all logic mixed together.
- **Version 2**: Removes loops entirely, uses recursion + dictionary dispatch, and organizes functionality into modular classes for summary and plotting.
