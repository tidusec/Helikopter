from typing import List, Union, Literal

Position = List[Union[int, float]]
Direction = Literal["noord", "oost", "zuid", "west"]

class Helicopter:
    def __init__(self, begin, direction):
        if not isinstance(begin, list) or len(begin) != 3 or not all(isinstance(x, (int, float)) for x in begin):
            raise ValueError("begin must be a list of 3 integers or floats")

        self.directions = ["noord", "oost", "zuid", "west"]
        if direction not in self.directions:
            raise ValueError("direction must be one of 'noord', 'oost', 'zuid', or 'west'")

        self.location = begin
        self.direction = self.directions.index(direction)

    def move_up(self):
        self.location[2] += 1

    def move_down(self):
        self.location[2] -= 1

    def turn_left(self):
        if self.direction == 0:
            self.direction = 4
        self.direction -= 1

    def turn_right(self):
        if self.direction >= 4:
            self.direction = self.direction % 4
        self.direction += 1

    def calculate_movement_vector(self):
        movement_vector = [0, 1]
        for i in range(self.direction):
            movement_vector = [movement_vector[1], -movement_vector[0]]

        return movement_vector

    def move_forward(self):
        movement_vector = self.calculate_movement_vector()
        self.location[0] += movement_vector[0]
        self.location[1] += movement_vector[1]

    def execute_instructions(self, instructions):
        for letter in instructions:
            match letter:
                case "U":
                    self.move_up()
                case "D":
                    self.move_down()
                case "R":
                    self.turn_right()
                case "L":
                    self.turn_left()
                case "V":
                    self.move_forward()

        return self.location, self.directions[self.direction]





heli1 = Helicopter([0, 0, 0], "noord")

print(heli1.execute_instructions("UURVVVLVVRRVD"))