import math
t = int(input())
l, X, Y = map(int, input().split())
q = int(input())

chokudai_list = [X, Y, 0]

x, y, z = 0,1,2

def cal_rad(co_list_1, co_list_2):
    horizon = ((co_list_2[x]-co_list_1[x]) ** 2 + (co_list_2[y]-co_list_1[y]) ** 2) ** 0.5
    edge = (horizon**2 + (co_list_2[z] - co_list_1[z])**2)**0.5
    return math.degrees(math.acos(horizon/edge))

def cal_coordinate(time, height, cycle):
    time = time % cycle
    rad_per_of_cycle = time / cycle
    rad = 360 * rad_per_of_cycle
    r_z = (height/2) * math.sin(math.radians(270-rad)) + (height/2)
    r_y = (height/2) * math.cos(math.radians(270-rad))
    return [0, r_y, r_z]

for _ in range(q):
    e = int(input())
    e_list = cal_coordinate(e, l, t)
    print(cal_rad(e_list, chokudai_list))
