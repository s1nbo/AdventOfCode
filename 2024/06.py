ans = 0
grid = []


# read input

with open('06_data.txt') as f:
    for line in f:
        line = list(map(str, line.strip()))
        grid.append(line)
        for i in range(len(line)):
            if line[i] == '^':
                x1, x2 = i, len(grid) - 1
                
        



# Always turn right -> Up, Right, Down, Left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# part 1

i = 0
while  0 <= x1 < len(grid[0]) and 0 <= x2 < len(grid):

    
    if grid[x2][x1] == '.' or grid[x2][x1] == '^':
        ans += 1
        grid[x2][x1] = 'X'

    if grid[x2][x1] != '#':
        x1 += directions[i][0]
        x2 += directions[i][1]
    else:
        x1 -= directions[i][0]
        x2 -= directions[i][1]
        i = (i + 1) % 4
        x1 += directions[i][0]
        x2 += directions[i][1]
    

print(ans)