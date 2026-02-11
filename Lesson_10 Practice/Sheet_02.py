"""
train_booking.py
----------------

This script demonstrates a simple Train class with:
- Ticket booking
- Checking train status
- Displaying ticket fare (simulated)
"""

from random import randint


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Train:
    """
    A Train class that allows booking tickets, checking status,
    and getting fares.
    """

    def __init__(self, train_no: int):
        """
        Initialize a Train instance.

        Args:
            train_no: Unique train number
        """
        self.train_no = train_no

    def book_ticket(self, from_station: str, to_station: str) -> None:
        """Book a ticket from from_station to to_station."""
        print(f"Ticket is booked in train no: {self.train_no} from {from_station} to {to_station}")

    def get_status(self) -> None:
        """Display the current train status."""
        print(f"Train no: {self.train_no} is running on time")

    def get_fare(self, from_station: str, to_station: str) -> None:
        """Display the fare for a ticket (simulated randomly)."""
        fare = randint(222, 5555)
        print(f"Ticket fare in train no: {self.train_no} from {from_station} to {to_station} is ₹{fare}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    # Create a Train instance
    t = Train(12399)

    # Book ticket, check status, and get fare
    t.book_ticket("Rampur", "Delhi")
    t.get_status()
    t.get_fare("Rampur", "Delhi")


if __name__ == "__main__":
    main()
