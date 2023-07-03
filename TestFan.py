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