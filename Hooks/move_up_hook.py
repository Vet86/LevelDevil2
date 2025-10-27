class MoveUpHook:
    def __init__(self, id, bbox, act_pos_x):
        self.id = id
        self.bbox = bbox
        self.act_pos_x = act_pos_x
        self.state = 0