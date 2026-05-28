import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']

data = yf.download(stocks, start='2020-01-01')['Close']

returns = data.pct_change().dropna()

mean_returns = returns.mean()
cov_matrix = returns.cov()

weights = np.array([0.25, 0.25, 0.25, 0.25])

portfolio_return = np.sum(mean_returns * weights) * 252
portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))

print("Expected Annual Return:", portfolio_return)
print("Portfolio Risk:", portfolio_risk)

(data / data.iloc[0] * 100).plot(figsize=(10,5))
plt.title("Portfolio Performance")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.show()
