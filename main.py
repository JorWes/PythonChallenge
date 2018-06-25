from tkinter import Tk, Canvas
import time
import math


class Car:
    def __init__(self, canvas, length, speed, color):
        self.length = length
        self.speed = speed
        self.color = color
        self.canvas = canvas
        self.rectangle = canvas.create_rectangle(100, 0, 200, length, fill=color)

    def move(self):
        self.canvas.move(self, 10, 0)

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
    canvas.create_line(300, 0, 300, 900, fill="white", dash=(20, 20))
    x = Car(canvas, 100, 1, "green")
    for i in range(100):
        canvas.update()
        time.sleep(0.02)
        move(Car.x)


    root.mainloop()

    print("test")

