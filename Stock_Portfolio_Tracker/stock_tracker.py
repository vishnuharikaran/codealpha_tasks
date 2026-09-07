"""
CodeAlpha - Stock Portfolio Tracker
A simple console-based Stock Portfolio Tracker built with Python 3.
"""

import csv

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


def export_portfolio_to_csv(portfolio, filename="portfolio.csv"):
    """Export portfolio details and total investment value to a CSV file."""
    if not portfolio:
        print("Portfolio is empty. Nothing to save.")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            # Write header row
            writer.writerow(["Stock Symbol", "Price per Share", "Quantity", "Investment Value"])

            total_portfolio_value = 0.0

            # Write stock data rows
            for symbol, quantity in portfolio.items():
                price = STOCK_PRICES[symbol]
                stock_value = price * quantity
                total_portfolio_value += stock_value
                writer.writerow([symbol, price, quantity, stock_value])

            # Write total portfolio value row
            writer.writerow(["Total Portfolio Value", "", "", total_portfolio_value])

        print(f"\nPortfolio saved successfully to {filename}")

    except Exception as error:
        print(f"\nError saving portfolio to CSV: {error}")


def prompt_export_option(portfolio):
    """Prompt the user whether to save portfolio to a CSV file with validation."""
    if not portfolio:
        return

    while True:
        try:
            choice = input("\nDo you want to save your portfolio to a CSV file? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            choice = "no"

        if choice in ["yes", "y"]:
            export_portfolio_to_csv(portfolio)
            break
        elif choice in ["no", "n"]:
            print("\nPortfolio was not saved.")
            break
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")


def main():
    """Main entry point for the Stock Portfolio Tracker application."""
    print("=" * 45)
    print("    WELCOME TO STOCK PORTFOLIO TRACKER       ")
    print("=" * 45)

    # Display available stock prices
    display_available_stocks()

    # Build user portfolio
    user_portfolio = build_portfolio()

    # Calculate and display portfolio summary
    display_portfolio_summary(user_portfolio)

    # Phase 6: Save to CSV option
    prompt_export_option(user_portfolio)


if __name__ == "__main__":
    main()




