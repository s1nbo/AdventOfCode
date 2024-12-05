from collections import defaultdict

ans = 0
rules = defaultdict(list) # key: int, value: list of ints that are not allowed to be before the key
pages = []

# read input
with open('05_data.txt') as f:
    rules_input = True
    for line in f:
        if line == '\n':
            rules_input = False
            continue
        
        if rules_input:
            line = line.strip().split('|')
            rules[int(line[0])].append(int(line[1]))
        else:
            pages.append(list(map(int, line.strip().split(','))))

# part 1
final_pages = []
wrong_pages = []
for page in pages:
    valid = True
    for i in range(len(page)):
        for j in range(0, i):
            if page[j] in rules[page[i]]:
                valid = False
                break
        if not valid:
            break
    if valid:
        final_pages.append(page)
    else:
        wrong_pages.append(page)
    
for page in final_pages:
    ans += page[len(page)//2]

print(ans)

# part 2
ans = 0
for page in wrong_pages:
    for i in range(len(page)):
        for j in range(0, i):
            if page[j] in rules[pages[i]]:
                page[j], page[i] = page[i], page[j]

    ans += page[len(page)//2]

print(ans)