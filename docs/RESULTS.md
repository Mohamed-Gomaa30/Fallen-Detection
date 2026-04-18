# Results Documentation

## Performance Metrics on CUACAFAll Dataset

| Model | Inference Time (ms) | Accuracy | Precision | Recall | F1 Score | mAP50 |
|-------|---------------------|----------|-----------|--------|----------|-------|
| yolov8n | 2.5 | 0.977 | 0.994 | 0.989 | 0.991 | 0.995 |
| yolov9t | 3.14 | 0.960 | 0.994 | 0.992 | 0.993 | 0.994 |
| YoloV11n | 3.2 | 0.973 | 0.988 | 0.994 | 0.991 | 0.994 |
| YoloV12n | 2.2 | 0.960 | 0.981 | 0.992 | 0.986 | 0.994 |
| Faster R-CNN | 7.174 | 0.990 | 0.990 | 0.990 | 0.990 | 0.990 |
| ssd_mobilenet_v2 | 22.78 | 0.990 | 0.990 | 0.990 | 0.990 | 0.983 |

### Key Findings - CUACAFAll Dataset
- **Fastest Inference**: YoloV12n (2.2ms)
- **Highest Accuracy**: yolov8n (0.977)
- **Best Precision**: yolov8n & yolov9t (0.994)
- **Best Recall**: YoloV11n (0.994)
- **Best F1 Score**: yolov9t (0.993)
- **Best mAP50**: yolov8n (0.995)

## Performance Metrics on URFD Dataset

| Model | Inference Time (ms) | Accuracy | Precision | Recall | F1 Score | mAP50 |
|-------|---------------------|----------|-----------|--------|----------|-------|
| yolov8n | 2.4 | 0.913 | 0.969 | 0.980 | 0.975 | 0.991 |
| YoloV9t | 3.2 | 0.934 | 0.972 | 0.973 | 0.972 | 0.989 |
| YoloV11n | 3.7 | 0.934 | 0.978 | 0.969 | 0.974 | 0.991 |
| YoloV12n | 3.7 | 0.930 | 0.964 | 0.977 | 0.970 | 0.988 |
| Faster R-CNN | 15.767 | 1.0 | 1.0 | 1.0 | 1.0 | 0.974 |
| ssd_mobilenet_v2 | 27.54 | 1.0 | 1.0 | 1.0 | 1.0 | 0.962 |

### Key Findings - URFD Dataset
- **Fastest Inference**: yolov8n (2.4ms)
- **Perfect Accuracy**: Faster R-CNN & ssd_mobilenet_v2 (1.0)
- **Perfect Precision**: Faster R-CNN & ssd_mobilenet_v2 (1.0)
- **Perfect Recall**: Faster R-CNN & ssd_mobilenet_v2 (1.0)
- **Perfect F1 Score**: Faster R-CNN & ssd_mobilenet_v2 (1.0)
- **Best mAP50**: yolov8n & YoloV11n (0.991)

## Data Augmentation Applied to URFD Dataset
1. Zoom augmentation: 50%
2. Grayscale conversion

## Comparative Analysis

### Speed vs Accuracy Trade-off
- **YOLO models**: Best balance of speed and accuracy (2-4ms inference)
- **Faster R-CNN**: Higher accuracy but slower (7-16ms)
- **SSD MobileNet**: Slowest inference (22-28ms) but perfect accuracy on URFD

### Dataset Performance
- **CUACAFAll**: YOLO models perform exceptionally well with mAP50 > 0.99
- **URFD**: Traditional models (Faster R-CNN, SSD) achieve perfect metrics

### Recommendations
- **Real-time applications**: Use YoloV12n for fastest inference
- **Highest accuracy**: Use yolov8n for CUACAFAll, Faster R-CNN for URFD
- **Balanced performance**: YoloV9t offers good speed-accuracy balance

## Model Selection Guide

### For CUACAFAll Dataset
1. **yolov8n** - Best overall performance (highest mAP50: 0.995)
2. **YoloV12n** - Fastest inference (2.2ms)
3. **yolov9t** - Best F1 score (0.993)

### For URFD Dataset
1. **Faster R-CNN** - Perfect accuracy (1.0 across all metrics)
2. **yolov8n** - Fastest with high mAP50 (0.991)
3. **YoloV9t** - Good balance of speed and accuracy

## Notes
- D-FINE-N and RF-DETR-Nano models were tested but results not available
- All metrics are based on standard evaluation protocols
- Inference times measured per image
