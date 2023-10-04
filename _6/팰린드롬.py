import collections
from ctypes.wintypes import BOOL, VARIANT_BOOL
from curses.ascii import isalnum
from typing import Deque

def isPalindrom(self,s:str)->bool:
    strs=[]
    for char in s:
        if char.isalnum():#영문자, 숫자여부를 판별하는 함수
            strs.append(char.lower())#해당하는 문자만 추가

    while len(strs)>1:
        if strs.pop(0)!=strs.pop():#pop 기본: 맨 끝 팝. 인덱스 지정 가능.
            return False

#더 빠른 ver (데크Deque 사용)
def isPalindrom2(self,s:str)->bool:# 파이썬 클래스 메서드 내에서 self를 사용하는 것은 해당 클래스의 인스턴스 속성 및 메서드에 액세스하기 위한 것입니다.
    #자료형 데크로 선언
    strs: Deque=collections.Deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.popleft()!=strs.pop():#리스트의 pop()는 O(n), 데크의 popleft()는 O(1)
            return False

    return True

#데크: O(n), 리스트: O(n^2)

#슬라이싱 사용
def isPalindrom3(self,s:str)->bool:
    s=s.lower()
    #정규식으로 불필요한 문자 필터링
    s=re.sub('[^a-z0-9]','',s)#문자열 전체를 한 번에 영숫자만 걸러내도록 정규식으로 처리.

    return s==s[::-1] #뒤집기해도 같은지 확인
#2번보다 2배 속도 높임.

