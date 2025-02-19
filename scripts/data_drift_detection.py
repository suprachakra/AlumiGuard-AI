#!/usr/bin/env python3
"""
drift_detection_cli.py
----------------------
CLI tool to run data drift detection between historical and live data.
"""

import argparse
import numpy as np
from src.utils.drift_detection import detect_drift

def main():
    parser = argparse.ArgumentParser(description="Run data drift detection.")
    parser.add_argument("--train", required=True, help="Path to training data numpy file")
    parser.add_argument("--live", required=True, help="Path to live data numpy file")
    args = parser.parse_args()

    train_data = np.load(args.train)
    live_data = np.load(args.live)
    drift = detect_drift(train_data, live_data)
    print("Data Drift Detected:" if drift else "No Significant Drift Detected.")

if __name__ == "__main__":
    main()
