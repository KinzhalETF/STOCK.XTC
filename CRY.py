import ccxt

# Initialize the Binance exchange
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
})

# Define the trade parameters
symbol = 'BTC/USDT'  # Replace with the trading pair you want
side = 'buy'         # 'buy' or 'sell'
quantity = 0.01      # The amount of cryptocurrency to buy/sell
price = 50000        # The price at which to buy/sell (optional for market orders)

# Create an order
try:
    if side == 'buy':
        order = exchange.create_limit_buy_order(symbol, quantity, price)
    elif side == 'sell':
        order = exchange.create_limit_sell_order(symbol, quantity, price)
    else:
        raise ValueError("Invalid side. Use 'buy' or 'sell'.")

    print(f"Order created successfully:\n{order}")
except Exception as e:
    print(f"Error creating order: {e}")
