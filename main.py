from tkinter import Tk, Canvas
import time
import math
from random import randint
import random


class Car:
    def __init__(self, canvas, length, speed, color):
        self.length = length
        self.speed = speed
        self.color = color
        self.canvas = canvas
        self.rectangle = canvas.create_rectangle(165, 0, 185, length, fill=color)

    def move(self):
        self.canvas.move(self.rectangle, 0, self.speed*10)

    def __str__(self):
        return "A " + self.color + " car with length " + str(self.length) + " pix and a speed of " + str(self.speed)


class Car2:
    def __init__(self, canvas, length, speed, color):
        self.length = length
        self.speed = speed
        self.color = color
        self.canvas = canvas
        self.rectangle = canvas.create_rectangle(415, 1100-length, 435, 1100, fill=color)

    def move(self):
        self.canvas.move(self.rectangle, 0, -self.speed*10)

    def __str__(self):
        return "A " + self.color + " car with length " + str(self.length) + " pix and a speed of " + str(self.speed)


if __name__ == '__main__':
    root = Tk()
    # main global variables
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # canvas is a white piece of paper on which you can draw
    canvas = Canvas(root, width=width, height=height, bg="black")
    canvas.pack()

    # draw the green parks
    canvas.create_line(300, 0, 300, 1200, fill="white", dash=(20, 20))
    canvas.create_line(50, 0, 50, 1200, fill="white", dash=(20, 20))
    canvas.create_line(550, 0, 550, 1200, fill="white", dash=(20, 20))

    cars = []
    spawn = -11
    cars2 = []
    spawn2 = -11
    for i in range(1000):
        if spawn < i-10:
            if randint(0, 9) == 1:
                cars.append(Car(canvas, randint(30, 80), randint(5, 10)/10, random.choice(["blue", "green", "red", "yellow", "black", "white", "purple", "pink"])))
                spawn = i

        for car in cars:
            car.move()
            index = cars.index(car)
            prevcar = cars[index-1]

        if spawn2 < i-10:
            if randint(0, 9) == 1:
                cars2.append(Car2(canvas, randint(30, 80), randint(10, 15)/10, random.choice(["blue", "green", "red", "yellow", "black", "white", "purple", "pink"])))
                spawn2 = i

        for car2 in cars2:
            car2.move()

        # remove cars that drove out of the scene
        #if (car.pos_x < 0 or car.pos_x > width or car.pos_y < 0 or car.pos_y > height):
                #cars.remove(car)



        canvas.update()
        time.sleep(0.02)




    root.mainloop()
    print("finished")

