"""
pm_model.py
-----------
Module for building and training the predictive maintenance model.
Integrates ICS sensor data and defect logs to forecast maintenance needs.
"""

import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt
from src.utils.logger import get_logger

logger = get_logger(__name__)

def preprocess_data(ics_data: pd.DataFrame, defect_logs: pd.DataFrame) -> pd.DataFrame:
    """
    Merge and preprocess ICS sensor data with defect logs.
    Returns a time-series DataFrame suitable for Prophet modeling.
    """
    logger.info("Preprocessing ICS data and defect logs for PM model.")
    # Example: Merge on timestamp (ensure both dataframes have a 'timestamp' column)
    merged = pd.merge_asof(ics_data.sort_values('timestamp'),
                           defect_logs.sort_values('timestamp'),
                           on='timestamp', direction='nearest')
    merged['defect_flag'] = merged['defect_type'].notnull().astype(int)
    # Aggregate to hourly data
    merged['timestamp'] = pd.to_datetime(merged['timestamp'])
    agg_data = merged.resample('H', on='timestamp').sum().reset_index()
    return agg_data

def run_training(data: pd.DataFrame):
    """
    Trains a Prophet model on the aggregated data.
    Returns the trained model and performance metrics.
    """
    logger.info("Training predictive maintenance model using Prophet.")
    # Prophet requires columns 'ds' and 'y'
    df = data.rename(columns={'timestamp': 'ds', 'defect_flag': 'y'})
    model = Prophet(interval_width=0.95)
    model.fit(df)
    # Dummy metric for demonstration
    metrics = {"mae": 0.05, "rmse": 0.08}
    logger.info("Predictive maintenance model training complete.")
    return model, metrics

def plot_forecast(model, data: pd.DataFrame):
    """
    Generate and plot forecast from the trained model.
    """
    df = data.rename(columns={'timestamp': 'ds', 'defect_flag': 'y'})
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    fig = model.plot(forecast)
    plt.title("Predictive Maintenance Forecast")
    plt.xlabel("Time")
    plt.ylabel("Defect Probability")
    plt.show()
    return fig

if __name__ == "__main__":
    # Example run (assumes existence of appropriate CSV files in data/raw)
    try:
        ics_data = pd.read_csv("data/raw/ics_sensor_data.csv")
        defect_logs = pd.read_csv("data/raw/defect_logs.csv")
        processed_data = preprocess_data(ics_data, defect_logs)
        model, metrics = run_training(processed_data)
        plot_forecast(model, processed_data)
    except Exception as e:
        logger.error(f"Error during PM model training: {e}")
