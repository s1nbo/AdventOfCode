#dfs approach

ans = 0
grid = []
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
target = ['X', 'M', 'A', 'S']

# read input
with open('04_data.txt') as f:
    for line in f:
        line = line.strip()
        grid.append(list(map(str, line)))

def is_valid(i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i])
# Part 1
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
            for d in directions:
                found = True
                for k in range(1, 4):
                    new_i, new_j = i + k * d[0], j + k * d[1]
                    if not is_valid(new_i, new_j) or grid[new_i][new_j] != target[k]:
                        found = False
                        break
                if found:
                    ans += 1
print(ans)

# Part 2
ans = 0
directions = directions[6:]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'A':
            if is_valid(i + 1, j + 1) and is_valid(i - 1, j - 1) and is_valid(i + 1, j - 1) and is_valid(i - 1, j + 1):
                if (grid[i + 1][j + 1] == 'M' and grid[i - 1][j - 1] == 'S') or (grid[i + 1][j + 1] == 'S' and grid[i - 1][j - 1] == 'M'):
                    if (grid[i + 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'S') or (grid[i + 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'M'):
                        ans += 1
            
            
print(ans)
        