import yfinance as yf
import pandas as pd
import locale

#Tapi Goredema
# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def fetch_basic_stock_data():
    """Fetch and display basic stock data (ticker, company name, current price)."""
    symbols = input("Enter stock symbols separated by a comma: ").split(',')

    stock_data = []
    for symbol in symbols:
        symbol = symbol.strip().upper()
        stock = yf.Ticker(symbol)
        info = stock.info

        try:
            stock_data.append([
                symbol,
                info['longName'],
                locale.currency(info['regularMarketPrice'], grouping=True)
            ])
        except KeyError:
            print(f"Error fetching data for {symbol}")

    df = pd.DataFrame(stock_data, columns=["Stock Ticker", "Company", "Current Market Price"])
    print("\nBasic Stock Data:")
    print(df)


def fetch_additional_data():
    """Fetch 52-week high, 52-week low, and Return on Assets (ROA)."""
    symbols = input("Enter stock symbols separated by a comma: ").split(',')

    stock_data = []
    for symbol in symbols:
        symbol = symbol.strip().upper()
        stock = yf.Ticker(symbol)
        info = stock.info

        try:
            stock_data.append([
                symbol,
                locale.currency(info.get('fiftyTwoWeekHigh', 0), grouping=True),
                locale.currency(info.get('fiftyTwoWeekLow', 0), grouping=True),
                info.get('returnOnAssets', "N/A")
            ])
        except KeyError:
            print(f"Error fetching data for {symbol}")

    df = pd.DataFrame(stock_data, columns=["Stock Ticker", "52-Week High", "52-Week Low", "ROA"])
    print("\nAdditional Stock Data:")
    print(df)


def fetch_trending_stocks():
    """Fetch trending stocks and their data (Current Price, 52-Week High & Low)."""
    trending_stocks = ["AAPL", "TSLA", "GOOGL"]  # Example trending stocks

    stock_data = []
    for symbol in trending_stocks:
        stock = yf.Ticker(symbol)
        info = stock.info

        try:
            stock_data.append([
                info['longName'],
                symbol,
                locale.currency(info.get('regularMarketPrice', 0), grouping=True),
                locale.currency(info.get('fiftyTwoWeekHigh', 0), grouping=True),
                locale.currency(info.get('fiftyTwoWeekLow', 0), grouping=True)
            ])
        except KeyError:
            print(f"Error fetching data for {symbol}")

    df = pd.DataFrame(stock_data, columns=["Stock Name", "Ticker", "Current Price", "52-Week High", "52-Week Low"])
    print("\nTrending Stocks:")
    print(df)


def main():
    """Main menu to select options."""
    while True:
        print("\nFinance API Data Fetcher")
        print("1. Fetch Basic Stock Data")
        print("2. Fetch Additional Data (52-Week High, Low, ROA)")
        print("3. Fetch Trending Stocks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            fetch_basic_stock_data()
        elif choice == '2':
            fetch_additional_data()
        elif choice == '3':
            fetch_trending_stocks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()
