import statistics
n = input()
array = list(map(int, input().split()))
array.sort()
print(statistics.median(array))