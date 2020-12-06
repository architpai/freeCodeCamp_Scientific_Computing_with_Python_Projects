import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color,number in kwargs.items():
            for i in range(0,number):
                self.contents.append(color)
    def draw(self,number_of_balls):
        drawnballs = []
        if number_of_balls > len(self.contents):
            drawnballs = self.contents
        else:
            for i in range(0, number_of_balls):
                random_int = random.randint(0, len(self.contents)-1)
                drawnballs.append(self.contents.pop(random_int))
        return drawnballs


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0
    expected_check_val = len(expected_balls.keys())
    for i in range(0,N):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        check = 0
        for color,number in expected_balls.items():
            if drawn_balls.count(color) >= number:
                check = check+1
        if check == expected_check_val:
            M = M + 1
    return M/N



hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
