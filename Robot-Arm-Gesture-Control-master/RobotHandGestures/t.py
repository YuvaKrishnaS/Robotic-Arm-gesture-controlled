
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=1)
mySerial = SerialObject("COM10", 9600, 1)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        mySerial.sendData(fingers)

    cv2.imshow("Image",img)
    cv2.waitKey(1)