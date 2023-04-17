import sys

sys.stdin = open('input.txt')

N = int(input())
arr = []
answer = []
for _ in range(N):
    rope = int(input())
    arr.append(rope)
    
arr.sort(reverse=True)

for i in range(len(arr)):
    answer.append((i+1)*arr[i])

print(max(answer))
