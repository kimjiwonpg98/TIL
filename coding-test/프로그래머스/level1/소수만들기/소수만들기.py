from itertools import combinations

def sort(fir, sec, thr):
    total = fir + sec + thr
    
    for i in range(2, total):
        if total % i == 0: return False
    return True
        


def solution(nums):
    answer = 0
    
    numbers = list(combinations(nums, 3))

    for num in numbers:
        if sort(num[0], num[1], num[2]):
            answer += 1
    return answer