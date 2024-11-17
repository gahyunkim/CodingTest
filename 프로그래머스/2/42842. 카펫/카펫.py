def solution(brown, yellow):
    for h in range(1, int(yellow**0.5) + 1):  
        if yellow % h == 0: 
            w = yellow // h 
            total_width = w + 2
            total_height = h + 2
            
            if total_width * total_height - yellow == brown:
                return [total_width, total_height]