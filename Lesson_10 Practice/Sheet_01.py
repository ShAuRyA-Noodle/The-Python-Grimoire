"""
train_booking.py
----------------

This script demonstrates a simple Train class with the following features:
- Booking tickets
- Checking train status
- Calculating ticket fare (simulated)
"""

from random import randint


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Train:
    """
    A simple Train class to simulate ticket booking and status checking.
    """

    def __init__(self, train_no: int):
        """
        Constructor to initialize a Train instance.

        Args:
            train_no: Train number (unique identifier)
        """
        self.train_no = train_no

    def book_ticket(self, from_station: str, to_station: str) -> None:
        """
        Simulate booking a ticket from one station to another.

        Args:
            from_station: Starting station
            to_station: Destination station
        """
        print(f"Ticket booked in train no: {self.train_no} from {from_station} to {to_station}")

    def get_status(self) -> None:
        """
        Display the current status of the train.
        """
        print(f"Train no: {self.train_no} is running on time.")

    def get_fare(self, from_station: str, to_station: str) -> None:
        """
        Display a randomly generated fare for a ticket.

        Args:
            from_station: Starting station
            to_station: Destination station
        """
        fare = randint(222, 5555)
        print(f"Ticket fare in train no: {self.train_no} from {from_station} to {to_station} is ₹{fare}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    t = Train(12399)
    t.book_ticket("Rampur", "Delhi")
    t.get_status()
    t.get_fare("Rampur", "Delhi")


if __name__ == "__main__":
    main()
