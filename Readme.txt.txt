# Apple Stock Forecast

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Forecasting Model](#forecasting-model)
- [Installation](#installation)
- [Usage](#usage)
- [Challenges Faced](#challenges-faced)
- [License](#license)

## Introduction

The Apple Stock Forecast application predicts future stock prices for Apple Inc. based on historical data. The application is built using Django as the web framework and utilizes machine learning techniques to generate forecasts.

## Dataset

The dataset used for this project is the historical stock price data for Apple Inc. (AAPL), sourced from [Yahoo Finance](https://finance.yahoo.com/). The dataset includes daily stock prices, including Open, High, Low, Close prices, and Volume for a specified period. This data serves as the foundation for training our forecasting model.

## Forecasting Model

The forecasting model employed in this application is a combination of time series analysis and machine learning techniques. We utilized **[insert model name, e.g., ARIMA, LSTM, etc.]** to make predictions based on past stock prices. The model was trained on the dataset, and its performance was evaluated using metrics such as Mean Absolute Error (MAE) and Root Mean Square Error (RMSE).

## Installation

To set up and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Niallbarne/apple-stock-forecast.git
   cd apple-stock-forecast
