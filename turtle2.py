import turtle
w = turtle.Turtle()
w.shape('turtle')
w.color("green")
#w.pensize(10)
w.penup()

step = 20
for i in range(40):
    w.forward(step)
    w.left(24)
    w.stamp()
    step = step + 3

turtle.done()
    
    

    
    

   

       
    
    
    
    
    
    
    
    

    
    