import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor ('dodgerblue')

# feet
t.goto(-90, -150)
rectangle(50, 20, 'grey')
t.goto(-25, -150)
rectangle(50, 20, 'grey')

# legs
t.goto(-25, -50)
rectangle(15, 100, 'lawngreen')
t.goto(-55, -50)
rectangle(15, 100, 'lawngreen')

# body
t.goto(-90, 100)
rectangle(100, 150, 'hotpink')

# arms
t.goto(-150, 70)
rectangle(60, 15, 'gold')
t.goto(-150, 110)
rectangle(15, 40, 'gold')

t.goto(10, 70)
rectangle(60, 15, 'gold')
t.goto(55, 110)
rectangle(15, 40, 'gold')

# neck
t.goto(-50, 120)
rectangle(15, 20, 'seashell')

# head
t.goto(-85, 170)
rectangle(80, 50, 'black')

# eyes
t.goto(-60, 160)
rectangle(30, 10, 'peru')
t.goto(-55, 155)
rectangle(5, 5, 'purple')
t.goto(-40, 155)
rectangle(5, 5, 'purple')

# mouth
t.goto(-65, 135)
t.right(5)
rectangle(40, 5, 'yellow')

t.hideturtle()
