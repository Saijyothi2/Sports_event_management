class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def display_event(self):
        return f"Event: {self.name} on {self.date}"

match = Event("Football Tournament", "2025-05-10")
print(match.display_event())