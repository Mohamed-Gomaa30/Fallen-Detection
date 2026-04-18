# Model Documentation

## Available Models

### YOLOv8n
- **Files**: `Yolo8n_URFD.pt`, `Yolov8n_CUACA.pt`
- **Architecture**: YOLOv8 nano version
- **Training Datasets**: URFD, CUACA
- **Performance**: Best overall mAP50 on CUACA (0.995), excellent speed (2.5ms)
- **Use Case**: Real-time detection with highest accuracy

### YOLOv9n
- **Files**: `Yolov9n_CUACA.pt`
- **Architecture**: YOLOv9 nano version
- **Training Dataset**: CUACA
- **Performance**: Best F1 score on CUACA (0.993), good speed (3.14ms)
- **Use Case**: Balanced performance with high precision

### YOLOv12
- **Files**: `Yolov12_CUACA.pt`
- **Architecture**: YOLOv12
- **Training Dataset**: CUACA
- **Performance**: Fastest inference (2.2ms), good accuracy (0.960)
- **Use Case**: Speed-critical applications with good accuracy

### Faster R-CNN
- **Files**: `faster_rcnn_URFD.pth`, `fastercnn_CUACAFAll.pth`
- **Architecture**: Faster R-CNN
- **Training Datasets**: URFD, CUACA
- **Performance**: Perfect accuracy on URFD (1.0), slower inference (7-16ms)
- **Use Case**: High accuracy needs where speed is not critical

### YOLOv11n
- **Files**: (Not currently in models directory)
- **Architecture**: YOLOv11 nano version
- **Training Datasets**: CUACA, URFD
- **Performance**: Best recall on CUACA (0.994), good speed (3.2-3.7ms)
- **Use Case**: Applications requiring high recall rates

### SSD MobileNet
- **Files**: `ssdmobilenet-CUACAFAll.pth`
- **Architecture**: SSD with MobileNet backbone
- **Training Dataset**: CUACA
- **Performance**: Perfect accuracy on URFD (1.0), slowest inference (23-28ms)
- **Use Case**: Edge deployment where accuracy is prioritized over speed

## Model Comparison

| Model | Speed | Accuracy | Size | Best For | mAP50 (CUACA) | mAP50 (URFD) |
|-------|-------|----------|------|-----------|---------------|--------------|
| YOLOv8n | Fast (2.5ms) | Good (0.977) | Small | Real-time detection | 0.995 | 0.991 |
| YOLOv9t | Fast (3.14ms) | Good (0.960) | Small | Balanced performance | 0.994 | 0.989 |
| YOLOv11n | Medium (3.2ms) | Good (0.973) | Small | High accuracy needs | 0.994 | 0.991 |
| YOLOv12n | Fastest (2.2ms) | Good (0.960) | Small | Speed-critical apps | 0.994 | 0.988 |
| Faster R-CNN | Slow (7-16ms) | Excellent (0.99-1.0) | Large | Offline analysis | 0.990 | 0.974 |
| SSD MobileNet | Very Slow (23-28ms) | Excellent (0.99-1.0) | Very Small | Edge deployment | 0.983 | 0.962 |

## Usage
Models are loaded in the inference script based on user selection. Ensure model weights are present in the `models/` directory before running inference.
