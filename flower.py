import turtle  

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
    
    abby = turtle.Turtle()
    abby.color("blue")
    abby.shape("turtle")
    abby.speed("fastest")
    for i in range (1,37):
        draw_square(abby)
        abby.right(10)
        
    for i in range (1,2):
        abby.color("green")
        abby.right(90)
        abby.forward(300)

    for i in range (1,19):
        draw_circle(abby)
        abby.right(10)
    window.exitonclick()

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_circle(some_turtle):
    some_turtle.circle(20)

    
draw_flower()
