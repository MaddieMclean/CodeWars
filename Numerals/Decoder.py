def solution(roman):
    i = 0
    j = 0
    ans = 0
    numerals = [
                ["CM", 900],
                ["M", 1000],
                ["CD", 400],
                ["D", 500],
                ["XC", 90],
                ["C", 100],
                ["XL", 40],
                ["L", 50],
                ["IX", 9],
                ["X", 10],
                ["IV", 4],
                ["V", 5],
                ["I", 1],                
                ]
    
    for key, value in numerals:
        while key in roman:
            ans += value
            roman = roman.replace(key, "", 1)
        
    return ans   