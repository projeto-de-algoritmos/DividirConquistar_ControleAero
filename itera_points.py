from distancia_pontos import Point

def itera_Points(initial, final):
    if initial == final:
        return initial
    
    for i in range(len(initial)):
        if initial[i].x < final[i].x:
            initial[i].x += 1
        elif initial[i].x > final[i].x:
            initial[i].x -= 1
        
        if initial[i].y < final[i].y:
            initial[i].y += 1
        elif initial[i].y > final[i].y:
            initial[i].y -= 1
    
    for i in range(len(initial)-1, -1, -1):
        if initial[i].x == final[i].x and initial[i].y == final[i].y:
            del initial[i]
    
    return initial
