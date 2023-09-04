import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

# Sample data (replace with your stock data)
dates = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
stock_values = [100, 110, 90, 120, 105]

# Create a GUI window
root = tk.Tk()
root.title("Stock Value Chart")

# Create a figure for the chart
fig, ax = plt.subplots(figsize=(8, 4))

# Highlight low values in red and high values in green
colors = ['red' if val < min(stock_values) + (max(stock_values) - min(stock_values)) / 3 else
          'green' if val > max(stock_values) - (max(stock_values) - min(stock_values)) / 3 else
          'blue' for val in stock_values]

# Plot the stock values
ax.plot(dates, stock_values, marker='o', linestyle='-', color='blue', markersize=8, label='Stock Value')

# Customize the chart
ax.set_xlabel('Date')
ax.set_ylabel('Stock Value')
ax.set_title('Stock Value Over Time')
ax.legend()

# Create a canvas to display the chart in the GUI
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Start the GUI event loop
root.mainloop()
