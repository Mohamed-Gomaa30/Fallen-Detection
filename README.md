# Fallen Detection System

A computer vision-based fall detection system using deep learning models for real-time person fall detection in video streams. This project is part of a graduation project focused on enhancing elderly care and safety monitoring.

## Features

- **Multiple Model Support**: YOLOv8, YOLOv9, YOLOv11, YOLOv12, Faster R-CNN, and SSD MobileNet
- **Real-time Detection**: Fast inference with YOLO models (2-4ms per image)
- **High Accuracy**: Up to 99.5% mAP50 on CUACA dataset
- **Multi-dataset Training**: Trained on CUACA and URFD datasets
- **Flexible Input**: Support for video files, webcam streams, and image sequences
- **Comprehensive Documentation**: Detailed docs for setup, usage, and results

## Performance Summary

### CUACA Dataset Results
| Model | Inference Time | Accuracy | mAP50 |
|-------|---------------|----------|-------|
| YOLOv8n | 2.5ms | 97.7% | 99.5% |
| YOLOv9t | 3.14ms | 96.0% | 99.4% |
| YOLOv11n | 3.2ms | 97.3% | 99.4% |
| YOLOv12n | 2.2ms | 96.0% | 99.4% |
| Faster R-CNN | 7.17ms | 99.0% | 99.0% |
| SSD MobileNet | 22.78ms | 99.0% | 98.3% |

### URFD Dataset Results
| Model | Inference Time | Accuracy | mAP50 |
|-------|---------------|----------|-------|
| YOLOv8n | 2.4ms | 91.3% | 99.1% |
| YOLOv9t | 3.2ms | 93.4% | 98.9% |
| YOLOv11n | 3.7ms | 93.4% | 99.1% |
| YOLOv12n | 3.7ms | 93.0% | 98.8% |
| Faster R-CNN | 15.77ms | 100% | 97.4% |
| SSD MobileNet | 27.54ms | 100% | 96.2% |

## Installation

### Prerequisites
- Python 3.8 or higher
- CUDA-capable GPU (optional)
- Roboflow API key

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd FallenDetection
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file:
```
ROBOFLOW_API_KEY=your_api_key_here
```

5. **Download model weights**
Place trained models in the `models/` directory.

For detailed setup instructions, see [docs/SETUP.md](docs/SETUP.md)

## Usage

### Basic Inference
```bash
python inference.py --model yolov8 --source videos/vid1.mp4 --output results/
```

### Real-time Detection
```bash
python inference.py --model yolov9 --source 0 --output results/
```

### Available Models
- `yolov8` - YOLOv8n (recommended for real-time)
- `yolov9` - YOLOv9t (balanced performance)
- `yolov11` - YOLOv11n (high recall)
- `yolov12` - YOLOv12n (fastest inference)
- `faster_rcnn` - Faster R-CNN (highest accuracy)
- `ssd` - SSD MobileNet (edge deployment)

For more usage examples, see [docs/USAGE.md](docs/USAGE.md)

## Project Structure

```
FallenDetection/
├── docs/              # Comprehensive documentation
│   ├── PROJECT_OVERVIEW.md
│   ├── MODELS.md
│   ├── RESULTS.md
│   ├── USAGE.md
│   ├── SETUP.md
│   └── DATASETS.md
├── models/            # Trained model weights
├── notebooks/         # Training notebooks
│   ├── finetune-yolov8-cuaca-dataset-with-coco-weights.ipynb
│   ├── finetune-yolov8-urfd-dataset-with-coco-weights.ipynb
│   └── Faster_RCNN.ipynb
├── assets/            # Training outputs and results
├── videos/            # Sample videos for testing
├── inference.py       # Main inference script
├── .env               # Environment variables
└── .gitignore         # Git ignore rules
```

## Documentation

- [Project Overview](docs/PROJECT_OVERVIEW.md) - General project information
- [Model Documentation](docs/MODELS.md) - Detailed model information
- [Results & Performance](docs/RESULTS.md) - Comprehensive performance metrics
- [Usage Guide](docs/USAGE.md) - How to use the system
- [Setup Guide](docs/SETUP.md) - Installation instructions
- [Dataset Information](docs/DATASETS.md) - Training dataset details

## Datasets

### CUACA Dataset
Custom University Activity and Action dataset for fall detection with COCO format annotations.

### URFD Dataset
UR Fall Detection dataset with grayscale and zoom augmentation (50%).

## Model Selection Guide

### For Real-time Applications
- **YOLOv12n**: Fastest inference (2.2ms)
- **YOLOv8n**: Best overall performance (99.5% mAP50)

### For Highest Accuracy
- **YOLOv8n**: Best on CUACA dataset
- **Faster R-CNN**: Perfect accuracy on URFD (100%)

### For Edge Deployment
- **SSD MobileNet**: Lightweight model
- **YOLOv8n**: Good balance of size and performance

## Requirements

See `requirements.txt` for complete dependency list. Key dependencies include:
- PyTorch
- Ultralytics YOLO
- OpenCV
- NumPy
- Roboflow

## Contributing

This is a graduation project. For questions or suggestions, please contact the project maintainers.

## License

[Specify your license here]

## Acknowledgments

- CUACA Dataset contributors
- URFD Dataset creators
- Ultralytics team for YOLO implementation
- Roboflow for dataset management tools

## Contact

For more information about this project, please refer to the comprehensive documentation in the `docs/` folder.
