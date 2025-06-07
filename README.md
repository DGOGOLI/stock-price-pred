# 📈 Stock Price Prediction with RNN (LSTM)

This is a simple project that uses a Recurrent Neural Network (RNN) with LSTM layers to predict stock prices based on historical data.

## 🧠 What It Does

- Loads stock price data from a CSV file
- Creates time series sequences for supervised learning
- Builds and trains an LSTM-based model
- Splits the dataset **temporally** into training and test sets (no random state)
- Visualizes the model predictions vs actual prices

## 📁 Project Structure

- `notebooks/stock-price-pred.ipynb`: main notebook with data preprocessing, model training, and result visualization
- `data/ticker_stock_data.csv`: historical stock data
- `data/get_raw_data.py`: basic script to download raw data

## 🛠️ Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
ll