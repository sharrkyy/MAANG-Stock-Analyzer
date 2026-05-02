import pandas as pd
import mplfinance as mpf

# Reads the csv file
class Stock:
    def __init__(self):
        self.df = pd.read_csv("Stock.csv", parse_dates=["Date"], sep=None, engine="python")
        self.df = self.df.dropna(subset=["Ticker"])
        self.df.columns = [c.strip().capitalize() for c in self.df.columns]
        self.df.set_index("Date", inplace=True)

        # Setting the colors and design
        self.colors = mpf.make_marketcolors(up="green",
                                            down="red",
                                            volume="in")

        self.style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=self.colors)

    def data(self):
        return self.df

# Shows a brief summary of the csv file
class Summary:
    def __init__(self, df):
        self.df = df

    def show_summary(self, ticker):
        stock_df = self.df[self.df["Ticker"] == ticker].copy()

        if stock_df.empty:
            print(f"\n--- {ticker} Highlights ---")
            print(f"Sorry Mate, but no {ticker} in the file :( ")
            return

        print(f"\n--- {ticker} Highlights ---")

        # For the highest value
        highest_val = stock_df["High"].max()
        highest_day = stock_df[stock_df["High"] == highest_val].index[0].date()

        # For the lowest value
        lowest_val = stock_df["Low"].min()
        lowest_day = stock_df[stock_df["Low"] == lowest_val].index[0].date()

        # Prints the highest and lowest value
        print(f"Highest: {highest_val} on {highest_day}")
        print(f"Lowest:  {lowest_val} on {lowest_day}")


# Plotting the Tickers
class Plot:
    def __init__(self, df, style, ticker):
        stock_df = df[df["Ticker"] == ticker].copy()
        has_vol = "Volume" in stock_df.columns

        # Designing the candle 
        mpf.plot(stock_df,
                 type="candle",
                 title=f"{ticker} Chart",
                 style=style,
                 volume=has_vol,
                 tight_layout=True)


# Shows the menu for user choice
class Menu:
    def __init__(self, df, style):
        self.df = df
        self.style = style
        self.summary = Summary(df)

    def show_menu(self):
        print("\nThe Stock Menu:")

        # THe menu bar
        print("1. Display Summary statistics | 2. Meta(Facebook) | 3. Apple | 4. Amazon | 5. Netflix | 6. Google | 7. Exit")

        try:
            choice = int(input("Choose a number: "))
        except ValueError:
            print("Oops, that’s not possible. Try again, dude.")
            return self.show_menu()

        actions = {
            1: self.run_summary,
            2: self.run_meta,
            3: self.run_apple,
            4: self.run_amazon,
            5: self.run_netflix,
            6: self.run_google,
            7: self.exit_program
        }

        if choice in actions:
            actions[choice]()
        else:
            print("Not an option, bro.")

        if choice != 7:
            return self.show_menu()

    def run_summary(self):
        self.summary.show_summary("META")
        self.summary.show_summary("AAPL")
        self.summary.show_summary("AMZN")
        self.summary.show_summary("NFLX")
        self.summary.show_summary("GOOG")

    def run_meta(self):
        self.summary.show_summary("META")
        Plot(self.df, self.style, "META")

    def run_apple(self):
        self.summary.show_summary("AAPL")
        Plot(self.df, self.style, "AAPL")

    def run_amazon(self):
        self.summary.show_summary("AMZN")
        Plot(self.df, self.style, "AMZN")

    def run_netflix(self):
        self.summary.show_summary("NFLX")
        Plot(self.df, self.style, "NFLX")

    def run_google(self):
        self.summary.show_summary("GOOG")
        Plot(self.df, self.style, "GOOG")

    def exit_program(self):
        print("Bye bye Brotha! :)")


