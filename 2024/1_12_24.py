left, right = [], []
ans = 0

# Read input
for line in open('1_12_24_data.csv'):
    line = line.split('   ')
    left.append(int(line[0]))
    right.append(int(line[1]))


# Sort input
left.sort()
right.sort()
for i in range(len(left)):
    ans += abs(left[i] - right[i])

print(ans)