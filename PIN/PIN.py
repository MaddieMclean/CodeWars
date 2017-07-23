import itertools

def get_pins(observed):
    dict = {"0":["0", "8"], "1":["1","2","4"], "2":["1","2","3","5"], "3":["2","3","6"], "4":["1","4","5","7"], "5":["2","4","5","6","8"], "6":["3","5","6","9"], "7":["4","7","8"], "8":["0","5","7","8","9"], "9":["6","8","9"]}
    combos = []
    ans = []
    str = ""
    
    for i in observed:
        combos.append(dict[i])
    
    combos = list(itertools.product(*combos))

    for set in combos:
        str = ""
        
        for i in set:
            str += i
            
        ans.append(str)
    
    return ans