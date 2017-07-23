def check_dir(field, y, x, ship):
    field[y][x] = 2
    
    if((x + 1 < 10) and (y + 1 < 10)):
    
        if ((x > 1) and (field[y + 1][x - 1] == 1)) or (field[y + 1][x + 1] == 1):
            return -1
    
        if (field[y][x + 1] == 1):
            x += 1            
        elif (field[y + 1][x] == 1):
            y += 1           
        else:
            return ship
    
    ship += 1
    ship = check_dir(field, y, x, ship)
    return ship

def validateBattlefield(field):
    remaining_ships = [4,3,3,2,2,2,1,1,1,1]
    
    ship_sum = 0
    i = 0
    
    for y in field:
        ship_sum += y.count(1)
    
    if ship_sum != 20:
            return False
        
    while i < 10:        
        if (1 in field[i]):
            start = field[i].index(1)
            
            ship = 1
            ship = check_dir(field, i, start, ship)        
            
            if ship in remaining_ships:
                remaining_ships.remove(ship)
            else:
                return False

        else:
            i += 1   
            
    return True