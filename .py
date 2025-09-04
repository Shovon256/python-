import turtle

# Create turtle object
pen = turtle.Turtle()


# Function to draw a square
def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)


# Function to draw a rectangle
def draw_rectangle():
    for _ in range(2):
        pen.forward(150)
        pen.right(90)
        pen.forward(80)
        pen.right(90)


# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        pen.forward(100)
        pen.left(120)


# Draw shapes
draw_square()
pen.penup()
pen.goto(200, 0)
pen.pendown()
draw_rectangle()
pen.penup()
pen.goto(-200, 0)
pen.pendown()
draw_triangle()

# Keep window open
turtle.done()
