import turtle as t

t.bgcolor('white')
t.pensize(2)


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


t.speed(2)
t.color('red', 'pink')
t.begin_fill()
t.left(140)
t.forward(111.65)
curve()

t.left(120)
curve()

t.forward(111.65)
t.end_fill()
t.hideturtle()
