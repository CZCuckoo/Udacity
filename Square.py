import turtle

def draw_objects():
    window = turtle.Screen()
    window.bgcolor("white")
    

    #drawing square
    abby = turtle.Turtle()
    abby.color("blue")
    abby.shape("turtle")
    abby.speed("fastest")
    for i in range (1,37):
        draw_square(abby)
        abby.right(10)

    #draw_circle()
    #draw_triangle()
    window.exitonclick()


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)



        
    
def draw_circle():
    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("red")
    bob.circle(100)

def draw_triangle():
    chris = turtle.Turtle()
    chris.color("green")
    chris.shape("turtle")
    y = 0
    while(y < 3):
        chris.forward(100)
        chris.left(120)
        y = y + 1
    
draw_objects()




