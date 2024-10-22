from picamera2 import Picamera2, Preview
from libcamera import controls
import cv2

class Camera:
    def __init__(self):
        self.picamera = Picamera2()

        preview_config = self.picamera.create_preview_configuration(
            main={"size": (1920, 1920)}
        )
        
        self.picamera.configure(preview_config)
        self.picamera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
        self.picamera.start()

        self.savedImage_filename = 'test'
        self.savedImage_index = 0
        self.savedImage_extension = '.png'

    def capture(self):
        img = self.picamera.capture_array()
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    def captureAndSave(self):
        save_path = self.savedImage_filename + '_' + str(self.savedImage_index) + self.savedImage_extension
        self.picamera.capture_file(save_path)
        print('saved as: ' ,save_path)

        self.savedImage_index += 1