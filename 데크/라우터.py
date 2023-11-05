from collections import deque
import sys

my_deque = deque()
size = int(sys.stdin.readline())

while True:
    num = int(sys.stdin.readline())
    if num == -1:
        break
    if num == 0:
        my_deque.popleft()
    elif len(my_deque) < size:
        my_deque.append(num)

if len(my_deque) == 0:
    print("empty")
    exit()

while my_deque:
    print(str(my_deque.popleft()), end=" ")
