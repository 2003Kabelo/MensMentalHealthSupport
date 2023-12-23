from tkinter import *
import turtle
import random
root = Tk()

def buttonClick():
     wn = turtle.Screen()
     wn.setup(width=800,height=600)
     wn = turtle.title("MENS MENTAL HEALTH")

     colors = ['red','blue','orange','yellow','magenta','purple','peru','ivory','dark orange']
     turtle.bgcolor("Black")

     star = turtle.Turtle()
     star.speed(0)
     star.hideturtle()

     moon = turtle.Turtle()
     moon.hideturtle()

     text = turtle.Turtle()
     text.speed(6)
     text.hideturtle()

     def draw_moon(color,pos):
         x , y = pos
         moon.color(color)
         moon.begin_fill()
         moon.penup()
         moon.goto(x, y)
         moon.pendown()
         moon.circle(50)
         moon.end_fill()
     draw_moon('white',(-300,170))
     draw_moon('black',(-278,183))
     def draw_star(pos, color,length):
         x,y = pos
         star.color(color)
         star.penup()
         star.goto(x,y)
         star.pendown()
         star.begin_fill()
         for i in range(5):
             star.forward(length)
             star.right(145)
             star.forward(length)
         star.end_fill()


     def write_text(color):
         text.color(color)
         text.penup()
         text.goto(-180,-270)
         text.pendown()
         style = ('Stencil Std Bold',25,'normal')
         text.write("Be Well Kings And Good Night",font=style,move=True)

     def random_pos():
         return (random.randint(-390,390),random.randint(-200,290))
     def random_length():
         return random.randint(5,25)

     while True:
         color = random.choice(colors)
         pos = random_pos()
         length = random_length()
         draw_star(pos,color,length)
         write_text(color)

     turtle.done()


label = Label(root,text="MEN'S MENTAL HEALTH",font=("Arial",35,"bold"))
label.place(x=10,y=10)
frame = Frame(root,bg="#306570",width=600,height=150)
frame.place(x=0,y=80)
label2 = Label(root,text="RAISE THE AWARENESS",font=("Arial",15,"italic"),fg="#267650")
label2.place(x=30,y=90)
label3 = Label(root,text="MENS LIVES MATTER",font=("Arial",15,"italic"),fg="#267650")
label3.place(x=30,y=120)
button = Button(root,text="CLICK HERE",fg="#267650",command=buttonClick)
button.place(x=30,y=250)

root.geometry('600x600')
root.mainloop()

