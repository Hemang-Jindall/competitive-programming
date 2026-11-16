nums = list(map(int, input().split()))
freq = {}

for x in nums:
    freq[x] = freq.get(x,0) + 1

print(freq)
        
ans = []

while len(ans) < len(nums):
    for x in sorted(freq.keys()):
        if freq[x] > 0:
            ans.append(x)
            freq[x] -=1
