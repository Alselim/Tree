from tkinter import Tk, Canvas, Frame, BOTH
import time
import random


class Object:
    def __init__(self, x, y, colors):
        self.x = x
        self.y = y
        self.colors = colors


class Tree(Object):
    def __init__(self, x, y, colors):
        Object.__init__(self, x, y, colors)
        canvas.update()
        canvas.create_rectangle(x, y, x + 20, y + 20, outline="#bb4508", fill="#bb4508")
        canvas.create_polygon(x - 40, y, x + 10, y - 50, x + 60, y, x - 40, y, fill=colors)
        canvas.create_polygon(x - 30, y - 30, x + 10, y - 70, x + 50, y - 30, x - 30, y - 30, fill=colors)
        canvas.create_polygon(x - 20, y - 50, x + 10, y - 90, x + 40, y - 50, x - 20, y - 50, fill=colors)
        canvas.after(400)
        canvas.pack(fill=BOTH, expand=1)


def draw_first_yard():
    """
    Функция отвечает за отрисовку первого ряда ёлочек. По условиям первый ряд состояит из 10 ёлочек,
    цвет - зеленый, x,y - координаты левого верхнего угла ствола
    """
    x = 70
    y = 100
    for i in range(10):
        #colors = "red,orange,yellow,green,lightBlue,blue,violet,pink,grey,black,gold,silver".split(",")
        colors = "green"
        draw_tree = Tree(x, y, colors)
        x += 100


def main():
    global canvas
    tk = Tk()
    canvas = Canvas(tk, width=1055, height=600, bg='light green')
    canvas.pack
    draw_first_yard()
    tk.geometry("1055x600")
    tk.title("Рисуем лес")
    tk.mainloop()


if __name__ == '__main__':
    main()
