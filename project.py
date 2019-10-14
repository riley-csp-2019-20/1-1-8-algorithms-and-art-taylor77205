import turtle as trtl
heart = trtl.Turtle()

#create heart 
heart.goto(0,0)
heart.shape("triangle")
heart.color("red")
heart.pendown()
heart.pensize(40)
heart.pencolor('red')
heart.begin_fill()
heart.left(60)
heart.forward(120)
heart.circle(40,190,60)
heart.right(140)
heart.circle(40,190,60)
heart.left(10)
heart.forward(130)
heart.end_fill()
#create T
import turtle            
wn= turtle.Screen()
T = turtle.Turtle()

for aColor in ["black"]:
   T.color(aColor)
   T.pensize(5)
   T.penup()
   T.goto(-8,60)
   T.pendown()
   T.left(90)
   T.forward(50)
   T.right(90)
   T.forward(25)
   T.right(90)
   T.right(90)
   T.forward(50)
   T.penup()

#make diamonds
import turtle 
wn= turtle.Screen()
D = turtle.Turtle()
D.penup()
D.goto(180,200)
D.left(40)
D.pendown()
count = 0
D.begin_fill()
while (count < 4):
   D.forward(100)
   D.left(90)
   count = count + 1
D.color("blue")
D.end_fill()

D.penup()
D.goto(-200,150)
D.left(0)
D.pendown()
count = 0
D.begin_fill()
while (count < 4):
   D.forward(50)
   D.left(90)
   count = count + 1
D.color("purple")
D.end_fill()

D.penup()
D.goto(-100,-150)
D.left(0)
D.pendown()
count = 0
D.begin_fill()
while (count < 4):
   D.forward(80)
   D.left(90)
   count = count + 1
D.color("yellow")
D.end_fill()


D.penup()
D.goto(150,-150)
D.left(0)
D.pendown()
count = 0
D.begin_fill()
while (count < 4):
   D.forward(40)
   D.left(90)
   count = count + 1
D.color("green")
D.end_fill()


letter = int(input("Enter a letter T> "))
if (letter >= T):
  print("!")

wn=trtl.Screen()
wn.mainloop()