# �似Ǫ�� ������ �ذ��ϴ� �Լ�
def josephus(n, k):
    # 1���� n������ ���ڸ� �����ϴ� ����Ʈ ����
    people = list(range(1, n + 1))
    # ����� ������ ����Ʈ �ʱ�ȭ
    result = []
    # ���� ��ġ�� ��Ÿ���� �ε��� �ʱ�ȭ
    index = 0

    # ����Ʈ�� �� ������ �ݺ�
    while people:
        # �������� ���ŵ� ����� �ε��� ���
        index = (index + k - 1) % len(people)
        # �ش� �ε����� ����� ����Ʈ���� �����ϰ� ��� ����Ʈ�� �߰�
        removed = people.pop(index)
        result.append(str(removed))

    # �似Ǫ�� ������ ���ڿ��� ��ȯ
    return "<" + ", ".join(result) + ">"

if __name__ == "__main__":
    # ����ڷκ��� n�� k�� �Է¹���
    n, k = map(int, input().split())
    # josephus �Լ��� ȣ���Ͽ� �似Ǫ�� ���� ���
    answer = josephus(n, k)
    # ��� ���
    print(answer)
