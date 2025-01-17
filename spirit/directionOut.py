import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random
import spirit.spiritCommon.velocity as velocity

class directionOut:
    def fDirection(x, y, food_list, fish_list, hunter_list, cell_size, velocityDirection):
        addList = [0, cell_size * velocity.velocity(1), -1 * cell_size * velocity.velocity(1)]
        # 生成周围位置的坐标
        Nembor_list = []
        for dx in addList:
            for dy in addList:
                Nembor_list.append((x + dx, y + dy))
        res = -100

        #先判定八个格子里有没有食物
        for i in Nembor_list:
            if (i[0], i[1]) in food_list:
                if(i[0] - x == cell_size * velocity.velocity(1) and i[1] - y == 0):
                    res = 1
                if(i[0] - x == cell_size * velocity.velocity(1) and i[1] - y == -1 * cell_size * velocity.velocity(1)):
                    res = 2
                if(i[0] - x == 0 and i[1] - y == -1 * cell_size * velocity.velocity(1)):
                    res = 3
                if(i[0] - x == -1 * cell_size * velocity.velocity(1) and i[1] - y == -1 * cell_size * velocity.velocity(1)):
                    res = 4
                if(i[0] - x == -1 * cell_size * velocity.velocity(1) and i[1] - y == 0):
                    res = 5
                if(i[0] - x == -1 * cell_size * velocity.velocity(1) and i[1] - y == cell_size * velocity.velocity(1)):
                    res = 6
                if(i[0] - x == 0 and i[1] - y == cell_size * velocity.velocity(1)):
                    res = 7
                if(i[0] - x == cell_size * velocity.velocity(1) and i[1] - y == cell_size * velocity.velocity(1)):
                    res = 8 
                if(i[0] == x and i[1] == y):
                    res = 9                                                                
                return res                
            else:
                continue

        #如果周围没有食物
        for i in Nembor_list:
            #如果周围没有猎人
            if (i[0], i[1]) not in hunter_list:
                weights = [0.5, 0.2, 0.2, 0.1]
                return random.choices([velocityDirection, (velocityDirection - 2) % 8 + 1, (velocityDirection % 8) + 1, random.randint(1, 9)], weights=weights)[0]
            #如果附近有猎人，那就逃跑    
            elif (i[0], i[1]) in hunter_list:
                if(i[0] < x and i[1] < y):
                    return 8
                if(i[0] > x and i[1] < y):
                    return 6
                if(i[0] > x and i[1] > y):
                        return 4
                if(i[0] < x and i[1] > y):
                    return 2
                if(i[0] == x and i[1] < y):
                    return 7
                if(i[0] == x and i[1] > y):
                    return 3
                if(i[0] < x and i[1] == y):
                    return 1
                if(i[0] > x and i[1] == y):
                    return 5
                if(i[0] == x and i[1] == y):
                    return 9
                    
    
    def hDirection(x, y, food_list, fish_list, hunter_list, cell_size, velocityDirection):
        addList = [0, cell_size * velocity.velocity(1), -1 * cell_size * velocity.velocity(1), cell_size * velocity.velocity(2), -1 * cell_size * velocity.velocity(2)]
        Nembor_list = []
        for dx in addList:
            for dy in addList:
                Nembor_list.append((x + dx, y + dy))
        res = -100        
        #先判定八个格子里有没有鱼
        for i in Nembor_list:
            #如果有就追捕
            if (i[0], i[1]) in fish_list:
                if(i[0] < x and i[1] < y):
                    return 4
                if(i[0] > x and i[1] < y):
                    return 2
                if(i[0] > x and i[1] > y):
                    return 8
                if(i[0] < x and i[1] > y):
                    return 6
                if(i[0] == x and i[1] < y):
                    return 3
                if(i[0] == x and i[1] > y):
                    return 7
                if(i[0] < x and i[1] == y):
                    return 5
                if(i[0] > x and i[1] == y):
                    return 1
                if(i[0] == x and i[1] == y):
                    return 9                                                                
                return res 
            else:
                continue
            
       #如果周围没有鱼儿
        for i in Nembor_list:
            #如果周围没有鱼且离边界有一定距离：
            if (i[0], i[1]) not in fish_list:
                weights = [0.2, 0.2, 0.2, 0.4]
                return random.choices([velocityDirection, (velocityDirection - 2) % 8 + 1, (velocityDirection % 8) + 1, random.randint(1, 9)], weights=weights)[0]