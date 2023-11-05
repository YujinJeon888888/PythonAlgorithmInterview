from collections import deque
import sys
myDeque=deque()
myDeque=sys.stdin.readline()
for i in range(len(myDeque)):
    if i+1 != len(myDeque):#ÀÎµ¦½º ¹üÀ§ ¾È ³Ñ¾î°¡°Ô
        if myDeque[i]==myDeque[i+1]:#¿·¿¡²¨¶û ºñ±³. 
            myDeque.popleft()
        elif myDeque[i]==myDeque[len(myDeque)]:

            