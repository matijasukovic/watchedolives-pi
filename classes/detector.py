from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from PIL import Image
import cv2
import os

class Detector:
     # Note: In  order to use a NCNN model with SAHI, you need to comment out line 33 from sahi > models > yolov8.py

    def __init__(self):
        self.detection_model = AutoDetectionModel.from_pretrained(
            model_type='yolov8',
            model_path=r"/home/matijasukovic_pi5/projects/watchedolives_pi/models/tuned/n_tuned/weights/best_ncnn_model",
            confidence_threshold=0.4,
            device="cpu"
        )

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

        if len(result_sliced.object_prediction_list) == 0:
            print('Detected no objects.')
            return None

        print('Detected {0} objects.'.format(len(result_sliced.object_prediction_list)))

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

        result_sliced.export_visuals(export_dir=r"/home/matijasukovic_pi5/projects/watchedolives_pi", file_name='testing')

        return (center_x, center_y)
