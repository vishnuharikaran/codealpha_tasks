# Stock Portfolio Tracker

A simple text-based console application built using Python 3 to track stock investments, portfolio valuation, and optional CSV report exports.

## Description

The Stock Portfolio Tracker is a command-line application developed for the **CodeAlpha** Python Programming Internship. It allows users to simulate managing a stock portfolio by selecting stock ticker symbols from a hardcoded market dictionary, entering share quantities, calculating individual investment holdings, determining total portfolio value, and optionally exporting the portfolio data to a CSV file.

---

## Features

- **Hardcoded Market Prices**: Stores stock ticker symbols and fixed market prices in a Python dictionary.
- **Interactive Portfolio Builder**: Prompts users to select stocks and enter share quantities.
- **Automatic Quantity Aggregation**: Combines share quantities automatically when duplicate stock symbols are entered.
- **Robust Input Validation**:
  - Validates stock symbols against available market tickers.
  - Normalizes string inputs (converts symbols to uppercase, strips whitespace).
  - Validates share quantities (rejects non-numeric characters, decimals, zeros, and negative numbers).
  - Validates yes/no prompt choices.
- **Investment Calculation**: Computes individual holding values (`Stock Price × Quantity`) and calculates total net portfolio value.
- **Terminal Summary Output**: Renders a formatted tabular breakdown of all stock holdings and total portfolio worth.
- **Optional CSV Export**: Allows users to save their portfolio summary into a CSV file (`portfolio.csv`) using Python's standard `csv` library.

---

## CodeAlpha Requirements Implemented

- ✅ Stored stock names/symbols and prices in a hardcoded Python dictionary.
- ✅ Accepted user input for stock symbols and share quantities.
- ✅ Calculated individual investment values for each stock.
- ✅ Calculated and displayed the total portfolio investment value.
- ✅ Used standard Python built-in modules (`csv`) with zero external libraries or GUI dependencies.
- ✅ Provided an optional CSV export feature (`portfolio.csv`).

---

## Technologies Used

- **Language**: Python 3.x
- **Standard Library**: `csv` (for CSV export handling)
- **User Interface**: Command Line Interface (CLI) / Terminal

---

## Python Concepts Demonstrated

- **Dictionaries**: Mapping stock ticker symbols to prices (`STOCK_PRICES`) and storing dynamic user holdings (`portfolio`).
- **Loops & Control Flow**: Using `while` loops for continuous user prompts, input validation loops, and iteration over dictionary items.
- **Conditional Statements**: Validating input criteria with `if-elif-else` logic.
- **Modular Functions**: Organizing code into clean, single-responsibility functions (`display_available_stocks`, `build_portfolio`, `display_portfolio_summary`, `export_portfolio_to_csv`, `prompt_export_option`, `main`).
- **Input / Output**: Interactive console interface using `input()` and formatted f-strings (`print()`).
- **Exception Handling**: Catching `ValueError`, `EOFError`, and `KeyboardInterrupt` using `try-except` blocks.
- **Arithmetic Calculations**: Performing floating-point calculations (`Price * Quantity`) and running totals.
- **File Handling**: Writing formatted structured data to external CSV files using `with open(...)` and `csv.writer`.

---

## Project Structure

```text
Stock_Portfolio_Tracker/
│
├── stock_tracker.py    # Main application script containing logic and CLI interface
├── README.md           # Professional project documentation
└── portfolio.csv       # (Optional) Generated when the user chooses to save portfolio
```

---

## How to Run

### Prerequisites

- Python 3.x installed on your machine.

### Instructions

1. Clone or download the repository.
2. Open your terminal or command prompt and navigate to the project directory:

   ```bash
   cd Stock_Portfolio_Tracker
   ```

3. Run the application:

   ```bash
   python stock_tracker.py
   ```

---

## How to Use

1. **View Available Stocks**: Upon launching, the application displays a list of available stock symbols (`AAPL`, `TSLA`, `GOOGL`, `MSFT`, `AMZN`) and their market prices.
2. **Select Stock**: Enter a valid stock symbol (e.g., `AAPL`).
3. **Enter Quantity**: Input a positive whole number representing the number of shares owned.
4. **Add Additional Stocks**: When prompted `Would you like to add another stock? (yes/no):`, enter `yes` to add more stocks or `no` to finish.
5. **Review Portfolio Summary**: View the tabular breakdown showing each stock, price, quantity, individual investment value, and the total portfolio value.
6. **Save to CSV**: When asked `Do you want to save your portfolio to a CSV file? (yes/no):`, enter `yes` to export your portfolio to `portfolio.csv`.

---

## Example Output

```text
=============================================
    WELCOME TO STOCK PORTFOLIO TRACKER       
=============================================

--- Available Stocks & Market Prices ---
Symbol     | Price ($) 
-------------------------
AAPL       | $  180.50
TSLA       | $  240.00
GOOGL      | $  140.25
MSFT       | $  370.80
AMZN       | $  145.10
-------------------------

Enter stock symbol: AAPL
Enter quantity for AAPL: 5
Added 5 shares of AAPL to your portfolio.

Would you like to add another stock? (yes/no): yes

Enter stock symbol: TSLA
Enter quantity for TSLA: 2
Added 2 shares of TSLA to your portfolio.

Would you like to add another stock? (yes/no): no

=============================================
              PORTFOLIO SUMMARY              
=============================================
Stock    Price      Quantity   Value       
---------------------------------------------
AAPL     $180.50    5          $902.50     
TSLA     $240.00    2          $480.00     
---------------------------------------------
Total Portfolio Value: $1,382.50
=============================================

Do you want to save your portfolio to a CSV file? (yes/no): yes

Portfolio saved successfully to portfolio.csv
```

---

## Future Improvements

*(Note: The following are optional potential enhancements for future development and are not part of the current CodeAlpha project release)*

- **Real-Time Market Data**: Integrate financial APIs (e.g., Alpha Vantage, Yahoo Finance) to fetch live stock prices.
- **Profit / Loss Tracking**: Allow users to enter buy prices to calculate unrealized gains or losses.
- **Graphical User Interface (GUI)**: Develop a desktop interface using `Tkinter` or web dashboard using `Flask`/`Streamlit`.
- **Persistent Database**: Store portfolio history in an SQLite database.
