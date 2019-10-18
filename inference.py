import time

from fer import FER
import cv2

from camera import *
from person import *
from spotify import *

class Inference():

    def __init__(self):
        pass


    def infer(self):
        camera = Camera()
        img = camera.get_image_2()
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

    def infer_video(self):
        self.cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        detector = FER()
        i = 0
        person = PersonAPI(0,0)
        avg_happines = 1
        while True:
            i += 1
            ret, frame = self.cam.read()
            if not ret:
                break
    
            result = detector.detect_emotions(frame)
            if len(result) > 0:
                print(result)
                happy = result[0]['emotions']['happy']
                sad = result[0]['emotions']['sad']
                x, y, w, h =  result[0]["box"]

                overall_happiness = (1.0+(happy-sad))/2.0
                cv2.rectangle(frame, (x,y),(x+w,y+h),(200,0,0),2)
            else:
                overall_happiness = 0.5
            
            cv2.putText(frame, str(overall_happiness), (0, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
            avg_happines = avg_happines*0.9 + overall_happiness*0.1
            print("average happines {}".format(avg_happines))
            if i == 20:
                i = 0
                if avg_happines > 0.6:
                    if person.STATE:
                        continue
                    else:
                        play_happy()
                    person.STATE = 1
                elif avg_happines < 0.5:
                    if person.STATE:
                        play_sad()
                    else:
                        continue
                    person.STATE=0
                    

            cv2.imshow("frame", frame)
            cv2.waitKey(40)
            #time.sleep(10)

if __name__ == "__main__":
    infer = Inference().infer_video()
    print(infer)
    