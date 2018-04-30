# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']
from operator import itemgetter
def compute_value(grid,goal,cost):
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    new_grid = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True
    current = [goal[0],goal[1]]
    value[current[0]][current[1]] = 0
    new_grid[current[0]][current[1]] = '*'
    next_point = []
    count =0 
    while change:
        count +=1
        change = False
        for i in xrange(len(delta)):
            x = current[0] + delta[i][0]
            y = current[1] + delta[i][1]
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]):
                #print x,y
                if grid[x][y]!=1 and value[x][y]==99:
                    value[x][y] = value[current[0]][current[1]] + cost
                    print str(value[x][y]) + '('+ str(x) +','+ str(y) +')'
                    new_grid[x][y] = delta_name[(i+2)%4]
                    next_point.append((value[x][y],x,y))
                    #print next_point
        if len(next_point) == 0:
            change = False
        else:
            change = True
            next_point = sorted(next_point)
            temp = next_point.pop(0)
            #print next_point
            current[0], current[1] = temp[1], temp[2]
    for row in new_grid:
        print row 
    print count

compute_value(grid,goal,cost)






















'''        change = False
        for i in xrange(len(delta)):#Assigning the direction to transverse
		    x = delta[i][0] + current[0]
		    y = delta[i][1] + current[1]
            if x>0 and y>0 and x<len(grid) and y<len(grid[0]):
                if grid[x][y] != 1 and new_grid[x][y] == 99:
                    next_coor.append([cost,[x,y],delta[i]])
                    print next_coor
                    new_grid[x][y] += cost -99
                    change = True

        cost+=1
        next_coor = next_coor.sort()
        print next_coor
        current[0] = next_coor[1][0]
        current[1] = next_coor[1][1]
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return new_grid 
    

    
print compute_value(grid,goal,cost)
'''