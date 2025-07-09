import torch
from PIL import Image
import numpy as np

# Load model (adjust path to your weights)
# model = torch.hub.load('WongKinYiu/yolov9', 'custom', path='yolov9-c.pt', source='github')
model = torch.hub.load('/root/.cache/torch/hub/yolov9-main', 'custom', path='app/yolov9-c.pt', source='local')
model.eval()

# Define labels
CLASS_NAMES = list(model.names.values())


def get_cvat_info():
    return {
        "name": "Yolov9 API",
        "description": "Yolov9 detection model",
        "type": "detector",
        "spec": [{"id": idx, "name": label} for idx, label in enumerate(CLASS_NAMES)]
    }


def detect_objects(image: Image.Image):
    results = model(image, size=640)

    if not hasattr(results, "xyxy") or len(results.xyxy) == 0:
        return []  # or raise HTTPException(status_code=422, detail="No detection result")

    detections = results.xyxy[0]  # [x1, y1, x2, y2, conf, cls]
    output = []

    for det in detections:
        if len(det) < 6:
            continue  # skip invalid detection
        x1, y1, x2, y2, conf, cls_id = det.tolist()
        cls_id = int(cls_id)
        item = {
            "label": CLASS_NAMES[cls_id] if cls_id < len(CLASS_NAMES) else f"class_{cls_id}",
            "points": [int(x1), int(y1), int(x2), int(y2)],
            "type": "rectangle"
        }

        if CLASS_NAMES[cls_id] == "Plate":
            # You can integrate OCR here for plate_number
            item["attributes"] = [{"name": "plate_number", "value": "ABC-1234"}]
        output.append(item)
    return output

