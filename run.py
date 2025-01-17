import os
from scene import scene
from spirit import rules
import matplotlib.pyplot as plt
import math
import random

if __name__ == "__main__":

    #场景生成
    #鱼和猎人数量
    n_fish = 5
    n_hunter = 2
    n_food = 2
    fish_list = []
    hunter_list = []
    food_list = []
    
    # 棋盘大小和单元大小
    board_size = 16
    cell_size = 80
    figure_instance = scene.figure(board_size, cell_size)
    # 最大时间
    max_time = 500
    
    #初始生成并保存地图
    figure_instance.draw_board()
    for _ in range(n_hunter):
        hunter_x, hunter_y, hunterVelocityDirection = figure_instance.draw_spirit('hunter', 1, 1, False, food_list, fish_list, hunter_list, 9)
        hunter_list.append((hunter_x, hunter_y, hunterVelocityDirection)) 

    for _ in range(n_fish):
        fish_x, fish_y, fishVelocityDirection= figure_instance.draw_spirit('fish', 1, 1, False, food_list, fish_list, hunter_list, 9)
        fish_list.append((fish_x, fish_y, fishVelocityDirection))    

    for _ in range(n_food):
        food_x, food_y = figure_instance.draw_spirit('food', 1, 1, False, food_list, fish_list, hunter_list, 9)
        food_list.append((food_x, food_y)) 
            

    plt.ion()
    timestep = 0

    while(max_time > 0):
        fishLeft = len(fish_list)
        foodLeft = len(food_list)
        figure_instance = scene.figure(board_size, cell_size)
        figure_instance.draw_board()
        # 更新标题以显示当前时间步
        figure_instance.ax.set_title(f'Timestep: {timestep}\nFish Left:{fishLeft} Food Left:{foodLeft}')
        #打乱坐标元组 他们哪个先动都是随机的
        fish_list_mutable = list(fish_list)
        hunter_list_mutable = list(hunter_list)
        random.shuffle(fish_list_mutable)
        random.shuffle(fish_list_mutable)

        for i in range(len(food_list)):
            foodi_x, foodi_y = food_list[i]
            food_list[i] = figure_instance.draw_spirit('food', foodi_x, foodi_y, True, food_list, fish_list, hunter_list, 9)

        for i in range(len(fish_list)):
            fishi_x, fishi_y, fishVelocityDirection = fish_list[i]
            fish_list[i] = figure_instance.draw_spirit('fish', fishi_x, fishi_y, True, food_list, fish_list, hunter_list, fishVelocityDirection)
            
            #绘制箭头
            update_fishi_x, update_fishi_y, _ = fish_list[i]
            # 绘制箭头，表示鱼类的移动方向
            # 这里假设fishVelocityDirection是一个表示角度的值（以度为单位）
            arrow_head_length = 0.1  # 箭头头部长度，相对于箭杆长度
            arrow_head_width = 0.05  # 箭头头部宽度，相对于箭杆宽度
            arrow_style = '-|>'  # 箭头样式
            # 这里简单地将箭头长度设置为0.2倍的cell_size，您可以根据需要调整
            arrow_length = figure_instance.cell_size * 0.2
            # 绘制箭头
            figure_instance.ax.annotate('', xy=(update_fishi_x, update_fishi_y), xytext=(fishi_x, fishi_y),
                                        arrowprops=dict(arrowstyle=arrow_style,
                                                        connectionstyle="arc3,rad=-0.2",
                                                        color='blue',
                                                        shrinkA=5, shrinkB=5,
                                                        patchA=None, patchB=None,
                                                        relpos=(0.5, 0.5),  # 修改此处
                                                        # 删除head_length和head_width
                                                        ))
            #食物是否吃掉检测
            for foodi in food_list:
                for fishi in fish_list:
                    foodi_x, foodi_y = foodi
                    fishi_x, fishi_y, _ = fishi
                    if(foodi_x == fishi_x and foodi_y == fishi_y):
                        food_list.remove(foodi)


        for i in range(len(hunter_list)):
            hunteri_x, hunteri_y, hunterVelocityDirection = hunter_list[i]
            hunter_list[i] = figure_instance.draw_spirit('hunter', hunteri_x, hunteri_y, True, food_list, fish_list, hunter_list, hunterVelocityDirection)
                        #绘制箭头
            update_hunteri_x, update_hunteri_y, _ = hunter_list[i]
            # 绘制箭头，表示鱼类的移动方向
            # 这里假设fishVelocityDirection是一个表示角度的值（以度为单位）
            arrow_head_length = 0.1  # 箭头头部长度，相对于箭杆长度
            arrow_head_width = 0.05  # 箭头头部宽度，相对于箭杆宽度
            # 这里简单地将箭头长度设置为0.2倍的cell_size，您可以根据需要调整
            arrow_length = figure_instance.cell_size * 0.2
            # 绘制箭头
            figure_instance.ax.annotate('', xy=(update_hunteri_x, update_hunteri_y), xytext=(hunteri_x, hunteri_y),
                                        arrowprops=dict(arrowstyle=arrow_style,
                                                        connectionstyle="arc3,rad=-0.2",
                                                        color='black',
                                                        shrinkA=5, shrinkB=5,
                                                        patchA=None, patchB=None,
                                                        relpos=(0.5, 0.5),  # 修改此处
                                                        # 删除head_length和head_width
                                                        ))

            #鱼儿是否吃掉检测
            for fishi in fish_list:
                for hunteri in hunter_list:
                    fishi_x, fishi_y, _ = fishi
                    hunteri_x, hunteri_y, _ = hunteri
                    if(hunteri_x == fishi_x and hunteri_y == fishi_y):
                        fish_list.remove(fishi)

        plt.pause(0.5)
        plt.close()

        max_time -= 1
        timestep += 1
        
    