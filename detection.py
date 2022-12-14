import torch
import cv2
from pathlib import Path
from socket import gaierror
from urllib.error import URLError

#Credit to itsjohnward

# Model
def load_model_network():
    try:
        return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).eval()
    except (gaierror, URLError):
        return None

def load_model_cache():
    try:
        path = Path.home() / '.cache/torch/hub/ultralytics_yolov5_master'
        return torch.hub.load(str(path), 'yolov5s', source='local', pretrained=True).eval()
    except:
        print("You must run `tello download` while connected to network first!")
        return None

def detect_objects(image):
    file1= open("detections.txt", "a")
    model = load_model_cache()
    if model is None:
        file1.write('Detection model not found!')
        return image, []
    detections = model([image]).pandas().xyxy[0]
    file1.writelines(detections)
    for label, confidence, left, right, bottom, top in detections[['name', 'confidence', 'xmin', 'xmax', 'ymin', 'ymax']].values:
        cv2.rectangle(image, (round(left), round(top)), (round(right), round(bottom)), (255, 0, 0), 2)
        cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)),
                            (round(left), round(top) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 0, 255), 1)
    #return image, detections
    image.save("detection.jpg")
    file1.writelines(detections)
