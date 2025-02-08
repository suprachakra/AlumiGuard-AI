import pandas as pd

def validate_dataset(path):
    df = pd.read_csv(path)
    assert not df.empty, "Dataset is empty"
    assert 'defect_type' in df.columns, "Missing defect_type column"
    assert df['defect_type'].nunique() >= 3, "Insufficient defect types"
    print("Dataset validation passed!")

if __name__ == "__main__":
    validate_dataset("data/labels/defect_labels.csv")
