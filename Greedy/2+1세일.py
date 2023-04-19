# 2+1 세일

N = int(input())
arr = []
free = []
for _ in range(N):
	arr.append(int(input()))

arr.sort(reverse=True)

for i in range(len(arr)):
	if i%3 == 2:
		free.append(arr[i])

print(sum(arr) - sum(free))