 ####################################################
# 
# Create different spiral shapes using
# Python and Turtle!
#
####################################################


# import the turtle library and create the turtle
import turtle
pen = turtle.Turtle()


# draw a dot in the center of the screen
# set the pen's drawing speed
pen.dot()
pen.speed(0)

def write_N():
    pen.pendown()
    pen.left(90)
    pen.forward(85)
    pen.right(150)
    pen.forward(100)
    pen.left(150)
    pen.forward(85)
    
def write_I():
    pen.penup()
    pen.right(90)
    pen.forward(40)
    pen.pendown()
    pen.forward(40)
    pen.left(180)
    pen.penup()
    pen.forward(20)
    pen.left(90)
    pen.pendown()
    pen.forward(85)
    pen.right(90)
    pen.forward(20)
    pen.left(180)
    pen.penup()
    pen.forward(20)
    pen.pendown()
    pen.forward(20)

def write_C():    
    pen.penup()
    pen.forward(65)
    pen.pendown()
    pen.forward(25)
    pen.left(180)
    pen.penup()
    pen.forward(25)
    pen.right(45)
    pen.pendown()
    pen.forward(35.3553390593)
    pen.right(45)
    pen.forward(30)
    pen.right(45)
    pen.forward(35.3553390593)
    pen.right(45)
    pen.forward(25)

def write_A():
    pen.penup()
    pen.right(90)
    pen.forward(85)
    pen.left(90)
    pen.forward(40)
    pen.left(60)
    pen.pendown()
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.right(180)
    pen.forward(50)
    pen.left(60)
    pen.forward(50)
    pen.penup()
    pen.left(60)
    pen.forward(50)
    pen.left(120)
    pen.forward(140)


pen.penup()
pen.right(180)
pen.forward(300)
pen.right(180)
write_N()
write_I()
write_C()
write_A()
write_N()

turtle.done()