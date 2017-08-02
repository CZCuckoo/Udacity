import turtle
import math
    

def draw_triangle(length, iteration):
    window = turtle.Screen()
    window.bgcolor("white")
    
    
    chris = turtle.Turtle()
    chris.speed("fast")
    chris.color("green")
    chris.shape("turtle")
    
    y = 0

    while(iteration > 0):
        while(y < 3):
            chris.forward(length)
            chris.left(120)
            y = y + 1
        

        length = length/2
        iteration = iteration - 1
        





    
        #while(y < 3):
        #    chris.forward(length)
        #    chris.left(120)
        #    y = y + 1
            
        #iteration = iteration - 1


 
        

    
        
        
draw_triangle(200,3)
