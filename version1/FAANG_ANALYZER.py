import pandas as pd
import mplfinance as mpf

# Reading from the csv file
df = pd.read_csv("Stock.csv", parse_dates=["Date"])

df = df.dropna(subset=["Ticker"])
df.columns = [c.strip().capitalize() for c in df.columns]
df.set_index("Date", inplace=True)

# Making the color palette
colors = mpf.make_marketcolors(up="green",
                               down="red",
                               wick="inherit",
                               edge="inherit",
                               volume="in")

mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)

print("Welcome to MAANG Stock Analyzer!")

while True:
    print("1 -> Meta (Facebook)")
    print("2 -> Apple")
    print("3 -> Amazon")
    print("4 -> Netflix")
    print("5 -> Google")
    print("6 -> Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice, enter a number.")
        continue

    if choice == 1:
        ticker = "META"
        title = "META (Facebook) Price History"
    elif choice == 2:
        ticker = "AAPL"
        title = "Apple Price History"
    elif choice == 3:
        ticker = "AMZN"
        title = "Amazon Price History"
    elif choice == 4:
        ticker = "NFLX"
        title = "Netflix Price History"
    elif choice == 5:
        ticker = "GOOG"
        title = "Google Price History"
    elif choice == 6:
        print("BYE BOII")
        break
    else:
        print("Error detected, choose again.")
        continue

    # Filtering by ticker
    stock_df = df[df["Ticker"] == ticker].copy()

    # Summary of the stocks
    summary = pd.DataFrame({
        "Highest High": [stock_df["High"].max()],
        "Lowest Low": [stock_df["Low"].min()]
    })
    print(summary)

    # 3. Plotting the stocks
    has_vol = "Volume" in stock_df.columns

    mpf.plot(stock_df,
             type="candle",
             title=title,
             style=mpf_style,
             volume=has_vol,
             tight_layout=True)

    # Replaying or quiting the loop
    print("\n1) Again")
    print("2) Exit")

    try:
        choice = int(input("Enter your decision: "))
        if choice == 2:
            print("Thank you my brotha")
            break
    except ValueError:
        continue
