# Importing the class Fan
from Fan import Fan

# Importing Tkinter to show the Fan properties
import tkinter as tk

# Creating the class TestFan
class TestFan (Fan):
    # Defining the objects for TestFan
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("FAN")

        # Creating two Fan objects
        fan1 = Fan(speed=Fan.FAST, radius=10, color='yellow', on=True)
        fan2 = Fan(speed=Fan.MEDIUM, radius=5, color='blue', on=False)