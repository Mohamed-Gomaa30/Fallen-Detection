# Usage Guide

## Running Inference

### Basic Usage
```bash
python inference.py
```

### Command Line Arguments
The inference script supports various arguments for customization:

- `--model`: Select model type (yolov8, yolov9, yolov12, faster_rcnn, ssd)
- `--source`: Input source (video file path or camera index)
- `--output`: Output directory for results
- `--conf`: Confidence threshold (default: 0.5)
- `--iou`: IoU threshold for NMS (default: 0.45)

### Examples

#### Detect falls in a video file
```bash
python inference.py --model yolov8 --source videos/vid1.mp4 --output results/
```

#### Real-time detection from webcam
```bash
python inference.py --model yolov9 --source 0 --output results/
```

#### Custom confidence threshold
```bash
python inference.py --model yolov12 --source videos/vid1.mp4 --conf 0.7
```

## Output Format
The inference script generates:
- Annotated video with bounding boxes
- Detection logs with timestamps
- Statistics (total detections, confidence scores)

## Supported Input Formats
- Video files: MP4, AVI, MOV
- Camera streams: Webcam (index 0, 1, etc.)
- Image sequences: PNG, JPG

## Performance Tips
1. Use YOLOv8n for real-time applications
2. Adjust confidence threshold based on your use case
3. Use GPU acceleration if available
4. Lower resolution for faster inference
