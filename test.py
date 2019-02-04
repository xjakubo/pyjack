from random import randint

def ace(tablica, reduce):
    if reduce:
    	x = 0
    	for element in tablica:
    		if element == 11:
    			tablica[x] = 1
    			print(element)
    			break
    		x += 1
    for element in tablica:
        if element == 11:
            return True
    return False

def Random(): 
	return randint(10,11)

gracz = [Random(), Random()]
krupier = [Random(), Random()]

print(gracz)

if ace(gracz,0) and sum(gracz) > 21:
	ace(gracz, 1)
	print(gracz)