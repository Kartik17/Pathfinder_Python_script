# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import copy

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
		]
		
heuristic = [[9, 8, 7, 6, 5, 4],
			[8, 7, 6, 5, 4, 3],
			[7, 6, 5, 4, 3, 2],
			[6, 5, 4, 3, 2, 1],
			[5, 4, 3, 2, 1, 0],
			]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
expand_time = 0
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def add_open_list(current,open_list,new_grid,action_grid):
	for i in xrange(len(delta)):
		grid_i = delta[i][0] + current[1]
		grid_j = delta[i][1] + current[2]
		if grid_i<0 or grid_j<0 or grid_i>len(grid)-1 or grid_j>len(grid[0])-1:
			continue
		elif grid[grid_i][grid_j] != 1 and new_grid[grid_i][grid_j] != 1 :
			new_grid[grid_i][grid_j] = 1
			action_grid[grid_i][grid_j] = i
			open_list.append([current[0]+1,grid_i,grid_j])
	return open_list
	
	
def search(grid,init,goal,cost,expand_time):
    path_grid = [[' ' for i in grid[j]] for j in range(len(grid))]
    action_grid = [[-1 for i in grid[j]] for j in range(len(grid))]
    expanse_grid = [[-1 for i in grid[j]] for j in range(len(grid))]
    new_grid = [[i for i in grid[j]] for j in range(len(grid))]
	
    open_list = []
    current = [0,init[0],init[1],' ']
	
    while([current[1],current[2]] != goal):
		new_grid[current[1]][current[2]] = 1
		expanse_grid[current[1]][current[2]] = expand_time
		open_list = add_open_list(current,open_list,new_grid,action_grid)
		expand_time += 1 
		if open_list == []:
			print 'fail'
			break
		open_list.sort()
		current = open_list.pop(0)
		
    x_current = goal[0]
    y_current = goal[1]
    path_grid[x_current][y_current]= '*'
	
    while x_current != init[0] or y_current != init[1]:
		x1 = x_current - delta[action_grid[x_current][y_current]][0]
		y1 = y_current - delta[action_grid[x_current][y_current]][1]
		
		path_grid[x1][y1] = delta_name[action_grid[x_current][y_current]]
		x_current = x1
		y_current = y1

    return current,expanse_grid, action_grid,path_grid

	
test_grid = search(grid,init,goal,cost,expand_time)[3]
for row in grid:
	print row
	
print "Solution - Shortest Path"

for row in test_grid:
	print row
#print search(grid,init,goal,cost,expand_time)[2]


