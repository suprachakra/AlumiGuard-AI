import pandas as pd
from sklearn.model_selection import train_test_split
from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab

def detect_data_drift():
    df = pd.read_csv('data/labels/defect_labels.csv')
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    
    dashboard = Dashboard(tabs=[DataDriftTab()])
    dashboard.calculate(train, test)
    dashboard.save('data_drift_report.html')

if __name__ == "__main__":
    detect_data_drift()
