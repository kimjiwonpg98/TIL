def solution(word):
    pp = 0
    yy = 0
    upper_word = word.upper();  
    
    word_list = list(upper_word)
    
    for i in word_list:
        if i == "P": pp += 1
        if i == "Y": yy += 1
            
    return pp == yy