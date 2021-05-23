import cv2
from fer import FER

image = cv2.imread("happy.jpeg")
detector = FER()

print(detector.detect_emotions(image))

emotion, score = detector.top_emotion(image)
print(emotion, score)
