# Creating the class Fan
class Fan:
    # Creating the constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Defining all of the objects anf functions of the Fan
    def __init__(self, speed=1, radius=5, color='blue', on=False):
        self._speed = speed
        self._on = on
        self._radius = radius
        self._color = color

    # Getters and setters
    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def is_on(self):
        return self._on

    def set_on(self, on):
        self._on = on

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
