from turtle import *
bgcolor("orange")
color("red")
title("corazon")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()
penup()
goto(0, -50)
pendown()
color("white")
write("Te Amo", font=("Arial", 24, "bold"))
hideturtle()
done()
import time
time.sleep(10) 
