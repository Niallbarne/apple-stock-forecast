# forecast/views.py

from django.shortcuts import render
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend for matplotlib
matplotlib.use('Agg')

# Load the trained model once at startup
model_fit = joblib.load(r'C:\Users\Sonali\OneDrive\Desktop\project\mysite\forecast\models\arima_model.pkl')

def load_data():
    """Load the historical data from the CSV file."""
    filepath = r'C:\Users\Sonali\OneDrive\Desktop\project\data\AAPL.csv'  # Path to the CSV file
    df = pd.read_csv(filepath)
    return df

def index(request):
    """Handles the main forecasting view."""
    forecast = None
    error_message = None
    forecast_list = []  # Initialize an empty list for the forecasted values
    if request.method == 'POST':
        # Get forecast horizon from user input, defaulting to 30 days
        forecast_horizon = int(request.POST.get('forecast_horizon', 30))
        df = load_data()  # Load the CSV file

        # Preprocess the data
        df['Date'] = pd.to_datetime(df['Date'])  # Ensure 'Date' is a datetime object
        df.set_index('Date', inplace=True)  # Set the date as the index
        
        try:
            # Forecast using ARIMA model with integer indices to avoid index matching issues
            start_index = len(df)
            end_index = start_index + forecast_horizon - 1
            
            # Make predictions using integer indices
            forecast_obj = model_fit.get_prediction(start=start_index, end=end_index)
            
            # Extract forecasted values and confidence intervals
            forecast = forecast_obj.predicted_mean
            forecast_list = forecast.tolist()  # Convert forecasted values to a list
            forecast_index = pd.date_range(df.index[-1] + pd.Timedelta(days=1), periods=forecast_horizon)
            confidence_intervals = forecast_obj.conf_int()

            # Plot historical data and forecast
            plt.figure(figsize=(10, 6))
            plt.plot(df.index, df['Close'], label='Historical Prices', color='blue')
            plt.plot(forecast_index, forecast, label='Forecasted Prices', color='orange')

            # Extract lower and upper bounds from confidence intervals
            lower_bound = confidence_intervals.iloc[:, 0].values
            upper_bound = confidence_intervals.iloc[:, 1].values

            # Add confidence intervals to the plot
            plt.fill_between(forecast_index, lower_bound, upper_bound, color='lightgray', alpha=0.5, label='Confidence Interval')

            plt.title('Apple Stock Price Forecast with Confidence Intervals')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.grid()

            # Save the figure
            image_path = r'C:\Users\Sonali\OneDrive\Desktop\project\mysite\forecast\static\forecast\forecast_plot.png'
            plt.savefig(image_path)
            plt.close()

        except Exception as e:
            error_message = str(e)  # Capture any errors during forecasting

    # Pass the forecast list and error message to the template
    return render(request, 'forecast/index.html', {'forecast': forecast_list, 'error': error_message})
