# подключаем графическую библиотеку
from tkinter import *
# подключаем модули, которые отвечают за время и случайные числа
import time
import random


class Settings:
    def __init__(self):
        self.wnd_width = 500
        self.wnd_height = 400

        self.frm_background = 'Orange'
        self.frm_background_field = 'White'
        self.frm_margin = 5
        self.frm_margin_bottom = 82

        self.lvl_start_pos_x = 40
        self.lvl_start_pos_y = 300

        self.plr_color = 'Black'
        self.plr_width = 8
        self.plr_height = 18
        self.plr_jump_height = 55

        self.door_width = 20
        self.door_height = 30

        # self.door_pos_x =

settings = Settings()
# создаём новый объект — окно с игровым полем. В нашем случае переменная окна называется tk, и мы его сделали из класса Tk() — он есть в графической библиотеке 
tk = Tk()
# делаем заголовок окна — Games с помощью свойства объекта title
tk.title('Level Devil 2')
# запрещаем менять размеры окна, для этого используем свойство resizable 
tk.resizable(0, 0)
# помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить. Попробуйте :)
tk.wm_attributes('-topmost', 1)
# создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
canvas = Canvas(tk, width=settings.wnd_width, height=settings.wnd_height, highlightthickness=0)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты 
canvas.pack()
# обновляем окно с холстом
tk.update()

#  Описываем класс Player, который отвечает за платформы
class Player:
    # конструктор
    def __init__(self, canvas, settings, level):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя 
        self.id = canvas.create_polygon(
            -settings.plr_width/4, 0, 
            settings.plr_width/4, 0, 
            settings.plr_width/4, 4, 
            settings.plr_width/2, 4,
            settings.plr_width/2, settings.plr_height,
            -settings.plr_width/2, settings.plr_height,
            -settings.plr_width/2, 4,
            -settings.plr_width/4, 4,
            fill=settings.plr_color)
        # задаём список возможных стартовых положений платформы
        # выбираем первое из перемешанных
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.id, settings.lvl_start_pos_x, settings.lvl_start_pos_y)
        #self.canvas.move(self.id2, settings.lvl_start_pos_x, settings.lvl_start_pos_y)
        # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.x = 0
        self.y = 0

        self.jumping = False
        # платформа узнаёт свою ширину
        self.canvas_width = self.canvas.winfo_width()
        # задаём обработчик нажатий
        # если нажата стрелка вправо — выполняется метод turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Right>', self.turn_right_stop)
        # если стрелка влево — turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyRelease-Left>', self.turn_left_stop)
        # если стрелка влево — space()
        self.canvas.bind_all('<space>', self.jump)
        # пока платформа не двигается, поэтому ждём
        self.started = False
    # движемся вправо 
    def turn_right(self, event):
        if level.is_plaing == False:
            self.x = 0
            self.y = 0
            return

        pos = self.canvas.coords(self.id)
        # если мы не упёрлись в правую границу 
        if pos[2] <= level.left_right_x - settings.plr_width/2:
            self.x = 2

    # движемся вправо 
    def turn_right_stop(self, event):
        self.x = 0

    # движемся вправо 
    def turn_left_stop(self, event):
        self.x = 0

    # движемся влево
    def turn_left(self, event):
        if level.is_plaing == False:
            self.x = 0
            self.y = 0
            return
        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если мы не упёрлись в левую границу 
        if pos[0] >= level.left_bound_x + settings.plr_width:
            self.x = -2
    # прыжок
    def jump(self, event):
        if level.is_plaing == False:
            self.x = 0
            self.y = 0
            return

        if self.jumping == True:
            return

        self.jumping = True
        # будем смещаться левее на 2 пикселя по оси х
        self.y = -2

    # метод, который отвечает за движение платформы
    def draw(self):
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.id, self.x, 0)
        #self.canvas.move(self.id2, self.x, 0)

        self.canvas.move(self.id, 0, self.y)
        #self.canvas.move(self.id2, 0, self.y)

        if level.is_plaing == False:
            self.x = 0
            self.y = 0
            return

        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если мы упёрлись в левую границу 
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
        # если упёрлись в правую границу 
        elif pos[2] > level.left_right_x - settings.plr_width/2:
            # останавливаемся
            self.x = 0

        if self.y == -2 and pos[1] <= level.bottom_bound_y_with_player-settings.plr_jump_height:
            # останавливаемся
            self.y = 2

        elif self.y == 2 and pos[1] >= level.bottom_bound_y_with_player:
            # останавливаемся
            self.y = 0
            self.jumping = False

        if pos[0] >= (level.door_left_pos_x) and pos[2]<=level.door_left_pos_x+settings.door_width and self.jumping == False:
            level.is_plaing = False


class Frame:
    # конструктор
    def __init__(self, canvas, settings):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя 
        self.id = canvas.create_rectangle(0, 0, settings.wnd_width, settings.wnd_height, fill=settings.frm_background)

class Level:
    # конструктор
    def __init__(self, canvas, settings):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.is_plaing = True
        self.canvas = canvas
        self.left_bound_x = settings.frm_margin
        self.left_right_x = settings.wnd_width-settings.frm_margin
        self.bottom_bound_y = settings.wnd_height-settings.frm_margin_bottom
        self.bottom_bound_y_with_player = settings.wnd_height-settings.frm_margin_bottom-settings.plr_height

        self.door_left_pos_x = self.left_right_x -50
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя 
        self.level_id = canvas.create_rectangle(self.left_bound_x, settings.frm_margin, self.left_right_x, settings.wnd_height-settings.frm_margin_bottom, fill=settings.frm_background_field)
        self.exit_id = canvas.create_rectangle(self.door_left_pos_x, self.bottom_bound_y, self.door_left_pos_x + settings.door_width, self.bottom_bound_y - settings.door_height, fill='Grey')

#  Описываем класс Score, который отвечает за отображение счетов
class Score:
    # конструктор
    def __init__(self, canvas, player, color):
        self.player = player
        # в самом начале счёт равен нулю
        self.posx = 0
        self.posy = 0
        # будем использовать наш холст
        self.canvas = canvas
        # создаём надпись, которая показывает текущий счёт, делаем его нужно цвета и запоминаем внутреннее имя этой надписи
        self.id = canvas.create_text(400, 20, text='', font=('Courier', 15), fill=color)
    # обрабатываем касание платформы
    def draw(self):
        pos = self.player.canvas.coords(self.player.id)
        posx = pos[0]
        posy= pos[1]
        self.canvas.itemconfig(self.id, text=str(posx) + ' ' + str(posy) + ' ' + str(self.player.x) + ' ' + str(self.player.y))




# создаём фрейм
frame = Frame(canvas, settings)
level = Level(canvas, settings)
# создаём объект — белую платформу
player = Player(canvas, settings, level)
# создаём объект — зелёный счёт 
score = Score(canvas, player, 'green')
# создаём объект — красный шарик 
# ball = Ball(canvas, player, score, 'red')
# пока шарик не коснулся дна 
while True:
    # двигаем шарик
    # ball.draw()
    # двигаем платформу
    score.draw()
    player.draw()

    # обновляем наше игровое поле, чтобы всё, что нужно, закончило рисоваться
    tk.update_idletasks()
    # обновляем игровое поле и смотрим за тем, чтобы всё, что должно было быть сделано — было сделано
    tk.update()
    # замираем на одну сотую секунды, чтобы движение элементов выглядело плавно
    time.sleep(0.01)
# если программа дошла досюда, значит, шарик коснулся дна. Ждём 3 секунды, пока игрок прочитает финальную надпись, и завершаем игру
time.sleep(3)