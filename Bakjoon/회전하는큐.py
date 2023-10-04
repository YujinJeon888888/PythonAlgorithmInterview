from collections import deque  # ��(deque)�� ����ϱ� ���� ����� ����Ʈ

def rotate_queue(queue, target):
    left_count = 0  # �������� �̵��� Ƚ���� �����ϴ� ���� �ʱ�ȭ
    right_count = 0  # ���������� �̵��� Ƚ���� �����ϴ� ���� �ʱ�ȭ
    
    while queue[0] != target:  # ť�� ���� �տ� �ִ� ���Ұ� ��ǥ���� �ƴ϶�� ��� �ݺ�
        queue.rotate(1)  # ť�� ���������� �� ĭ ȸ��
        right_count += 1  # ���������� �̵��� Ƚ�� ����
    left_count = len(queue) - right_count  # �������� �̵��� Ƚ�� ���
    return min(left_count, right_count)  # ���ʰ� ������ �� ���� �̵� Ƚ���� ��ȯ

def min_operations(N, targets):
    queue = deque(range(1, N + 1))  # ť�� 1���� N������ ���ڷ� �ʱ�ȭ
    total_operations = 0  # �� �̵� Ƚ���� �����ϴ� ���� �ʱ�ȭ
    
    for target in targets:  # �̾Ƴ��� �ϴ� ���ڵ��� �ϳ��� ó��
        total_operations += rotate_queue(queue, target)  # �ش� ���ڸ� �̾Ƴ��� ���� �̵� Ƚ���� ���ϱ�
        queue.popleft()  # �̾Ƴ� ���ڸ� ť���� ����
    
    return total_operations  # �� �̵� Ƚ���� ��ȯ

N, M = map(int, input().split())  # ť�� ũ�� N�� �̾Ƴ��� �ϴ� ���ڵ��� ���� M�� �Է¹ޱ�
targets = list(map(int, input().split()))  # �̾Ƴ��� �ϴ� ���ڵ��� ����Ʈ�� �Է¹ޱ�.
result = min_operations(N, targets)  # min_operations �Լ��� ȣ���Ͽ� ����� ���
print(result)  # ����� ���
