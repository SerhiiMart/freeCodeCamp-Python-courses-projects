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
  time_index = 0
  for experiment in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    expected_balls_copy = copy.deepcopy(expected_balls)
    result = hat_copy.draw(num_balls_drawn)
    for ball in result:
      if ball in expected_balls_copy:
        expected_balls_copy[ball] -= 1
    if all(value <= 0 for value in expected_balls_copy.values()):
      time_index += 1
  prob_calculator = time_index/num_experiments
  return(prob_calculator)
