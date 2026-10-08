#!/usr/bin/python3
import turtle

def circle(direction="left"):
    N=150
    for i in range (N):
	    turtle.forward(1)
	    if direction == "left":
		    turtle.left(360/N)
	    elif direction == "right":
		    turtle.right(360/N)
	    else:
		    print("Error")
		    return
def eight():
    circle("left")
    circle("right")
turtle.speed(0)
turtle.shape("turtle")
for i in range(6):
    eight()
    turtle.left(30)
turtle.mainloop()



	 

