class PersonAPI(object):
    SAD = 0
    HAPPY = 1
    THRESHOLD = 0.5
    STATE = HAPPY
    Presence = None
    Emotions = None

    def __init__(self, present_=None, emotions_=None):
        self.Presence = present_
        self.Emotions = emotions_

    def calculate_emotions(self):
        if self.Emotions <= self.THRESHOLD:
            self.STATE = self.SAD

        elif self.Emotions > self.THRESHOLD:
            self.STATE = self.HAPPY

    def detection(self):
        if self.Presence > 0:
            self.calculate_emotions()
        return self.STATE


def main():
    print("Instantiate person object")
    person = PersonAPI(0, 0)
    print(person.detection())


if __name__ == '__main__':
    main()
