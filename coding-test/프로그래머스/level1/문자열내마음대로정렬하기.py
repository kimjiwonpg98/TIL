def solution(strings, n):
    new_strings = sorted(sorted(strings), key = lambda x : x[n])
    
    return new_strings