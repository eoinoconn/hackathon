

import time

class PersonAPI(object):
    """Person object to communicate with inference module
    Abstract usage of data sent from inference module
    """
    timer_started=None
    timer_ended=None
    timer_current=None;
    last_detection_time = 0
    sitting_time = 0
    emotions = None
    present = None
    keep_going = True
    current_state = None
    #time in seconds after which notification will be sent
    time_limit_for_sitting = 180

    def __init__(self, present_=None, emotions_=None):
        //main loop?
        while self.keep_going:
            keep_going = False

    def notificiation_builder(self, emotion_=None, presence_=None):
        """
        build notification
        :return: varies based on parameters
        """
        notification = [emotion_, presence_]
        return notification

    def get_current_timer(self):
        """
        Returns time since timer start or reset
        :return: time
        """        
        self.timer_current = time.time() - self.timer_started;
        return self.timer_current
    
    def reset_timer(self):
        self.timer_started=time.time()

    def set_emotions(self,emo_):
        self.emotions = emo_

    def set_present(self,present_):
        self.present = present_

    def get_current_state(self):
        return self.current_state



