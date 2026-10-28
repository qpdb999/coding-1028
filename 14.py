'''
# 파이썬 예외 처리

    오늘 배운 내용

예외 처리는 프로그램 실행 중 발생하는 오류에 대응하여
프로그램이 갑자기 종료되는 것을 방지하고,
오류 상황에 맞는 처리를 할 수 있도록 하는 기능이다.

예를 들어 숫자를 입력해야 하는 프로그램에서
사용자가 문자를 입력하면 오류가 발생할 수 있다.
이때 예외 처리를 사용하면 오류 안내를 출력하고
프로그램을 계속 실행할 수 있도록 만들 수 있다.



    예외 처리의 정의

1) 예외(Exception)
프로그램 실행 중 발생하여 정상적인 실행을 방해하는 오류 상황이다.

2) try
예외가 발생할 수 있는 코드를 작성하는 부분이다.

3) except
try 안에서 예외가 발생했을 때 실행할 코드를 작성하는 부분이다.

4) else
try 안에서 예외가 발생하지 않았을 때 실행하는 부분이다.

5) finally
예외 발생 여부와 관계없이 마지막에 실행하는 부분이다.

6) ValueError
숫자로 변환할 수 없는 문자열을 int()나 float()로 변환하려 할 때
발생할 수 있는 예외이다.

7) ZeroDivisionError
숫자를 0으로 나누려고 할 때 발생하는 예외이다.


    기본적인 예외 처리

try:
    num = int(input("숫자를 입력하세요: "))
    print("입력한 숫자:", num)

except ValueError:
    print("오류: 숫자만 입력해야 합니다.")



    try-except-else-finally 사용하기


try:
    num = int(input("정수를 입력하세요: "))

except ValueError:
    print("정수가 아닌 값을 입력했습니다.")

else:
    print("입력에 성공했습니다.")
    print("입력한 값:", num)

finally:
    print("입력 작업이 끝났습니다.")



    0으로 나누는 오류 처리하기


try:
    num1 = int(input("첫 번째 숫자: "))
    num2 = int(input("두 번째 숫자: "))

    result = num1 / num2
    print("나눗셈 결과:", result)

except ValueError:
    print("오류: 숫자로 입력해야 합니다.")

except ZeroDivisionError:
    print("오류: 0으로 나눌 수 없습니다.")



    예외 처리를 활용한 계산기


try:
    num1 = float(input("첫 번째 숫자: "))
    operator = input("연산자 입력 (+, -, *, /): ")
    num2 = float(input("두 번째 숫자: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("지원하지 않는 연산자입니다.")
        result = None

    if result is not None:
        print("계산 결과:", result)

except ValueError:
    print("오류: 숫자를 올바르게 입력하세요.")

except ZeroDivisionError:
    print("오류: 0으로 나눌 수 없습니다.")

finally:
    print("계산기 실행이 끝났습니다.")



    코드 분석


try:
오류가 발생할 수 있는 코드를 작성한다.

except ValueError:
숫자 변환 등에 실패했을 때 실행한다.

except ZeroDivisionError:
0으로 나누려고 했을 때 실행한다.

else:
try 안에서 예외가 발생하지 않았을 때만 실행한다.

finally:
예외 발생 여부와 관계없이 실행된다.

result = None
아직 계산 결과가 없다는 의미로 None을 저장한다.

if result is not None:
result에 계산 결과가 있는지 확인한다.
지원하지 않는 연산자를 입력했을 때
잘못된 결과가 출력되는 것을 방지한다.


# ========================================
# 📌 9. AI 활용 복습 문제
# ========================================
#
# 1) 오류가 발생할 가능성이 있는 코드를 작성하는 부분은?
# 1. if   2. try   3. else   4. finally
# 정답: 2번 (try)
#
# 2) try 안에서 예외가 발생했을 때 실행되는 부분은?
# 1. except   2. else   3. for   4. return
# 정답: 1번 (except)
#
# 3) int("hello")를 실행하면 발생할 수 있는 예외는?
# 1. TypeError   2. ValueError
# 3. ZeroDivisionError   4. IndexError
# 정답: 2번 (ValueError)
#
# 4) 10 / 0을 실행하면 발생하는 예외는?
# 1. ValueError   2. NameError
# 3. ZeroDivisionError   4. IndexError
# 정답: 3번 (ZeroDivisionError)
#
# 5) try 안에서 예외가 발생하지 않았을 때 실행되는 부분은?
# 1. except   2. else   3. break   4. pass
# 정답: 2번 (else)
#
# 6) 예외 발생 여부와 관계없이 마지막에 실행되는 부분은?
# 1. try   2. except   3. else   4. finally
# 정답: 4번 (finally)
#
# 7) 예외 처리를 사용하는 주된 이유는?
# 1. 모든 오류를 없애기 위해
# 2. 변수의 개수를 줄이기 위해
# 3. 오류 상황에 대응하기 위해
# 4. 반복문을 만들기 위해
# 정답: 3번 (오류 상황에 대응하기 위해)
#
# 8) 계산기에서 0으로 나누는 오류를 처리하려면?
# 1. except ValueError
# 2. except ZeroDivisionError
# 3. else ValueError
# 4. finally ZeroDivisionError
# 정답: 2번 (except ZeroDivisionError)
'''