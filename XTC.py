import alpaca_trade_api as tradeapi

# Replace with your Alpaca API keys
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'  # Use the paper trading URL
APCA_API_KEY_ID = 'YOUR_API_KEY_ID'
APCA_API_SECRET_KEY = 'YOUR_API_SECRET_KEY'

# Initialize the Alpaca API client
api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, api_version='v2')

# Define the stock symbols
source_stock_symbol = 'AMD'
target_stock_symbol = 'INTC'

# Define the percentage of shares to trade (10%)
percentage_to_trade = 0.10

# Get account information
account = api.get_account()

# Get the current portfolio holdings
portfolio = api.list_positions()

# Find the number of shares of source_stock_symbol in the portfolio
source_stock_position = next((position for position in portfolio if position.symbol == source_stock_symbol), None)
if source_stock_position is not None:
    source_stock_qty = float(source_stock_position.qty)
else:
    source_stock_qty = 0.0

# Calculate the number of shares to trade
shares_to_trade = int(source_stock_qty * percentage_to_trade)

# Check if you have enough shares to trade
if shares_to_trade > 0:
    # Submit a market order to sell shares of source_stock_symbol
    api.submit_order(
        symbol=source_stock_symbol,
        qty=shares_to_trade,
        side='sell',
        type='market',
        time_in_force='gtc'
    )

    # Submit a market order to buy shares of target_stock_symbol
    api.submit_order(
        symbol=target_stock_symbol,
        qty=shares_to_trade,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

    print(f"Traded {shares_to_trade} shares from {source_stock_symbol} to {target_stock_symbol}.")
else:
    print(f"No shares of {source_stock_symbol} available to trade.")
