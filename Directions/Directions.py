def opposite(dir):
    
    if(dir == "NORTH"):
        return "SOUTH"
    if(dir == "SOUTH"):
        return "NORTH"
    if(dir == "EAST"):
        return "WEST"
    if(dir == "WEST"):
        return "EAST"
    
    return ""
                

def dirReduc(arr):
    
    ans = []
    i = 0

    while i < len(arr) - 1:

        if(arr[i + 1] == opposite(arr[i])):
            del arr[i + 1]
            del arr[i]
            i = 0
        else:
            i += 1
        
    
    return arr