def nb_year(p0, percent, aug, p):
    pop = p0
    percent = percent / 100
    n = 0
    while pop < p:  
        pop = int( pop + (pop * percent) + aug)
        n += 1
    return n 
