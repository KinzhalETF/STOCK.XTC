import tkinter as tk
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

# Alpha Vantage API key (replace with your own key)
ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY'

# Create a function to fetch stock data and update the chart
def fetch_and_update_chart():
    symbol = symbol_entry.get().strip()
    if not symbol:
        return

    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')

    if 'Error Message' in data:
        chart_label.config(text="Invalid symbol or API error.")
    else:
        chart_label.config(text=f"Fetching data for {symbol}...")
        plt.figure(figsize=(8, 4))
        plt.title(f"Stock Price for {symbol}")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.plot(data.index, data['4. close'], label='Close Price', color='blue')
        plt.legend(loc='upper left')
        chart_label.config(text="")

        # Embed the chart in the tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

# Create the main application window
app = tk.Tk()
app.title("Stock Price Monitor")

frame = tk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True)

# Create and pack widgets
symbol_label = tk.Label(frame, text="Enter Stock Symbol:")
symbol_label.pack(pady=5)

symbol_entry = tk.Entry(frame)
symbol_entry.pack(pady=5)

fetch_button = tk.Button(frame, text="Fetch Data", command=fetch_and_update_chart)
fetch_button.pack(pady=5)

chart_label = tk.Label(frame, text="")
chart_label.pack()

# Run the tkinter main loop in a separate thread
def run_gui():
    app.mainloop()

gui_thread = threading.Thread(target=run_gui)
gui_thread.start()
