from curses.ascii import isdigit

def reorderLogFiles(self,logs:list[str])->list[str]:
    letters,digits=[],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    #2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))
    return letters+digits

#람다 표현식: 식별자 없이 실행 가능한 함수. 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현할 수 있다.
#람다 표현식은 코드가 길어지고 map이나 filter와 함께 섞어서 사용하기 시작하면 가독성이 매우 떨어질 수 있으므로 주의가 필요하다.
