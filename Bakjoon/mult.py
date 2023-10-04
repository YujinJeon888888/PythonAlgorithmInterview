# 첫 번째 수 입력
num1 = int(input())

# 두 번째 수 입력
num2 = int(input())

# 두 수를 곱셈하여 결과를 계산
result = num1 * num2

# 각 자리수별로 곱셈 결과를 출력
print(num1 * (num2 % 10))    # 일의 자리
print(num1 * ((num2 // 10) % 10))  # 십의 자리
print(num1 * (num2 // 100))   # 백의 자리

# 전체 결과 출력
print(result)
