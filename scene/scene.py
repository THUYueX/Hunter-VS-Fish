import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random
from spirit.rules import move_rule
from spirit.directionOut import directionOut
import run
class figure:
    def __init__(self, board_size, cell_size):
        self.board_size = board_size
        self.cell_size = cell_size
        self.fig, self.ax = None, None
        self.coordinates = []

    # 绘制  网格
    def draw_board(self):
        if self.fig and self.ax:
            return
        self.fig, self.ax = plt.subplots()

        # 绘制棋盘网格
        for i in range(self.board_size + 1):
            self.ax.axhline(i * self.cell_size, color='black')
            self.ax.axvline(i * self.cell_size, color='black')

        # 设置坐标轴范围和刻度
        self.ax.set_xlim(0, self.board_size * self.cell_size)
        self.ax.set_ylim(0, self.board_size * self.cell_size)
        self.ax.set_xticks(range(0, self.board_size * self.cell_size + 1, self.cell_size))
        self.ax.set_yticks(range(0, self.board_size * self.cell_size + 1, self.cell_size))

        # 隐藏坐标轴刻度
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])

    def draw_spirit(self, catagery, x, y, flag, food_list, fish_list, hunter_list, velocityDirection):
        if catagery == 'food':
            if flag == False:
                x, y = coordinate_detection(self.board_size, self.cell_size)
                while(x, y) in self.coordinates:
                    x, y = coordinate_detection(self.board_size, self.cell_size)
                    self.coordinates.append((x, y))           
            self.ax.scatter(x, y, color='red', s=self.cell_size * 0.4)
            # 绘制浅红色圆环
            ring_radius = self.cell_size * 0.5  # 圆环半径
            light_red_color = (1.0, 0.7, 0.7)  # 浅红色RGB值
            circle = Circle((x, y), ring_radius, color=light_red_color, fill=False)
            self.ax.add_patch(circle)


            return x, y

        elif catagery == 'hunter':
            action_number = random.randint(1, 9)
            if flag == False:
                x, y = coordinate_detection(self.board_size, self.cell_size)
                while(x, y) in self.coordinates:
                    x, y = coordinate_detection(self.board_size, self.cell_size)
                    self.coordinates.append((x, y))
            if flag == True:
                action_number = directionOut.hDirection(x, y, food_list, fish_list, hunter_list, self.cell_size, velocityDirection)
                x, y = move_rule.hunter_move(x, y, action_number, self.board_size, self.cell_size)
            self.ax.scatter(x, y, color='black', s=self.cell_size * 2)
            return x, y, action_number
        

        elif catagery == 'fish':
            action_number = random.randint(1, 9)
            if flag == False:
                x, y = coordinate_detection(self.board_size, self.cell_size)
                while(x, y) in self.coordinates:
                    x, y = coordinate_detection(self.board_size, self.cell_size)
                    self.coordinates.append((x, y))
            if flag == True:
                action_number = directionOut.fDirection(x, y, food_list, fish_list, hunter_list, self.cell_size, velocityDirection)
                x, y = move_rule.fish_move(x, y, action_number, self.board_size, self.cell_size)
            self.ax.scatter(x, y, color='blue', s=self.cell_size * 1)
            return x, y, action_number
#坐标生成
def coordinate_detection(board_size, cell_size):
    x = (random.randint(0, board_size - 1) + 0.5) * cell_size
    y = (random.randint(0, board_size - 1) + 0.5) * cell_size
    return x, y

        


        
