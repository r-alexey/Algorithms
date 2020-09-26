# ------------------------------ WAY 1 ------------------------------ #
from random import random 

def choice_road(left, right):
	if random() * (left + right) < left :
		return 'left'
	else:
		return 'right'

max_summ=0
triangle = [
[75]
,[95, 64]
,[17, 47, 82]
,[18, 35, 87, 10]
,[20, 4, 82, 47, 65]
,[19, 1, 23, 75, 3, 34]
,[88, 2, 77, 73, 7, 63, 67]
,[99, 65, 4, 28, 6, 16, 70, 92]
,[41, 41, 26, 56, 83, 40, 80, 70, 33]
,[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
,[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
,[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
,[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
,[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
,[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

for iteration in range(500):

	iteration_summ = triangle[0][0]
	j=0
	
	for i in range(1, len(triangle)):
		if choice_road(triangle[i][j], triangle[i][j+1]) == 'right':
			j += 1
		iteration_summ += triangle[i][j]
	
	if iteration_summ > max_summ:
		max_summ = iteration_summ

print (max_summ)


# ------------------------------ WAY 2 ------------------------------ #
trg = [
[75]
,[95, 64]
,[17, 47, 82]
,[18, 35, 87, 10]
,[20, 4, 82, 47, 65]
,[19, 1, 23, 75, 3, 34]
,[88, 2, 77, 73, 7, 63, 67]
,[99, 65, 4, 28, 6, 16, 70, 92]
,[41, 41, 26, 56, 83, 40, 80, 70, 33]
,[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
,[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
,[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
,[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
,[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
,[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

for i in range(1, 15):
    for j in range(i+1):
    
        try:
        
            if trg[i-1][j-1] > trg[i-1][j]:
                trg[i][j] += trg[i-1][j-1]
            else:
                trg[i][j] += trg[i-1][j] 
                
        except LookupError:  
        
            try:
                trg[i][j] += trg[i-1][j-1]
            except LookupError:
                trg[i][j] += trg[i-1][j]


print (max(trg[14]))
