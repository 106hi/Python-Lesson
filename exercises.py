nums = [1, 2, 4, 3, 2, 1, 5, 1]
num2freq = {}
for num in nums:
    num2freq[num] = num2freq.get(num, 0) + 1
print(num2freq)