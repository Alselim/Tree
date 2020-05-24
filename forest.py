from tkinter import Tk, Canvas, Frame, BOTH
import time


class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Tree(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y)
        canvas.create_rectangle(x, y, x + 20, y + 20, outline="#bb4508", fill="#bb4508")
        canvas.create_polygon(x - 40, y, x + 10, y - 50, x + 60, y, x - 40, y, fill="green")
        canvas.create_polygon(x - 30, y - 30, x + 10, y - 70, x + 50, y - 30, x - 30, y - 30, fill="green")
        canvas.create_polygon(x - 20, y - 50, x + 10, y - 90, x + 40, y - 50, x - 20, y - 50, fill="green")
        canvas.pack(fill=BOTH, expand=1)


def main():
    x = 70
    y = 100
    root = Tk()
    global canvas
    canvas = Canvas(root, width=1024, height=800, bg='white')
    canvas.pack
    i = 0
    while i < 10:
        draw_tree = Tree(x, y)
        x += 100
        i += 1
    root.geometry("1055x600")
    root.title("Рисуем лес")
    root.mainloop()


if __name__ == '__main__':
    main()
