import cv2
import numpy as np
import math
from time import sleep
from classes.detector import Detector

#global values, calculated manually
defaultHeight = 1300
height = defaultHeight
laserOriginPoint = (792, 1005)

# Laser setup
from gpiozero import OutputDevice
laser = OutputDevice(17)

# Detector setup
detector = Detector() 

# Laser head setup
from classes.laser_head import LaserHead
head = LaserHead()

def moveServos(laserPoint, targetPoint):
    movePanServo(laserPoint, targetPoint)
    moveTiltServo(laserPoint, targetPoint)

def movePanServo(laserPoint, targetPoint):
    angleRadians = math.atan2(targetPoint[0] - laserPoint[0], laserPoint[1] - targetPoint[1])

    shiftedAngleRadians = angleRadians + math.pi / 2
    
    # Bringing shifted angle to the [-pi, pi] range
    shiftedAngleRadians = math.atan2(math.sin(shiftedAngleRadians), math.cos(shiftedAngleRadians))


    angleDegrees = math.degrees(shiftedAngleRadians)

    if angleDegrees < 0:
        angleDegrees += 180

    if angleDegrees >= 0 and angleDegrees <= 180:
        head.setPanAngle(angleDegrees)

def moveTiltServo(laserPoint, targetPoint, invert=False):
    global height

    distance = math.sqrt((laserPoint[0] - targetPoint[0])**2 + (laserPoint[1] - targetPoint[1])**2)
    
    angleRadians = math.atan2(distance, height)

    shiftedAngleRadians = angleRadians + math.pi / 2
    
    # Bringing shifted angle to the [-pi, pi] range
    shiftedAngleRadians = math.atan2(math.sin(shiftedAngleRadians), math.cos(shiftedAngleRadians))

    angleDegrees = math.degrees(shiftedAngleRadians)

    if invert:
        angleDegrees = 180 - angleDegrees

    head.setTiltAngle(angleDegrees)


# Camera setup

from picamera2 import Picamera2, Preview
from libcamera import controls
camera = Picamera2()

def capture():
    img = camera.capture_array()
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

index = 1
def captureAndSave():
	global index

	save_path = 'test_' + str(index) + '.png'
	camera.capture_file(save_path)
	print('saved as: ' ,save_path)

	index = index + 1


def findArucoMarker(img):
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # New aruco API, for opencv version >4.8.0
    arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
    arucoDetectionParams = cv2.aruco.DetectorParameters()
    arucoDetector = cv2.aruco.ArucoDetector(arucoDict, arucoDetectionParams)
    corners, ids, rejected_img_points = arucoDetector.detectMarkers(imgGrayscale)

    # Old API
    # arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_250)
    # arucoDetectionParams = cv2.aruco.DetectorParameters_create()
    # corners, ids, rejected_img_points = cv2.aruco.detectMarkers(imgGrayscale, arucoDict, parameters=arucoDetectionParams)

    if np.all(ids is not None): # If there are markers found by detector
        for i in range(0, len(ids)):
            cv2.aruco.drawDetectedMarkers(img, corners)

        targetPoint = (int(corners[0][0][0][0]), int(corners[0][0][0][1]))

        return targetPoint
    
    else:
        print('Aruco marker not found.')
        return None
    

def findLaserPoint(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_range = np.array([160, 70, 242])
    upper_range = np.array([170, 255, 255])

    mask = cv2.inRange(img_hsv, lower_range, upper_range)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        print('Laser point not found.')
        return None

    laserPointCandidates = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        aspect_ratio = w / float(h)
        area = w * h

        minAspectRatio = 0.8
        maxAspectRatio = 1.5
        maxArea = 2000

        if minAspectRatio <= aspect_ratio <= maxAspectRatio and area <= maxArea:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                laserPointCandidates.append({
                    "coordinates": (cx, cy),
                    "area": area
                })

    if len(laserPointCandidates) == 0: 
        print('Laser point not detected.')
        return None

    candidateWithMaxArea = max(laserPointCandidates, key=lambda x: x['area'])

    return candidateWithMaxArea['coordinates']

def distanceBetweenPointsExceedsThreshold(targetPoint, laserPoint):
    threshold_for_error = 50
    distance = math.sqrt((laserPoint[0] - targetPoint[0])**2 + (laserPoint[1] - targetPoint[1])**2)

    return distance > threshold_for_error

def adjustHeight(laserPoint, targetPoint):
    global height
    global defaultHeight
    global laserOriginPoint

    maxHeight = 10000
    minHeight = 100

    print('previous height: ', height)

    distance_laser_target = math.sqrt((laserPoint[0] - targetPoint[0])**2 + (laserPoint[1] - targetPoint[1])**2)
    distance_origin_laser = math.sqrt((laserOriginPoint[0] - laserPoint[0])**2 + (laserOriginPoint[1] - laserPoint[1])**2)
    distance_origin_target = math.sqrt((laserOriginPoint[0] - targetPoint[0])**2 + (laserOriginPoint[1] - targetPoint[1])**2)

    theta = abs(90 - head.tilt.getAngle()) # calculate angle between laser origin height and laser beam
    theta_radians = math.radians(theta)

    delta_H = distance_laser_target / math.tan(theta_radians)

    if (distance_origin_laser >= distance_origin_target):
        height = height + delta_H
        print('Increased H by ', delta_H)
    else:
        height = height - delta_H
        print('Reduced H by ', delta_H)

    if not minHeight < height < maxHeight:
        height = defaultHeight
        print('Reset to default height.')

    print('new height: ', height)
    
    


def main():
    global height
    global laserOriginPoint

    head.pan.mid()
    head.tilt.mid()

    preview_config = camera.create_preview_configuration(
		main={"size": (1920, 1920)}
	)
    camera.configure(preview_config)
    camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
    camera.start()

    while True:
        img = capture()

        targetPoint = detector.detect(img)

        if targetPoint:

            movePanServo(laserOriginPoint, targetPoint)

            invertTiltAngle = targetPoint[1] <= laserOriginPoint[1]
            moveTiltServo(laserOriginPoint, targetPoint, invertTiltAngle)
            
            laser.on()

            # This sleep should be the amount of time it takes for the servos to move to the position
            sleep(0.75)

            img = capture()

            laserPoint = findLaserPoint(img)
            if laserPoint:
                cv2.circle(img, laserPoint, radius=10, thickness=2, color=(255, 0, 0))

            if targetPoint:
                cv2.circle(img, targetPoint, radius=10, thickness=2, color=(0, 255, 0))

            if laserPoint and distanceBetweenPointsExceedsThreshold(targetPoint, laserPoint):
                print('Sufficient error detected.')
                adjustHeight(laserPoint, targetPoint)

                moveTiltServo(laserOriginPoint, targetPoint, invertTiltAngle)
        else:
            laser.off()

        

        preview_img = cv2.resize(img, (800, 800))
        cv2.imshow('Preview', preview_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            head.pan.mid()
            head.tilt.mid()
            laser.off()

            break


if __name__ == '__main__':
    main()