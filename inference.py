from fer import FER
import cv2

from camera import *

class Inference():

    def __init__(self):
        pass


    def infer(self):
        img = cv2.imread("./test_im_blank.jpg")
        detector = FER()
        result = detector.detect_emotions(img)
        return result

if __name__ == "__main__":
    infer = Inference().infer()
    print(infer)
    