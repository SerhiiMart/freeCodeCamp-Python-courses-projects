import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(object, **balls):
        object.balls = dict(balls)
        object.contents = []
        for colour, number in object.balls.items():
            for i in range(number):
                object.contents.append(colour)

  def draw(object, number_of_balls_to_draw):
      rand_balls = []
      temp_contents = object.contents
      if number_of_balls_to_draw > len(object.contents):
          return object.contents
      for i in range(number_of_balls_to_draw):
        rand_ball = random.choice(temp_contents)
        rand_balls.append(rand_ball)
        temp_contents.remove(rand_ball)
      return rand_balls




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
