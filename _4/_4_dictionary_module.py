from collections import defaultdict
from collections import Counter
import collections

fruit_count=defaultdict(int)#int 타입의 기본값 가지는 defaultdict생성

#딕셔너리에 값 추가
fruit_count['apple']+=1
fruit_count['banana']+=2
fruit_count['cherry']+=3

print(fruit_count['apple'])   # 출력: 1
print(fruit_count['banana'])  # 출력: 2
print(fruit_count['cherry'])  # 출력: 3
print(fruit_count['grape'])   # 출력: 0 (기본값이 0이므로)


#counter
print("counter  ↓")
a = [1,2,3,4,5,5,5,6,6]

b = collections.Counter(a)
print(b)
### result Counter({5:3, 6:2, 1:1, 2:1, 3:1, 4:1})

##### 가장 빈도가 높은 것은?
b.most_common(1)
[(5,3)]