import sys

count = 0
while True:
    first_str = sys.stdin.readline().strip()  # 입력 받은 문자열의 앞뒤 공백 및 개행문자 제거
    last_str = sys.stdin.readline().strip()

    if last_str == "END" and first_str == "END":
        break  # "END"가 입력되면 루프 종료

    count += 1
    isCollected = False

    if len(first_str) == len(last_str):
        sorted_first = sorted(first_str)
        sorted_last = sorted(last_str)

        if sorted_first == sorted_last:
            isCollected = True

    if isCollected:
        print(f'Case {count}: same')
    else:
        print(f'Case {count}: different')
