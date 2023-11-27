import turtle
from random import randint
from turtle import Screen

t = turtle.Turtle()
screen = Screen()
w, h = 960, 900
print(w, h)
screen.setup(w, h)
t.speed(100)

# ПОЛЕ
t.color("#175c19")

t.begin_fill()
t.left(180)
t.forward(w/2)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w/2)
t.end_fill()

# НЕБО
t.color("#182e63")

t.begin_fill()
t.forward(w/2)
t.right(90)
t.forward(h/2)
t.right(90)
t.forward(w)
t.right(90)
t.forward(h/2)
t.right(90)
t.forward(w/2)
t.end_fill()


# ДОМ КОРОБКА
t.color("#7e6337")

t.left(90)
t.forward(h/12)
t.right(90)
t.begin_fill()
t.forward(w/6)
t.right(90)
t.forward(h/6)
t.right(90)
t.forward(w/3)
t.right(90)
t.forward(h/6)
t.right(90)
t.forward(w/6)
t.end_fill()



# КРЫША

# СДВИГ ПО КРЫШЕ
t.right(90)
t.forward(h/6)
t.left(90)
t.forward(w/6)

t.color("#451717")

t.begin_fill()
t.goto(0,150)
t.goto(160,75)
t.goto(-160,75)
t.end_fill()

# ДВЕРЬ

# СДВИГ ПО ДВЕРИ
t.penup()
t.goto(-20,-75)

t.color("#462700")
t.begin_fill()
t.goto(-20, 25)
t.goto(20, 25)
t.goto(20, -75)
t.goto(-20,-75)
t.end_fill()

# ОКНА

t.penup()
t.goto(-60,-30)

t.color("#567a79")
t.begin_fill()
t.goto(-60, 30)
t.goto(-120, 30)
t.goto(-120, -30)
t.goto(-60,-30)
t.end_fill()

t.penup()
t.goto(60,-30)

t.color("#567a79")
t.begin_fill()
t.goto(60, 30)
t.goto(120, 30)
t.goto(120, -30)
t.goto(60,-30)
t.end_fill()

ang = (75/160)

for i in range(10**4):
    x = randint(-w/2, w/2)

    if -160 < x < 160:
        y = randint(75 + int(((160-abs(x))*ang)), h/2)

    else:
        y = randint(3, h/2)

    t.penup()
    t.goto(x,y)
    t.color("#fff5c1")
    t.begin_fill()
    t.circle(2)
    t.end_fill()

turtle.done()