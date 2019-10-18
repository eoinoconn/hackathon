
"""Camera module for emote project
"""
import io
import time

from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2 # debug only
import numpy as np

class Camera():
    """Camera object for processing images captured by pi and pi camera
    """

    def __init__(self):
        self.camera = PiCamera()
        

    def get_image(self):
        """ Method to capture and return image

        return:
            numpy array: Image array
        """
        self.rawCapture = PiRGBArray(self.camera)
        time.sleep(0.1)
        self.camera.capture(self.rawCapture, format='bgr')
        image = self.rawCapture.array
        
        return np.array(image)

if __name__ == "__main__":
    camera = Camera()
    image = camera.get_image()
    cv2.imshow("Figure", image)
    cv2.waitKey(0)
