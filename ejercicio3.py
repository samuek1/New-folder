def hanoi (n , origen , dest, aux):
    if n== 1: 
        print (f"Mover el disco {n} de {origen} al {dest}")
        return 
    
    hanoi (n-1, origen, aux, dest)
    print (f"Mover el disco {n} de {origen} al {dest}")
    hanoi (n-1, dest, aux, dest, origen) 
    hanoi (n-1, dest, aux, dest) 
    