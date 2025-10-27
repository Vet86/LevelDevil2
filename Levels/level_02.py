import sys
import os

sys.path.append(os.path.abspath("..\."))
from move_up_hook import *

class Level2:
    # конструктор
    def __init__(self, canvas, settings):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте                
        self.name = 'Уровень 2'
        self.is_plaing = True
        self.canvas = canvas
        self.left_bound_x = settings.frm_margin
        self.left_right_x = settings.wnd_width-settings.frm_margin
        self.bottom_bound_y = settings.wnd_height-settings.frm_margin_bottom
        self.bottom_bound_y_with_player = settings.wnd_height-settings.frm_margin_bottom-settings.plr_height

        self.door_left_pos_x = self.left_right_x - 100
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя 
        self.level_id = canvas.create_rectangle(self.left_bound_x, settings.frm_margin, self.left_right_x, settings.wnd_height-settings.frm_margin_bottom, fill=settings.frm_background_field)
        self.exit_id = canvas.create_rectangle(self.door_left_pos_x, self.bottom_bound_y, self.door_left_pos_x + settings.door_width, self.bottom_bound_y - settings.door_height, fill='Grey')


        self.lvl_start_pos_x = 20
        self.lvl_start_pos_y = 300

        self.start_level()

    def destruct(self):
        self.canvas.delete(self.level_id)
        self.canvas.delete(self.exit_id)

    def calc(self):
        for hook in self.hooks:
            if type(hook) is MoveUpHook and hook.state == 1:
                self.canvas.move(hook.id, 0, -2)
                hook.bbox = self.canvas.bbox(hook.id)

    def start_level(self):
        if hasattr(self, 'hook_id'):
            self.canvas.delete(self.hook_id)
        self.hook_id = self.canvas.create_polygon(self.left_bound_x + 200, self.bottom_bound_y, 
                                        self.left_bound_x + 200, self.bottom_bound_y - 20, 
                                        self.left_bound_x + 200 + 20, self.bottom_bound_y - 20, 
                                        self.left_bound_x + 200 + 20, self.bottom_bound_y, 
                                        self.left_bound_x + 200, self.bottom_bound_y, 
                                        fill='Grey')

        hook1 = MoveUpHook(self.hook_id, self.canvas.bbox(self.hook_id), self.left_bound_x + 180)
        self.hooks = [hook1]