student@debian ~ @ script.sh
xonsh: For full traceback set: $XONSH_SHOW_TRACEBACK = True
xonsh: subprocess mode: command not found: 'script.sh'
script.sh: command not found
student@debian ~ [1] @ vim script.sh
student@debian ~ @ chmod +x script.sh
student@debian ~ @ ./script.sh
Traceback (most recent call last):
  File "/home/student/script.sh", line 6, in <module>
    turtle.bacward(5)
    ^^^^^^^^^^^^^^
AttributeError: module 'turtle' has no attribute 'bacward'. Did you mean: 'backward'?
student@debian ~ [1] @ vim script.sh
student@debian ~ @ ./script.sh
student@debian ~ @





scipt.sh = #!/usr/bin/python3
import turtle
turtle.speed(0)
for i in range(30):
	turtle.penup()
	turtle.backward(5)
	turtle.right(90)
	turtle.forward(5)
	turtle.left(90)
	turtle.pendown

for a in range(4):
	turtle.forward(i + 10)
	turtle.left(90)

turtle.mainloop()



















 
