# Abstract State class
class State:
    def open(self):
        pass

    def close(self):
        pass

    def raise_window(self):
        pass

    def lower_window(self):
        pass

# Concrete State: Open Doors
class OpenState(State):
    def open(self):
        print("The doors are already open")

    def close(self):
        print("Closing the doors")
        return ClosedState()

    def raise_window(self):
        print("Raising the windows")

    def lower_window(self):
        print("Lowering the windows")

# Concrete State: Closed Doors
class ClosedState(State):
    def open(self):
        print("Opening the doors")
        return OpenState()

    def close(self):
        print("The doors are already closed")

    def raise_window(self):
        print("Raising the windows")

    def lower_window(self):
        print("Lowering the windows")

# Door class that uses the State pattern
class Door:
    def __init__(self):
        self.state = ClosedState()

    def open(self):
        self.state = self.state.open()

    def close(self):
        self.state = self.state.close()

    def raise_window(self):
        self.state.raise_window()

    def lower_window(self):
        self.state.lower_window()

# Usage
door = Door()
door.open()          # Opening the doors
door.raise_window()  # Raising the windows
door.close()         # Closing the doors
door.lower_window()  # Lowering the windows
