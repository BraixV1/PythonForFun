from turtle import *




def function(length):
    
    
    if length < 5:
        exitonclick()
    else:
        for i in range(4):
            fd(100)
            right(90)
            i += 1
            left(45)
            function(length*0.65)
            right(135)
        
        
