from itertools import permutations

def solution(k, dungeons):
    max_count = 0 

    for order in permutations(dungeons):
        current_k = k  
        count = 0      
        

        for dungeon in order:
            min_required, fatigue = dungeon
            if current_k >= min_required:  
                current_k -= fatigue      
                count += 1                
            else:
                break  


        max_count = max(max_count, count)

    return max_count

