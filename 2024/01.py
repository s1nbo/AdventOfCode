left, right = [], []
ans1 = 0
ans2 = 0

# Read input
for line in open('01.csv'):
    line = line.split('   ')
    left.append(int(line[0]))
    right.append(int(line[1]))


# Sort input
left.sort()
right.sort()

# Part 1
for i in range(len(left)):
    ans1 += abs(left[i] - right[i])
print(ans1)

# Part 2
from collections import Counter
right_counter = Counter(right)

for i in range(len(left)):
    ans2 += right_counter[left[i]] * left[i]

print(ans2)
