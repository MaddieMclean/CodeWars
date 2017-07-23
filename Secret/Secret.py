def populate(triplets):
    master = ""
    
    for trip in triplets:
        for char in trip:
            if (char not in master):
                master += char
                
    return master

def recoverSecret(triplets):
    finished = False
    
    master = populate(triplets)    
    
    while not finished:    
        finished = True
        
        for trip in triplets:            
            x = master.find(trip[0])
            y = master.find(trip[1])
            z = master.find(trip[2])
            
            if (x > y):
                finished = False
                master = master.replace(trip[0], "", 1)
                master = master[:y] + trip[0] + master[y:]
                
            if (y > z):
                finished = False
                master = master.replace(trip[1], "", 1)
                master = master[:z] + trip[1] + master[z:]

    return master
