ans1 = 0
ans2 = 0

def valid(line: list[int]) -> bool:
    if line == sorted(line) or line == sorted(line, reverse=True):
        
        safe = True
        for i in range(len(line)-1):   
            dif = abs(int(line[i]) - int(line[i+1]))
            if dif > 3 or dif == 0:
                safe = False
                break
        return safe
    
    return False


with open('02_data.txt') as f:
    for line in f:
        line = line.strip().split(' ')
        line = list(map(int, line))
        
        # Part 1
        ans1 += valid(line)
        
        # Part 2
        for i in range(len(line)):
            new_line = line[:i] + line[i+1:]
            if valid(new_line):
                ans2 += 1
                break

print(ans1)
print(ans2)