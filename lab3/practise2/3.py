def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        legs = chickens * 2 + rabbits * 4
        if(numlegs == legs):
            return chickens , rabbits
    return 0
chickens , rabbits = solve(35 , 94)
print(f"chickens = {chickens} , rabbits = {rabbits}")
