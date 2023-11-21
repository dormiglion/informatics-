import turtle
from random import randint

t = turtle.Turtle()
sc = turtle.getscreen()
w, h = sc.window_width(), sc.window_height()
print(w, h)
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

for i in range(50):
    x = randint(-w/2, w/2)

    if -160 < x < 160:
        y = randint(150, h/2)
    else:
        y = randint(0, h/2)

    t.penup()
    t.goto(x,y)
    t.color("#fff5c1")
    t.begin_fill()
    t.circle(3)
    t.end_fill()

turtle.done()