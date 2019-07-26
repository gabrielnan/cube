import numpy as np
from itertools import product
cube = [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0]
len(cube)



def solve(pos, i, dir): 
    if np.any(pos > 2) or np.any(pos < 0) or visited[tuple(pos)] != 0:
        return
    visited[tuple(pos)] = 1
    pos_list.append(tuple(pos))
    i += 1
    if i == len(cube):
        print('found solution!!!!!')
        print_sol(pos_list)
    else:
        if cube[i]:
            for next_dir in side_dirs(dir[0]):
                next_pos = pos + eye[next_dir[0]] * next_dir[1]
                solve(next_pos, i, next_dir)
        else:
            next_pos = pos + eye[dir[0]] * dir[1]
            solve(next_pos, i, dir)
    
    visited[tuple(pos)] = 0
    pos_list.pop()


def side_dirs(axis):
    axes = {0, 1, 2}
    axes.remove(axis)
    return product(axes, [-1, 1])

def print_sol(poses):
    for i, pos in enumerate(poses):
        print(f'{i:<2}: {pos}')

    
visited = np.zeros([3, 3, 3])
eye = np.eye(3, dtype=int)
init_pos = np.array([0, 0, 0])
init_dir = (0, 1)
i = -1
pos_list = []
solve(init_pos, i, init_dir)
