string="안녕하세요"
#인덱스: 01234, -5-4-3-2-1
print(string[1:4])#항상 끝보다 -1까지 출력 (인덱스)
print(string[1:-2])#인덱스 1에서 -2이전까지(-2는 포함하지 않는다.)
print(string[1:])#인덱스 1부터 끝까지: 문자열의 시작 또는 끝은 생략 가능하다.
print(string[:])
print(string[1:100])#인덱스가 지나치게 클 경우 문자열의 최대 길이만큼만 표현된다. 
print(string[-1])#요
print(string[-4])#녕
print(string[:-3])#안녕
print(string[-3:])#-3부터 끝까지.
print(string[::1])#1은 기본값으로 동일.
print(string[::-1])#뒤집기
print(string[::2])#2칸씩 앞으로 이동 // 안하요

