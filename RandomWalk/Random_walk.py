from random import choice

class RandomWalk:

    def __init__(self, num_points = 5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0] # location of start
    
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1, 1])
            y_direction = choice([-1, 1])
            x_length = choice([0,1,2,3,4])
            y_length = choice([0,1,2,3,4])

            if x_length == 0 and y_length == 0:
                continue

            temp_x = self.x_values[-1] + x_length * x_direction
            temp_y = self.y_values[-1] + y_length * y_direction

            self.x_values.append(temp_x)
            self.y_values.append(temp_y)