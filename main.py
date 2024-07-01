import matplotlib.pyplot as plt
import yfinance as yf

sp500 = yf.Ticker("^GSPC")

sp500 = sp500.history(period="max")

del sp500["Dividends"]
del sp500["Stock Splits"]


sp500[""]


# Create a line plot
plt.plot(sp500.index, sp500["Close"])

# Display the plot in the terminal
plt.show()
