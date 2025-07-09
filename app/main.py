from fastapi import FastAPI, UploadFile, HTTPException, Request
from pydantic import BaseModel
import base64
import io
from PIL import Image
from app.yolov9_model import detect_objects
from app.yolov9_model import get_cvat_info
from app.utils import get_status

app = FastAPI()

class InvokeRequest(BaseModel):
    image: str  # base64 encoded image

@app.get("/status")
def cvat_info():
    return get_status()


@app.get("/cvat_info")
def cvat_info():
    return get_cvat_info()


@app.post("/invoke")
async def invoke(request: InvokeRequest):
    try:
        image_data = base64.b64decode(request.image)
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        result = detect_objects(image)
        print("result: {}".format(result))
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
