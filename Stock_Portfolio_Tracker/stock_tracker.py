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
    """Interactively build a portfolio dictionary from user input with strict validation."""
    portfolio = {}

    while True:
        # Step 1: Stock Symbol Input & Validation
        symbol = ""
        while True:
            try:
                symbol = input("\nEnter stock symbol: ").strip().upper()
            except (EOFError, KeyboardInterrupt):
                print("\nPortfolio entry cancelled.")
                return portfolio

            if symbol in STOCK_PRICES:
                break
            else:
                print("Invalid stock symbol. Please choose from the available stocks.")

        # Step 2: Quantity Input & Validation
        quantity = 0
        while True:
            try:
                quantity_input = input(f"Enter quantity for {symbol}: ").strip()
                quantity = int(quantity_input)
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid whole number.")
            except (EOFError, KeyboardInterrupt):
                print("\nPortfolio entry cancelled.")
                return portfolio

        # Combine or store stock quantity
        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"Added {quantity} more shares of {symbol}. Total shares: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f"Added {quantity} shares of {symbol} to your portfolio.")

        # Step 3: Add Another Stock Confirmation & Validation
        add_more = False
        while True:
            try:
                again = input("\nWould you like to add another stock? (yes/no): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                again = "no"

            if again in ["yes", "y"]:
                add_more = True
                break
            elif again in ["no", "n"]:
                add_more = False
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")

        if not add_more:
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



