from turtle import Screen, Turtle

screen = Screen() 
screen.setup(width=600, height=600) #setting dimensions
screen.bgcolor("black") #setting color
screen.title("snakegame")#setting title

segment_1 = Turtle("square")
segment_1.color("red")

segment_2 = Turtle("square")
segment_2.color("red")
segment_2.goto(-20,0)

segment_3 = Turtle("square")
segment_3.color("red")
segment_3.goto(-40,0)



#holding screen apperance
screen.exitonclick()