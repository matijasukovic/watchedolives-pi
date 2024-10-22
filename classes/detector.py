from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from PIL import Image
import cv2
import os
from datetime import datetime

class Detector:
     # Note: In  order to use a NCNN model with SAHI, you need to comment out line 33 from sahi > models > yolov8.py

    def __init__(self):
        self.detection_model = AutoDetectionModel.from_pretrained(
            model_type='yolov8',
            model_path=r"/home/matijasukovic_pi5/projects/watchedolives_pi/models/tuned/n_tuned/weights/best_ncnn_model",
            confidence_threshold=0.4,
            device="cpu"
        )

        self.setsDir = '/home/matijasukovic_pi5/sets'

        self.setIndex = self.getSetIndex(os.path.join(self.setsDir, 'set_index.txt'))
        self.innerIndex = 0

        os.makedirs(os.path.join(self.setsDir, self.getCurrentSetName(), 'images'), exist_ok=True)
        os.makedirs(os.path.join(self.setsDir, self.getCurrentSetName(), 'labels'), exist_ok=True)

    def detect(self, image):
        # 'image' is a numpy array because that's what we use elsewhere, and for SAHI we need to convert it to a PIL image
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)

        result_sliced = get_sliced_prediction(
            image_pil,
            self.detection_model,
            slice_height=640,
            slice_width=640,
            overlap_height_ratio=0,
            overlap_width_ratio=0,
            verbose=1
        )

        predictions = result_sliced.object_prediction_list

        filename = self.getNextFilename()
        image_path = os.path.join(self.setsDir, self.getCurrentSetName(), 'images', filename + '.png'),
        label_path = os.path.join(self.setsDir, self.getCurrentSetName(), 'labels', filename + '.txt'),

        image_path = image_path[0]
        label_path = label_path[0]

        cv2.imwrite(image_path, image)
        self.save_predictions_to_yolo(predictions=predictions, save_path=label_path, img_width=image.shape[1], img_height=image.shape[0])

        if len(predictions) == 0:
            print('Detected no objects.')
            return None

        print('Detected {0} objects.'.format(len(predictions)))

        max_confidence = 0
        best_bbox = None

        for obj in result_sliced.object_prediction_list:
            if obj.score.value > max_confidence:
                max_confidence = obj.score.value
                best_bbox = obj.bbox

        if not best_bbox:
            print('Error in Detector.detect')
            return None

        min_x = best_bbox.minx
        min_y = best_bbox.miny
        max_x = best_bbox.maxx
        max_y = best_bbox.maxy

        center_x = int((min_x + max_x) / 2)
        center_y = int((min_y + max_y) / 2)

        return (center_x, center_y)


    def getCurrentSetName(self):
        year = datetime.now().strftime('%Y')
        return f'{year}_set{self.setIndex}'
    
    def getNextFilename(self):
        self.innerIndex += 1
        return f'{self.getCurrentSetName()}_{self.innerIndex}'


    def getSetIndex(self, index_file_path):
        if os.path.exists(index_file_path):
            with open(index_file_path, 'r') as f:
                index = int(f.read().strip())
        else:
            index = 1

        with open(index_file_path, 'w') as f:
            f.write(str(index + 1))
        
        return index

    def convert_sahi_to_yolo_format(self, bbox, img_width, img_height):
        # YOLO expects center_x, center_y, width, height, all normalized
        x_min, y_min, box_width, box_height = bbox
        x_center = (x_min + box_width / 2) / img_width
        y_center = (y_min + box_height / 2) / img_height
        norm_width = box_width / img_width
        norm_height = box_height / img_height
        return x_center, y_center, norm_width, norm_height

    def save_predictions_to_yolo(self, predictions, save_path, img_width, img_height):
        with open(save_path, 'w') as f:
            for prediction in predictions:
                yolo_bbox = self.convert_sahi_to_yolo_format(prediction.bbox.to_xywh(), img_width, img_height)
                yolo_line = f"{prediction.category.id} " + " ".join(map(str, yolo_bbox)) + "\n"
                f.write(yolo_line)