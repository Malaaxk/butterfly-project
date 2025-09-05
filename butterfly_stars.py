import turtle
import math
import random
import time

# إعداد الشاشة
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Butterfly with Stars and Name")
screen.setup(width=800, height=600)
screen.tracer(0)  # لتعطيل التحديث التلقائي

# إعداد الفراشة
butterfly = turtle.Turtle()
butterfly.speed(0)
butterfly.color("red", "pink")
butterfly.hideturtle()

# دالة لرسم جناح بشكل صحيح
def wing(t, scale, x_offset=0):
    t.penup()
    t.goto(x_offset, 0)  # بداية الجناح
    t.pendown()
    t.begin_fill()
    for angle in range(0, 361, 5):  # كل 5 درجات كفاية
        x = scale * math.sin(math.radians(angle)) * math.sin(math.radians(angle/2)) + x_offset
        y = scale * math.cos(math.radians(angle)) * math.sin(math.radians(angle/2))
        t.goto(x, y)
    t.end_fill()

# رسم الفراشة كاملة (جناحين)
wing(butterfly, 100, -50)  # الجناح الأيسر
wing(butterfly, 100, 50)   # الجناح الأيمن

# إعداد الاسم مع الإيموجي
name = turtle.Turtle()
name.hideturtle()
name.color("cyan")
name.penup()
name.goto(-80, -200)
name.write("Eng/Malak 💻", font=("Arial", 16, "bold"))

# إنشاء نجوم صغيرة متلألئة
stars = []
for _ in range(40):
    star = turtle.Turtle()
    star.hideturtle()
    star.color(random.choice(["yellow", "white"]))
    star.penup()
    star.goto(random.randint(-350,350), random.randint(-250,250))
    stars.append(star)

# دالة تحريك النجوم
def move_stars():
    for s in stars:
        x, y = s.position()
        x += random.uniform(-1.5, 1.5)
        y += random.uniform(-1.5, 1.5)
        x = max(-380, min(380, x))
        y = max(-280, min(280, y))
        s.goto(x, y)
        s.dot(random.randint(2,5))

# حلقة التحديث
while True:
    move_stars()
    screen.update()
    time.sleep(0.05)