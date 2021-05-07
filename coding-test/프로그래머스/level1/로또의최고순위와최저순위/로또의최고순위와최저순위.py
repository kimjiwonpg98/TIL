def solution(lottos, win_nums):
    
    rank = [6,6,5,4,3,2,1]
    count = 0
    zero_count = 0
    
    for num in lottos:
        if num == 0:
            zero_count += 1
            continue
            
        for win_num in win_nums:
            if num == win_num:
                count += 1
    
    high_score = rank[zero_count + count]
    low_score = rank[count]
    
    return [high_score, low_score]