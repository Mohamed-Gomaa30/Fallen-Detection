
import os
import modal 
from pathlib import Path 

current_dir = Path(__file__).parent
config_vid = current_dir / "videos"
config_models = current_dir / "models"

app = modal.App("Fallen-Detection")

volume = modal.Volume.from_name("fallen-data", create_if_missing=True)
print(f"Volume out {volume}")

# Image
image = (modal.Image.debian_slim()
.apt_install("libgl1-mesa-glx", "libglib2.0-0")
.pip_install(
    "roboflow", 
    "ultralytics"
)
.add_local_dir(config_vid, remote_path="/root/videos/")
.add_local_dir(config_models, remote_path="/root/models/"))


# ---------------------------
# Yolo Inference 
# ---------------------------
@app.function(
    # gpu="t4", 
    image=image,
    volumes={"/data/": volume},
    timeout=3600
)
def yolo_inference():
    """Yolo Inference"""

    from ultralytics import YOLO

    model = YOLO('/root/models/Yolo8n_URFD.pt')
    results = model(source="/root/videos/fall.png", project="/root/output",show=False, save=True)
