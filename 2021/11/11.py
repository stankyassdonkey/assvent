file = open('11.txt', 'r')
input = file.read()
lines = input.split("\n")

energy_level = ([[eval(i) for i in energy] for energy in [[*energy]for energy in lines]])

def print_map(map):
    for i in range(len(map)):
        print(list_to_string(map[i]))

def list_to_string(rows):
    output = ""
    for symbols in (rows) :
        output += str(symbols)+" "
    return (output)

def next_step(energy_levels):
    new_energy_level = [[n+1 for n in rows] for rows in energy_levels]
    return new_energy_level

def check_flash(map):
    flash_list = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] >= 10:
                flash_list.append([i,j])
    return flash_list

def neighbours(coords,flash_list):
    y,x = coords[0] , coords[1]
    return (["None" if (y-1+j) < 0 or (y-1+j) > len(energy_level)-1 or (x-1+i) < 0 or (x-1+i) > len(energy_level[0])-1 or (y-1+j==y and x-1+i==x) or ([y-1+j,x-1+i] in flash_list )  else [(y-1+j),(x-1+i)] for j in range(3) for i in range(3)])

flash_count = [0]
last_flash = []

def flash(last_flash_list, flash_list,map):
    if len(flash_list) != 0 :
        for flashies in flash_list:
            flash_count[0] += 1
            map[flashies[0]][flashies[1]] = 0
            for coords in neighbours(flashies, flash_list) :
                if coords != "None" and coords not in last_flash_list:
                    y,x = coords[0] , coords[1]
                    map[y][x] += 1
                    last_flash.extend([flashies]) if flashies not in last_flash else None
        flash(last_flash ,check_flash(map),map)
    last_flash.clear()
    return map
            
old_map = energy_level

def flash_go_brrrr(steps):
    global old_map
    sync = 0
    for i in range(steps) :
        old_flash_list = []
        next_map = next_step(old_map)
        flash_list = check_flash(next_map)
        new_map = (flash(old_flash_list,flash_list,next_map))
        old_map = new_map
        if check_sync(new_map):
            print(f"Sync at:{i}")
            break

    print_map(new_map)
    print(f"Flashes:{flash_count[0]}")
    
def check_sync(map):
    count = 0 
    count += sum(1 for i in range(len(energy_level[0])) for j in range(len(energy_level)) if map[j][i] == 0)
    return True if count == (len(energy_level)*len(energy_level[0])) else False

flash_go_brrrr(265)

