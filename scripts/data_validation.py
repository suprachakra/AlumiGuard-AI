import pandas as pd

def validate_dataset(path='data/labels/defect_labels.csv'):
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("Dataset is empty.")
    required_cols = ['image_id','defect_type','x_min','y_min','x_max','y_max']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
    print("Dataset validation passed!")

if __name__ == "__main__":
    validate_dataset()
