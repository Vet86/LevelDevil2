import sys
import os

sys.path.append(os.path.abspath("Hooks\."))
from game_state import *
from simple_hook import *
from move_up_hook import *

class Game:
    # конструктор
    def __init__(self, canvas, settings, player, level):
        self.player = player
        self.level = level
        self.canvas = canvas
        self.settings = settings
        self.game_state = GameState.InProcess
        self.player.can_move = True
        pass
 
    def calc(self):
        pos = self.canvas.coords(self.player.id)
        if self.game_state == GameState.InProcess and pos[0] >= (self.level.door_left_pos_x) and pos[2]<=self.level.door_left_pos_x+self.settings.door_width and self.player.jumping == False:
            self.game_state = GameState.FinishSuccessfully
            self.player.can_move = False

        bound_player = self.canvas.bbox(self.player.id)
        m = 3
        for hook in self.level.hooks:
            if type(hook) is MoveUpHook and hook.state == 0 and pos[0] >= hook.act_pos_x:
                hook.state = 1
            bbox = hook.bbox
            if (bound_player[0] < bbox[2] -m and bound_player[2] > bbox[0] + m and
                bound_player[1] < bbox[3] -m and bound_player[3] > bbox[1] + m):
                self.game_state = GameState.FinishUnsuccessfully