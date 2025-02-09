## Dataset Documentation

### Overview
The dataset contains images of aluminum surfaces with labeled defects:
- **Cracks**
- **Pitting**
- **Dents**
- **Corrosion**

### Structure
- `data/raw/`: Raw images (640x640 or original resolution).
- `data/labels/defect_labels.csv`: YOLO/COCO-like CSV with bounding boxes.

### Quality Checks
- We run `scripts/data_validation.py` to ensure correct format and no missing columns.
- Periodic visual inspections and random sampling ensure annotation accuracy.

### Future Work
- Add new defect types (e.g., welding anomalies).
- Expand dataset for other metals or conditions (temperature variations, humidity, etc.).
