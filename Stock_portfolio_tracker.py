import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input(f"\nEnter stock name {i + 1}: ").upper()

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        portfolio[stock_name] = quantity

        investment_value = stock_prices[stock_name] * quantity
        total_investment += investment_value
    else:
        print("Stock not found in price list!")

print("\n" + "=" * 40)
print("         STOCK PORTFOLIO REPORT")
print("=" * 40)

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock:<10} Qty: {quantity:<5} Value: ${value}")

print("-" * 40)
print(f"Total Investment Value: ${total_investment}")
print("=" * 40)

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["STOCK PORTFOLIO REPORT"])
    writer.writerow([])

    writer.writerow(
        ["Stock Symbol", "Quantity", "Price per Share ($)", "Investment Value ($)"]
    )

    for stock, quantity in portfolio.items():
        writer.writerow([
            stock,
            quantity,
            stock_prices[stock],
            stock_prices[stock] * quantity
        ])

    writer.writerow([])
    writer.writerow(["Total Investment Value ($)", total_investment])

print("\nPortfolio data has been saved to 'portfolio.csv'")