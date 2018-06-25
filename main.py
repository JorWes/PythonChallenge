from tkinter import Tk, Canvas
import time
import math
from random import randint
import random


class Car:
    def __init__(self, canvas, length, speed, ypos, color):
        self.length = length
        self.speed = speed
        self.color = color
        self.canvas = canvas
        self.ypos = ypos
        self.rectangle = canvas.create_rectangle(165, ypos, 185, ypos+length, fill=color)

    def move(self):
        self.canvas.move(self.rectangle, 0, self.speed*10)
        self.ypos = self.ypos + self.speed*10

    def __str__(self):
        return "A " + self.color + " car with length " + str(self.length) + " pix and a speed of " + str(self.speed)


class Car2:
    def __init__(self, canvas, length, speed, ypos, color):
        self.length = length
        self.speed = speed
        self.color = color
        self.canvas = canvas
        self.ypos = ypos
        self.rectangle = canvas.create_rectangle(415, ypos-length, 435, ypos, fill=color)

    def move(self):
        self.canvas.move(self.rectangle, 0, -self.speed*10)
        self.ypos = self.ypos - self.speed*10

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
    for i in range(3000):
        if spawn < i-25:
            if randint(0, 9) == 1:
                cars.append(Car(canvas, randint(30, 60), randint(2, 8)/10, -100, random.choice(["blue", "green", "red", "yellow", "black", "white", "purple", "pink"])))
                spawn = i

        for car_index, car in enumerate(cars):
            if car_index > 0:
                prev_car = cars[car_index-1]
                if prev_car.ypos > car.ypos + car.length + 50:
                    car.move()
            else:
                car.move()

        if spawn2 < i-10:
            if randint(0, 9) == 1:
                cars2.append(Car2(canvas, randint(30, 60), randint(2, 11)/10, 1300, random.choice(["blue", "green", "red", "yellow", "black", "white", "purple", "pink"])))
                spawn2 = i

        for car_index2, car2 in enumerate(cars2):
            if car_index2 > 0:
                prev_car2 = cars2[car_index2-1]
                if prev_car2.ypos < car2.ypos - prev_car2.length - 50:
                    car2.move()
            else:
                car2.move()



        # remove cars that drove out of the scene
        #if (car.pos_x < 0 or car.pos_x > width or car.pos_y < 0 or car.pos_y > height):
                #cars.remove(car)



        canvas.update()
        time.sleep(0.01)




    root.mainloop()
    print("finished")

