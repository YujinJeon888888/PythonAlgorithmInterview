from collections import deque
import sys
myDeque=deque()
myDeque=sys.stdin.readline()
for i in range(len(myDeque)):
    if i+1 != len(myDeque):#�ε��� ���� �� �Ѿ��
        if myDeque[i]==myDeque[i+1]:#�������� ��. 
            myDeque.popleft()
        elif myDeque[i]==myDeque[len(myDeque)]:

            