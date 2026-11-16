# Category: binary search, brute forceg, reedy, implementation, *1000
# Constraints: 1.5 seconds, 256 mb
# First instinct: First try to identify the guy who's going to finish up first
# Then find out how to get it done quickly
# 

t = int(input())

for _ in range(t):
    n,q = map(int, input())
    machines = list(map(int, input().split()))
    queries = list(map(int, input().split()))

