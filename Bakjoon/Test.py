#단비
#*런타임 에러가 뜹니다..! ㅠ.ㅠ
n = int(input())
num = n
cnt = 0

while (True):
     a = num // 10
     b = num % 10
     c = (a+b) % 10#새로운 수의 일의자리
     d = (b*10)+c#새로운 수
     
     cnt = cnt+1
     num=d
     if (d == n):#새로운 수가 들어온 수랑 같으면 멈추기
         break

print(cnt)