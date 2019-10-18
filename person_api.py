
import time

class PersonAPI(object):
    """Person object to communicate with inference module
    Abstract usage of data sent from inference module
    """
    timer_started =None
    timer_ended =None
    time_elapsed =None;
    last_detection_time = 0
    sitting_time = 0
    emotions = None
    present = None
    keep_going = True
    current_state = None
    # time in seconds after which notification will be sent
    time_limit_for_sitting = 180
    time_limit_for_away_reset = 60

    def __init__(self, present_=None, emotions_=None):
        if present_ is not None:
            self.present = present_
            self.restart_timer()

        if emotions_ is not None:
            self.emotions = emotions_

        self.performchecks()

    def performchecks(self):
        if self.get_time_elapsed() > self.time_limit_for_sitting:
            # remind user to move
            pass
        if self.present is not None:
            self.current_state = self.state_builder(self.emotions, self.present)
        else:
            if self.get_time_elapsed() > self.time_limit_for_away_reset:
                self.restart_timer()

    def state_builder(self, emotion_=None, presence_=None):
        """
        build state
        :return: varies based on parameters
        """
        state = [emotion_, presence_]
        return state

    def get_time_elapsed(self):
        """
        Returns time since timer start or reset
        :return: time
        """
        self.time_elapsed = time.time() - self.timer_started;
        return self.time_elapsed

    def restart_timer(self):
        self.timer_started =time.time()

    def set_emotions(self ,emo_):
        self.emotions = emo_

    def set_present(self ,present_):
        self.present = present_

    def get_current_state(self):
        return self.current_state
