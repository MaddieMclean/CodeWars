def solution(args):
    ans = ""
    idx = 0
    length = len(args)
    
    while idx < length:
        val = args[idx]
        j = (idx + 1) % length        
        x = 1
        while args[j] == val + x:
            x += 1
            j = (j + 1) % length
        ans += str(val)
        if (x == 2):
            ans += "," + str(args[idx + x - 1])
        elif (x > 2):                  
            ans += "-" + str(args[idx + x - 1])
        ans += ","
        idx += x

    return ans[:len(ans) - 1]