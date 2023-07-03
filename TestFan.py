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
        fan1 = Fan(speed=Fan.FAST, radius=10, color='Yellow', on=True)
        fan2 = Fan(speed=Fan.MEDIUM, radius=5, color='Blue', on=False)

        # Create labels to display fan properties
        self.label1 = tk.Label(self.window, text="FAN 1")
        self.label1.pack()
        self.display_fan_properties(fan1)

        self.label2 = tk.Label(self.window, text="FAN 2")
        self.label2.pack()
        self.display_fan_properties(fan2)

        self.window.mainloop()

    def display_fan_properties(self, fan):
        speed_label = tk.Label(self.window, text=f"Speed: {fan.get_speed()}")
        speed_label.pack()

        radius_label = tk.Label(self.window, text=f"Radius: {fan.get_radius()}")
        radius_label.pack()

        color_label = tk.Label(self.window, text=f"Color: {fan.get_color()}")
        color_label.pack()

        on_label = tk.Label(self.window, text=f"Is On: {fan.is_on()}")
        on_label.pack()

        separator = tk.Label(self.window, text="\n")
        separator.pack()

# Create an instance to run the test program
if __name__ == "__main__":
    test = TestFan()