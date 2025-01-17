import random
import spirit.spiritCommon.velocity as velocity
class move_rule:
    def fish_move(x, y, direction, board_size, cell_size):
        #移动规则   
        original_x = x
        original_y = y

        #这里要加移动的判定规则
        cell_size *= velocity.velocity(1)
        if direction == 1:
            x += cell_size
        elif direction == 2:
            x += cell_size
            y -= cell_size
        elif direction == 3:
            y -= cell_size
        elif direction == 4:
            x -= cell_size
            y -= cell_size
        elif direction == 5:
            x -= cell_size
        elif direction == 6:
            y += cell_size
            x -= cell_size
        elif direction == 7:
            y += cell_size
        elif direction == 8:
            x += cell_size
            y += cell_size
        else:
            x = x
            y = y
        if x < cell_size / 2 or y < cell_size / 2 or x > (board_size - 0.5) * cell_size or y > (board_size - 0.5) * cell_size:
            return original_x, original_y
        return x, y

    def hunter_move(x, y, direction, board_size, cell_size):
        original_x = x
        original_y = y
        cell_size_copy = cell_size
        cell_size *= velocity.velocity(2)
        #这里要加移动的判定规则
        if direction == 1:
            x += cell_size
        elif direction == 2:
            x += cell_size
            y -= cell_size
        elif direction == 3:
            y -= cell_size
        elif direction == 4:
            x -= cell_size
            y -= cell_size
        elif direction == 5:
            x -= cell_size
        elif direction == 6:
            y += cell_size
            x -= cell_size
        elif direction == 7:
            y += cell_size
        else:
            x += cell_size
            y += cell_size
        if x < cell_size_copy * 2.5 or y < cell_size_copy * 2.5 or x > (board_size - 2.5) * cell_size_copy or y > (board_size - 2.5) * cell_size_copy:
            return original_x, original_y
        return x, y


def eat(self, x, y):
    pass
