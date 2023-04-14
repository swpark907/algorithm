N, M = map(int, input().split())
j = int(input())
count = 0
left = 1
right = M
for _ in range(j):
    position = int(input())
    if left <= position and position <= right:
        continue
    elif right < position:
        count += position-right
        left += position - right
        right += position - right
    else:
        count += left-position
        left -= left-position
        right -= left - position

print(count)