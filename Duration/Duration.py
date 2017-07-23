mods = [365,24,60,60,1]
units = [" year", " day", " hour", " minute", " second"]
ans = []
    

def setup_times():
    length = len(mods) -1
    
    for i in range(length, -1, -1):
    
        if(i != length):
            mods[i] = mods[i] * mods[i + 1]


def populate_ans(seconds):
    for idx, i in enumerate(mods):
    
        if (seconds >= i):
            value = seconds / i
            seconds = seconds % i
            
            if(value > 1):
                units[idx] = units[idx] + "s"
                
            value = str(value) + units[idx]
            ans.append(value)
            
def format_ans():
    andPoint = len(ans) - 2
    output = ""
    
    for idx, i in enumerate(ans):
        output = output + i
        
        if(idx == len(ans) - 1):
            break
        
        if(idx == andPoint):
            output = output + " and " + ans[idx + 1]
            break
        
        output = output + ", "
    
    return output

def format_duration(seconds):
    mods[:] = [365,24,60,60,1]
    units[:] = [" year", " day", " hour", " minute", " second"]
    ans[:] = []   
        
    if (seconds == 0):
        return "now"
    
    setup_times()
    populate_ans(seconds)
    output = format_ans()
    return output

          
        
            

        
            
            
            