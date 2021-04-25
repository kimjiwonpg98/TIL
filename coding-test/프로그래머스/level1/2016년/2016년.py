def solution(a, b):
    result = 0;
    weeks = ["FRI","SAT","SUN","MON","TUE","WED","THU"];
    dates = [31,29,31,30,31,30,31,31,30,31,30,31];
    
    for month in range(0, a):
        for day in range(1, dates[month] + 1):
            result += 1
            if result == 7:
                result = 0
            if month == a - 1 and day == b: 
                return weeks[result - 1]