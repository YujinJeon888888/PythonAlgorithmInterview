from collections import deque  # 덱(deque)을 사용하기 위해 모듈을 임포트

def rotate_queue(queue, target):
    left_count = 0  # 왼쪽으로 이동한 횟수를 저장하는 변수 초기화
    right_count = 0  # 오른쪽으로 이동한 횟수를 저장하는 변수 초기화
    
    while queue[0] != target:  # 큐의 가장 앞에 있는 원소가 목표값이 아니라면 계속 반복
        queue.rotate(1)  # 큐를 오른쪽으로 한 칸 회전
        right_count += 1  # 오른쪽으로 이동한 횟수 증가
    left_count = len(queue) - right_count  # 왼쪽으로 이동한 횟수 계산
    return min(left_count, right_count)  # 왼쪽과 오른쪽 중 작은 이동 횟수를 반환

def min_operations(N, targets):
    queue = deque(range(1, N + 1))  # 큐를 1부터 N까지의 숫자로 초기화
    total_operations = 0  # 총 이동 횟수를 저장하는 변수 초기화
    
    for target in targets:  # 뽑아내야 하는 숫자들을 하나씩 처리
        total_operations += rotate_queue(queue, target)  # 해당 숫자를 뽑아내기 위한 이동 횟수를 더하기
        queue.popleft()  # 뽑아낸 숫자를 큐에서 제거
    
    return total_operations  # 총 이동 횟수를 반환

N, M = map(int, input().split())  # 큐의 크기 N과 뽑아내야 하는 숫자들의 개수 M을 입력받기
targets = list(map(int, input().split()))  # 뽑아내야 하는 숫자들을 리스트로 입력받기.
result = min_operations(N, targets)  # min_operations 함수를 호출하여 결과를 계산
print(result)  # 결과를 출력
