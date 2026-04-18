# Dataset Documentation

## Datasets Used

### CUACA Dataset
- **Full Name**: Custom University Activity and Action Dataset
- **Purpose**: Fall detection dataset
- **Classes**: Fall, Normal activities
- **Format**: COCO format annotations
- **Training Models**: YOLOv8, YOLOv9, YOLOv12, SSD MobileNet, Faster R-CNN

### URFD Dataset
- **Full Name**: UR Fall Detection Dataset
- **Purpose**: Fall detection dataset
- **Classes**: Fall, Normal activities
- **Format**: Custom format
- **Training Models**: YOLOv8, YOLOv12, Faster R-CNN

## Dataset Statistics

### CUACA
- Total Images: [To be updated]
- Training Split: [To be updated]
- Validation Split: [To be updated]
- Test Split: [To be updated]

### URFD
- Total Images: [To be updated]
- Training Split: [To be updated]
- Validation Split: [To be updated]
- Test Split: [To be updated]

## Data Preparation

### Annotation Format
Datasets are annotated in COCO format with the following structure:
```json
{
  "images": [...],
  "annotations": [...],
  "categories": [...]
}
```

### Class Labels
- `0`: Fall
- `1`: Normal/No Fall

## Training Data Organization
```
assets/
└── Object_Detection/
    ├── CUACA/
    │   └── FineTune_YoloV8_(CUACA_Dataset)_with_COCO_weights/
    │       ├── train/
    │       ├── val/
    │       └── predict/
    └── URFD/
        └── FineTune_YoloV8_(URFD_Dataset)_with_COCO_weights/
            ├── train/
            ├── val/
            └── predict/
```

## Data Augmentation
Training notebooks include data augmentation techniques:
- Random flips
- Rotation
- Color jittering
- Scaling
- Mosaic augmentation (YOLO models)

## Roboflow Integration
The project uses Roboflow for dataset management:
- API key stored in `.env` file
- Dataset versioning
- Automatic preprocessing
- Data augmentation pipeline
