import datetime
from implementation import Event  # Import the Event class

def test_event():
    event = Event("Basketball League", "2025-06-15")
    assert event.display_event() == "Event: Basketball League on 2025-06-15"
    print("Test Passed")

test_event()
