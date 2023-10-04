#num=int(input('출력할 숫자를 입력하세요: '))
#i=0
#while i<num:
#    i+=1
#    print(' ',num)

#정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.1
#num=int(input('정수를 입력하세요: '))
#i=1
#while i<=num:
#    print(i,' ', i*i)
#    i+=1

#고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.
height=100
i=0
while i<10:
    i+=1
    print(round(height*3/5,4))#소숫점 넷째자리로 반올림
    height=round(height*3/5,4)
