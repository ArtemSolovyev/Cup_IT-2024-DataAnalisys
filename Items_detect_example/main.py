from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("best.pt")
image = cv2.imread("img/test_image2.jpg")
CONFIDENCE = 0.5

results = model.predict(image, conf=CONFIDENCE)
print(results[0].boxes.data.tolist())


def result_image_out(results, image):
    thickness = 1
    font_scale = 1
    color = (0, 0, 255)
    class_id = "ariel_bottle"

    for data in results[0].boxes.data.tolist():
        xmin, ymin, xmax, ymax, confidence, class_id = data
        xmin=int(xmin)
        ymin=int(ymin)
        xmax=int(xmax)
        ymax=int(ymax)
        class_id=int(class_id)
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color=color, thickness=thickness)
        text=f"{class_id}: {confidence:.2f}"
        (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale, thickness=thickness)
        text_offset_x = xmin
        text_offset_y = ymin - 5
        box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height + baseline))
        overlay = image.copy()
        cv2.rectangle(overlay, box_coords[0], box_coords[1], color=color, thickness=cv2.FILLED)
        image = cv2.addWeighted(overlay, 0.6, image, 0.4, 0)
        cv2.putText(image, text, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale, color=(255,255,255), thickness=thickness)

    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.imwrite("result_image.jpg", image)
    return

def form_cord_list(results):
    array_of_shelves=[], array_of_items=[]
    for data in results[0].boxes.data:
        if data[-1]==1.1:
            array_of_shelves.append([int((data[0] + data[2])/2),int((data[1] + data[3])/2), data[2]-data[0]])
        elif data[-1]==0.0:
            array_of_items.append([int((data[0] + data[2])/2),int((data[1]+data[3])/2)])
    array_of_shelves.sort(reverse=True)
    return array_of_shelves, array_of_items

def form_pos_list(results, amount_of_boxes):
    array_of_shelves,array_of_items = form_cord_list(results)
    shelf_legth=(sum([i[2] for i in array_of_shelves])/len(array_of_shelves))
    box_length=shelf_legth/amount_of_boxes
    pos_array=[]
    for item in array_of_items:
        for shelf in array_of_shelves:
            if shelf[1]<item[1]:
                pos_array.append([int(item[0]//box_length)+1, array_of_shelves.index(shelf)])
                break
    return pos_array

def push_item(results):
    #get amount of boxes on a shelf
    amount_of_boxes=5
    pos_array=form_pos_list(results, amount_of_boxes)
    #push pos_array to DataBase
    return



result_image_out(results, image)
push_item(results)
