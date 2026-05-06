class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, data):
        for obs in self.observers:
            obs.update(data)

class EmailService:
    def update(self, data):
        print("Email sent:", data)

class SmsService:
    def update(self, data):
        print("SMS sent:", data)

subject = Subject()
subject.subscribe(EmailService())
subject.subscribe(SmsService())

subject.notify("User registered")
