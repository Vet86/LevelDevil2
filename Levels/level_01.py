import sys
import os

sys.path.append(os.path.abspath("..\."))
from hook import *

class Level1:
    # конструктор
    def __init__(self, canvas, settings):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
    
        self.canvas = canvas
        self.left_bound_x = settings.frm_margin
        self.left_right_x = settings.wnd_width-settings.frm_margin
        self.bottom_bound_y = settings.wnd_height-settings.frm_margin_bottom
        self.bottom_bound_y_with_player = settings.wnd_height-settings.frm_margin_bottom-settings.plr_height

        self.door_left_pos_x = self.left_right_x - 50
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя 
        self.level_id = canvas.create_rectangle(self.left_bound_x, settings.frm_margin, self.left_right_x, settings.wnd_height-settings.frm_margin_bottom, fill=settings.frm_background_field)
        self.exit_id = canvas.create_rectangle(self.door_left_pos_x, self.bottom_bound_y, self.door_left_pos_x + settings.door_width, self.bottom_bound_y - settings.door_height, fill='Grey')
        self.hook_id = canvas.create_polygon(self.left_bound_x + 200, self.bottom_bound_y, 
                                        self.left_bound_x + 200, self.bottom_bound_y - 20, 
                                        self.left_bound_x + 200 + 20, self.bottom_bound_y - 20, 
                                        self.left_bound_x + 200 + 20, self.bottom_bound_y, 
                                        self.left_bound_x + 200, self.bottom_bound_y, 
                                        fill='Grey')

        self.name = 'Уровень 1'

        self.lvl_start_pos_x = 40
        self.lvl_start_pos_y = 300

        hook1 = Hook(canvas.bbox(self.hook_id))
        self.hooks = [hook1]
    
    def destruct(self):
        self.canvas.delete(self.level_id)
        self.canvas.delete(self.exit_id)
        self.canvas.delete(self.hook_id)