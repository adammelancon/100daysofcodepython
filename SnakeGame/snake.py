from turtle import Turtle, heading
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_COLOR = "green"
SNAKE_SHAPE = "square"
NORTH = 90.0
SOUTH = 270.0
EAST = 0.0
WEST = 180.0


class Snake():
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[-1]

    def create_snake(self):
        for i in STARTING_POS:
            t = Turtle(shape=SNAKE_SHAPE)
            t.color(SNAKE_COLOR)
            t.penup()
            t.goto(i)
            self.segment.append(t)
            # input("continue...")

    def move(self):
        for seg in range(len(self.segment) - 1 , 0 , -1):
            newx = self.segment[seg - 1].xcor()
            newy = self.segment[seg - 1].ycor()
            self.segment[seg].goto(newx, newy)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)
    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
    def left(self):
        if self.head.heading() != EAST:     
            self.head.setheading(WEST)
    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def wall_check(self):
        if self.head.xcor() >= 290 or self.head.xcor() <= -290:
            print("YOU HIT THE FAR WALL")
            return True
            
        if self.head.ycor() >= 290 or self.head.ycor() <= -290:
            print("YOU HIT THE SIDE WALL")
            return True
            

    def grow_snake(self):
        g = Turtle(shape=SNAKE_SHAPE)
        g.color(SNAKE_COLOR)
        g.penup()
        new_tail_x = self.segment[-1].xcor()
        new_tail_y = self.segment[-1].ycor()
        g_cords = (new_tail_x, new_tail_y)
        g.goto(g_cords)
        self.segment.append(g)

        # self.segment.append(new_tail_x, new_tail_y)
