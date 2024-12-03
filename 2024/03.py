import re
ans = 0
active = True

with open('03_data.txt') as f:
    for line in f:
        nums = re.findall(r"mul\(\d+,\d+\)|don't|do", line)
        print(nums)
        for num in nums:
            # Part 2
            if num == "don't":
                active = False
            elif num == "do":
                active = True
            elif active:
                # Part 1
                num = num[4:-1].split(',')
                ans += int(num[0]) * int(num[1])

print(ans)
       


    
    