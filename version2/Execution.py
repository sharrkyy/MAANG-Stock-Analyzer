from Stock import Menu, Stock

if __name__ == "__main__":
    stock_obj = Stock()
    main_menu = Menu(stock_obj.df, stock_obj.style)
    main_menu.show_menu()