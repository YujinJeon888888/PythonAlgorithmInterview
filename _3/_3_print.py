print('a1', 'b2')
#가장 쉽게 출력하는 ','구분 방법이다. 이 경우 한 칸 공백이 디폴트로 설정되어 있으며, 띄어쓰기로 값을 구분해준다.
print('a1','b2', sep=',')
#sep 파라미터로 구분자를 ','로 지정해줄 수도 있다.
print('aa',end=' ')
print('bb')
#print함수는 항상 줄바꿈을 함-> 긴 루프의 값을 반복족으로 출력하면 디버깅이 어려움
#end파라미터를 공백처리해서 줄바꿈을 대체해서 처리 가능
a=['A','B','C']
print('__'.join(a))
#리스트를 출력할 때는 join()으로 묶어서 처리한다.
idx=1
fruit="Apple"

print('{0}: {1}'.format(idx+1,fruit))
print('{}: {}'.format(idx+1,fruit))#이렇게 인덱스 생략도 가능

##########
print(f'{idx+1}: {fruit}')
#f-string방법