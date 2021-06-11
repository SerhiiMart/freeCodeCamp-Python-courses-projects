class Rectangle:
    def __init__(object, width, height):
      object.width = width
      object.height = height

    def __str__(object):
      return f'Rectangle(width={object.width}, height={object.height})'

    def set_width(object, width):
      object.width = width

    def set_height(object, height):
      object.height = height

    def get_area(object):
      return object.width * object.height
      
    def get_picture(object):
      if(object.width > 50 or object.height > 50):
        return "Too big for picture."
      string = (("*" * object.width) + "\n") * object.height
      return string

    def get_perimeter(object):
      return 2 * object.width + 2 * object.height

    def get_diagonal(object):
      return ((object.width ** 2 + object.height ** 2) ** .5)

    def get_amount_inside(object, shape):
      return int(object.get_area() / shape.get_area())



class Square:
