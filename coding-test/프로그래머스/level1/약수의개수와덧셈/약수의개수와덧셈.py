def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        numbers = 0
        for n in range(1, i + 1):
            if (i % n == 0):
                numbers += 1
        if numbers % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
# 내 풀이


# 다른사람 풀이
# import math

# def solution(left, right):
#     answer = 0
#     for i in range(left, right + 1, 1):
#         sqrt = math.sqrt(i)
#         if int(sqrt) == sqrt:
#             answer -= i
#         else:
#             answer += i

#     return answer

# 제곱근으로 사용 가능