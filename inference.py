from fer import FER
import cv2

from camera import *

class Inference():

    def __init__(self):
        pass


    def infer(self):
        camera = Camera()
        img = camera.get_image()
        cv2.imwrite("test.jpeg", img)
        detector = FER()
        result = detector.detect_emotions(img)
        
        if not result:
            return False, None
        else:
            # only looking at the first face found, check largest face in ideal world
            happy = result[0]['emotions']['happy']
            sad = result[0]['emotions']['sad']
            overall_happiness = (1.0+(happy-sad))/2.0
            return True, overall_happiness

if __name__ == "__main__":
    infer = Inference().infer()
    print(infer)
    