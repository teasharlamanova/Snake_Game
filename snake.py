from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.body = list()
        self.draw_snake()
        self.head = self.body[0]

    def draw_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def move_parts(self):
        for part_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part_num - 1].xcor()
            new_y = self.body[part_num - 1].ycor()
            self.body[part_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_part(self, position):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.body.append(part)

    def extend(self):
        self.add_part(self.body[-1].position())
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)