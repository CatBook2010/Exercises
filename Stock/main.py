from stock import Stock

stock = Stock("Intc", "Intel Corporation", 20.5, 20.35)

print(f"Change Percent = {stock.getChangePercent()}%")