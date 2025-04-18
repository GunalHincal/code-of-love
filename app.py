
import math
import turtle

def xt(t):
    return 16 * math.sin(t)**3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Drawing")

t = turtle.Turtle()
t.speed(0)  # Maksimum hız
t.pensize(2)

# Create heart outline
t.color("red")

# Başlangıç konumu
t.penup()
x = xt(0) * 10
y = yt(0) * 10
t.goto(x, y)
t.pendown()

# Kalp çizimi
for i in range(314):  # Yaklaşık 2*pi*50
    angle = i * 0.02
    x = xt(angle) * 10
    y = yt(angle) * 10
    t.goto(x, y)

t.hideturtle()
turtle.done()
