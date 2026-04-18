# Setup Guide

## Prerequisites
- Python 3.8 or higher
- CUDA-capable GPU (optional, for faster inference)
- Roboflow API key

## Installation Steps

### 1. Clone the Repository
```bash
git clone <repository-url>
cd FallenDetection
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```
ROBOFLOW_API_KEY=your_api_key_here
```

### 5. Download Model Weights
Place model weights in the `models/` directory:
- `Yolov8n_CUACA.pt`
- `Yolov9n_CUACA.pt`
- `Yolov12_CUACA.pt`
- `faster_rcnn_URFD.pth`
- `ssdmobilenet-CUACAFAll.pth`

Note: Model weights are not included in the repository due to size. Contact the project maintainers for access.

### 6. Verify Installation
```bash
python inference.py --help
```

## GPU Setup (Optional)

### NVIDIA GPU
1. Install CUDA Toolkit
2. Install cuDNN
3. Install PyTorch with CUDA support:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Verify GPU
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

## Troubleshooting

### Import Errors
- Ensure all dependencies are installed
- Check Python version compatibility

### CUDA Errors
- Verify CUDA installation
- Check GPU driver compatibility
- Install correct PyTorch version

### Model Loading Errors
- Verify model weights are in correct directory
- Check model file integrity
- Ensure model architecture matches weights
