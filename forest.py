from tkinter import Tk, Canvas, Frame, BOTH
import random


class Object:
    def __init__(self, x, y, color_trunk, colors_needles):
        self.x = x
        self.y = y
        self.colors_needles = colors_needles
        self.color_trunk = color_trunk


class Tree(Object):
    def __init__(self, x, y, color_trunk, colors_needles):
        Object.__init__(self, x, y, color_trunk, colors_needles)
        canvas.update()
        canvas.create_rectangle(x, y, x + 20, y + 20, outline=color_trunk, fill=color_trunk)
        canvas.create_polygon(x - 40, y, x + 10, y - 50, x + 60, y, x - 40, y, fill=colors_needles)
        canvas.create_polygon(x - 30, y - 30, x + 10, y - 70, x + 50, y - 30, x - 30, y - 30, fill=colors_needles)
        canvas.create_polygon(x - 20, y - 50, x + 10, y - 90, x + 40, y - 50, x - 20, y - 50, fill=colors_needles)
        canvas.create_polygon(x - 10, y - 60, x + 10, y - 100, x + 30, y - 60, x - 10, y - 60, fill=colors_needles)
        # canvas.after(400)
        canvas.pack(fill=BOTH, expand=1)


def draw(x, y, n, dx1, dx2, dt_start, dt_end, color_trunk, color_needles):
    """
    Функция отвечает за отрисовку ёлок в зависимости от входящих условия
    :param x: левая верхняя координата ствола по оси х
    :param y: левая верхняя координата ствола по оси у
    :param n: количество ёлочек
    :param dx1: изменение координаты х последующей елки относительно предыдущей min
    :param dx2: изменение координаты х последующей елки относительно предыдущей max
    :param dt_start: Начало дельты времени появления следующей ёлки
    :param dt_end: Конец дельты времени появления следующей ёлки
    :param color_trunk: цвет ствола
    :param color_needles: цвет иголок
    :return: Ничего не возвращает
    """
    for i in range(n):
        print(color_trunk)
        draw_tree = Tree(x, y, random.choice(color_trunk), color_needles[i])
        canvas.after(random.randint(dt_start, dt_end))
        x += random.randint(dx1, dx2)


def main():
    global canvas
    tk = Tk()
    canvas = Canvas(tk, width=1055, height=600, bg='light green')
    draw(70, 100, 10, 100, 100, 400, 400, "#bb4508".split(","),
         "#FF0000,#B22222,#8B0000,#B22222,#CD5C5C,#FA8072,#F08080,#FF4500,#A52A2A,#800000".split(","))
    draw(120, 250, 5, 200, 200, 0, 0, "#bb4508".split(","),
         "#008000,#9ACD32,#32CD32,#ADFF2F,#556B2F".split(","))
    draw(70, 400, 5, 70, 200, 300, 5000, "red,orange,yellow,green,lightBlue,blue,"
                                         "violet,pink,grey,black,gold,silver".split(","),
         "#0000FF,#00008B,#00BFFF,#1E90FF,#6495ED".split(","))
    canvas.pack
    tk.geometry("1055x600")
    tk.title("Рисуем лес")
    tk.mainloop()


if __name__ == '__main__':
    main()