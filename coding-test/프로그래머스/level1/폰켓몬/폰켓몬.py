def solution(nums):
    
    take_len = len(nums) // 2
    pocketmon = set(nums)
    pocketmon_list = list(pocketmon)
    
    if take_len < len(pocketmon_list):
        return take_len
    else:
        return len(pocketmon_list)