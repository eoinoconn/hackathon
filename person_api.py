
class PersonAPI(object):
    SAD = 0
    HAPPY = 1
    THRESHOLD = 0.5;
    STATE= HAPPY
    Presence = None
    Emotions = None
    def __init__(self, present_=None, emotions_=None):
        print("Hello from PERSON api")
        self.Presence = present_
        self.Emotions = emotions_

    def calculate_emotions(self):
        if self.Emotions <= self.THRESHOLD:
            self.STATE = self.SAD
            print("Not happy: Setting STATE to SAD")
        elif self.Emotions > self.THRESHOLD:
            self.STATE = self.HAPPY
            print("Not sad: Setting STATE to HAPPY")

    def detection(self):
        if self.Presence > 0:
            print("Face detected! Calculating Emotions")
            self.calculate_emotions()
        else:
            print("No Detection... Are you there ?")

        return self.STATE



def main():
    print("Instantiate person object")
    person = PersonAPI(0,0)
    print(person.detection())

if __name__ == '__main__':
    main()