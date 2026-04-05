# 📈 MAANG Stock Analyzer

A Python-based interactive tool to visualize and analyze **MAANG stocks** (Meta, Apple, Amazon, Netflix, Google) using candlestick charts and summary statistics.

---

## 🚀 Features
- **Interactive Menu**: Choose between Meta, Apple, Amazon, Netflix, and Google.
- **Data Cleaning**: Drops rows with missing tickers and standardizes column names.
- **Summary Stats**: Displays highest high and lowest low for the selected stock.
- **Candlestick Charts**: Plots price history with optional volume overlay.
- **Custom Styling**: Uses `mplfinance` with a dark theme and green/red color palette.
- **Loop Control**: Replay analysis or exit gracefully.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Libraries**:
  - `pandas` – data handling
  - `mplfinance` – candlestick chart visualization

---

## 📦 Installation
Install dependencies:

```bash
pip install pandas mplfinance