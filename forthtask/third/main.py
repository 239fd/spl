class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка посредством {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка с помощью  {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка {self.title}")

pen = Pen("синей ручки")
pencil = Pencil("черного карандаша")
marker = Handle("красным маркером")

pen.draw()
pencil.draw()
marker.draw()
