# ù ��° �� �Է�
num1 = int(input())

# �� ��° �� �Է�
num2 = int(input())

# �� ���� �����Ͽ� ����� ���
result = num1 * num2

# �� �ڸ������� ���� ����� ���
print(num1 * (num2 % 10))    # ���� �ڸ�
print(num1 * ((num2 // 10) % 10))  # ���� �ڸ�
print(num1 * (num2 // 100))   # ���� �ڸ�

# ��ü ��� ���
print(result)
