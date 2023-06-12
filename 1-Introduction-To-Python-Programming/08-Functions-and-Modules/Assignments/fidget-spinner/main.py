from turtle import *

fidget = {
    "size": 120,
    "length": 100,
    "speed": 0,
    "friction": .96,
    "colors": ["purple", "red", "blue"],
    "flickSpeed": 30,
}


def spinner():
    clear()
    angle = fidget["speed"] / 10
    right(angle)
    forward(fidget["length"])
    dot(fidget["size"], fidget["colors"][0])
    back(fidget["length"])
    right(fidget["size"])
    forward(fidget["length"])
    dot(fidget["size"], fidget["colors"][1])
    back(fidget["length"])
    right(fidget["size"])
    forward(fidget["length"])
    dot(fidget["size"], fidget["colors"][2])
    back(fidget["length"])
    right(fidget["size"])
    update()


def animate():
    if fidget["speed"] > 0:
        fidget["speed"] *= .99
    if fidget["speed"] < 1:
        fidget["speed"] = 0

    spinner()
    ontimer(animate, 20)


def flick():
    fidget["speed"] += fidget["flickSpeed"]


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, "space")
listen()
animate()
done()
