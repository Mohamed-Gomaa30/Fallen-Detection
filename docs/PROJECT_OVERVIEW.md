# Fallen Detection Project Documentation

## Overview
This project is part of a graduation project focused on detecting fallen people using computer vision and deep learning techniques. The system uses various object detection models trained on different datasets to identify fallen individuals in video streams.

## Project Structure
```
FallenDetection/
├── docs/              # Documentation files
├── models/            # Trained model weights (gitignored)
├── notebooks/         # Jupyter notebooks for training
├── assets/            # Training outputs and results (gitignored)
├── videos/            # Sample videos for testing (gitignored)
├── inference.py       # Main inference script
├── .env               # Environment variables (gitignored)
└── .gitignore         # Git ignore rules
```

## Models Used
The project implements multiple object detection architectures:

### YOLO Models
- **YOLOv8n**: Trained on CUACA and URFD datasets
- **YOLOv9n**: Trained on CUACA dataset
- **YOLOv12**: Trained on CUACA and URFD datasets

### Traditional Object Detection Models
- **Faster R-CNN**: Trained on URFD dataset
- **SSD MobileNet**: Trained on CUACA dataset

## Datasets
- **CUACA**: Custom dataset for fall detection
- **URFD**: UR Fall Detection dataset

## Training Notebooks
- `finetune-yolov8-cuaca-dataset-with-coco-weights.ipynb`: YOLOv8 training on CUACA
- `finetune-yolov8-urfd-dataset-with-coco-weights.ipynb`: YOLOv8 training on URFD
- `Faster_RCNN.ipynb`: Faster R-CNN training

## Inference
The main inference script is `inference.py` which can be used to run fall detection on video files or camera streams.

## Environment Setup
1. Install required dependencies (see requirements)
2. Set up Roboflow API key in `.env` file
3. Download model weights to `models/` directory

## Results
Training results and outputs are stored in the `assets/` directory, organized by model and dataset.
