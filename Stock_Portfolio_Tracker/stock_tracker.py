"""
CodeAlpha - Stock Portfolio Tracker
A simple console-based Stock Portfolio Tracker built with Python 3.
"""

# Hardcoded dictionary containing stock symbols and their fixed market prices
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 240.00,
    "GOOGL": 140.25,
    "MSFT": 370.80,
    "AMZN": 145.10
}


def display_available_stocks():
    """Display all available stock symbols and their corresponding prices."""
    print("\n--- Available Stocks & Market Prices ---")
    print(f"{'Symbol':<10} | {'Price ($)':<10}")
    print("-" * 25)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} | ${price:>8.2f}")
    print("-" * 25)


def main():
    """Main entry point for the Stock Portfolio Tracker application."""
    print("=" * 45)
    print("    WELCOME TO STOCK PORTFOLIO TRACKER       ")
    print("=" * 45)

    # Display available stock prices (Phase 2)
    display_available_stocks()


if __name__ == "__main__":
    main()

