from collections import deque
import sys
totalNum=int(sys.stdin.readline())
myDeque=deque()

for i in range(totalNum):#i는 0부터 시작하므로 +1을 해 주어 1부터 카드가 쌓이도록 한다.
    myDeque.append(1+i)

while myDeque:
    print(myDeque.popleft(),end=" ")
    if myDeque:
        myDeque.append(myDeque.popleft())