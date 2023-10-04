# 요세푸스 문제를 해결하는 함수
def josephus(n, k):
    # 1부터 n까지의 숫자를 포함하는 리스트 생성
    people = list(range(1, n + 1))
    # 결과를 저장할 리스트 초기화
    result = []
    # 시작 위치를 나타내는 인덱스 초기화
    index = 0

    # 리스트가 빌 때까지 반복
    while people:
        # 다음으로 제거될 사람의 인덱스 계산
        index = (index + k - 1) % len(people)
        # 해당 인덱스의 사람을 리스트에서 제거하고 결과 리스트에 추가
        removed = people.pop(index)
        result.append(str(removed))

    # 요세푸스 순열을 문자열로 반환
    return "<" + ", ".join(result) + ">"

if __name__ == "__main__":
    # 사용자로부터 n과 k를 입력받음
    n, k = map(int, input().split())
    # josephus 함수를 호출하여 요세푸스 순열 계산
    answer = josephus(n, k)
    # 결과 출력
    print(answer)
