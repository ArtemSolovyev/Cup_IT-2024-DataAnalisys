from ultralytics import YOLO

model = YOLO("yolov8x.pt")

results = model.train(data="custom.yaml", epochs=1)