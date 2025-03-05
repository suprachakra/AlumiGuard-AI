"""
Advanced logic for correlating ICS threat logs with YOLO-based defect detections.
Assumes we have two data sources:
1) ICS security logs (from Nozomi/Vectra) containing timestamps, severity, anomaly type
2) Defect logs from YOLO detection pipeline

Realistic assumptions:
- ICS logs come in JSON or CSV
- YOLO logs stored in a separate DB or CSV
- We do a time-window correlation: if ICS event occurs within +/- X minutes of a defect spike, raise a "Potential ICS sabotage" flag
"""

import pandas as pd
import numpy as np
import datetime

def load_ics_logs(ics_log_path: str) -> pd.DataFrame:
    """
    Loads ICS logs from Nozomi/Vectra, e.g., CSV with columns:
    ['timestamp', 'anomaly_type', 'severity', 'description']
    """
    df = pd.read_csv(ics_log_path, parse_dates=['timestamp'])
    return df

def load_defect_logs(defect_log_path: str) -> pd.DataFrame:
    """
    Loads YOLO-based defect logs, e.g., CSV with columns:
    ['timestamp', 'defect_count', 'plant_id', 'avg_confidence']
    """
    df = pd.read_csv(defect_log_path, parse_dates=['timestamp'])
    return df

def correlate_ics_defects(ics_df: pd.DataFrame, defect_df: pd.DataFrame, time_window: int = 5) -> pd.DataFrame:
    """
    Correlates ICS anomalies with defect spikes within a given time window (minutes).
    - If an ICS event severity >= 'medium' occurs, check for spike in defect_count in +/- time_window minutes.
    - Return a DataFrame with potential correlations.
    """
    # Simple approach: for each ICS log, find defect logs within time_window
    correlated_events = []
    for _, ics_row in ics_df.iterrows():
        ics_time = ics_row['timestamp']
        ics_severity = ics_row['severity']
        if ics_severity.lower() in ['medium', 'high', 'critical']:
            # Filter defect logs in +/- time_window
            start_time = ics_time - pd.Timedelta(minutes=time_window)
            end_time = ics_time + pd.Timedelta(minutes=time_window)
            window_df = defect_df[(defect_df['timestamp'] >= start_time) & 
                                  (defect_df['timestamp'] <= end_time)]
            # Check if there's a significant spike in defect_count
            avg_defect = window_df['defect_count'].mean() if not window_df.empty else 0
            if avg_defect > 5:  # arbitrary threshold
                correlated_events.append({
                    'ics_timestamp': ics_time,
                    'ics_severity': ics_severity,
                    'anomaly_type': ics_row['anomaly_type'],
                    'defect_spike_avg': avg_defect,
                    'time_window': f"{start_time} to {end_time}"
                })
    return pd.DataFrame(correlated_events)

def main():
    ics_path = 'data/ics_logs.csv'
    defect_path = 'data/defect_yolo_logs.csv'
    ics_df = load_ics_logs(ics_path)
    defect_df = load_defect_logs(defect_path)
    correlated_df = correlate_ics_defects(ics_df, defect_df, time_window=5)
    if not correlated_df.empty:
        print("Potential ICS sabotage or correlation found:")
        print(correlated_df)
    else:
        print("No ICS-Defect correlation found in the given timeframe.")

if __name__ == "__main__":
    main()
