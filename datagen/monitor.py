from classes.camera import Camera
import cv2

camera = Camera()

def main():
    while True:
        img = camera.capture()
        cv2.namedWindow('Preview', cv2.WINDOW_NORMAL)
        cv2.imshow('Preview', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()