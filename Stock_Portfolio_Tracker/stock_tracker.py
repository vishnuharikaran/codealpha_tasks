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


def build_portfolio():
    """Interactively build a portfolio dictionary from user input."""
    portfolio = {}

    while True:
        try:
            symbol = input("\nEnter a stock symbol to add (e.g., AAPL): ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nPortfolio entry cancelled.")
            break

        # Validate symbol against available stock price dictionary
        if symbol not in STOCK_PRICES:
            print(f"Invalid symbol '{symbol}'! Please choose from the available stock list.")
            continue

        # Get valid integer quantity from user
        try:
            quantity_input = input(f"Enter quantity of shares for {symbol}: ").strip()
            quantity = int(quantity_input)
            if quantity <= 0:
                print("Quantity must be a positive integer greater than 0.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number for quantity.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nPortfolio entry cancelled.")
            break

        # Combine quantity if stock already exists in portfolio, otherwise add new key
        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"Added {quantity} more shares of {symbol}. Total shares: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f"Added {quantity} shares of {symbol} to your portfolio.")

        # Ask if user wants to add another stock
        try:
            again = input("\nWould you like to add another stock? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            again = "no"

        if again not in ["yes", "y"]:
            break

    return portfolio


def display_portfolio_summary(portfolio):
    """Calculate and display individual stock investment values and total portfolio value."""
    print("\n" + "=" * 45)
    print("              PORTFOLIO SUMMARY              ")
    print("=" * 45)

    if not portfolio:
        print("Your portfolio is currently empty.")
        print("-" * 45)
        print("Total Portfolio Value: $0.00")
        print("=" * 45)
        return

    print(f"{'Stock':<8} {'Price':<10} {'Quantity':<10} {'Value':<12}")
    print("-" * 45)

    total_portfolio_value = 0.0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        stock_value = price * quantity
        total_portfolio_value += stock_value
        print(f"{symbol:<8} ${price:<9.2f} {quantity:<10} ${stock_value:<11.2f}")

    print("-" * 45)
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print("=" * 45)


def main():
    """Main entry point for the Stock Portfolio Tracker application."""
    print("=" * 45)
    print("    WELCOME TO STOCK PORTFOLIO TRACKER       ")
    print("=" * 45)

    # Display available stock prices
    display_available_stocks()

    # Build user portfolio
    user_portfolio = build_portfolio()

    # Calculate and display portfolio summary (Phase 4)
    display_portfolio_summary(user_portfolio)


if __name__ == "__main__":
    main()



