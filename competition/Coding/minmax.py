# take in the number
n = input()
list_number = n.split(' ')

min_nb = None
max_nb = None
# calculate answer
for nb in list_number:
    number = float(nb)
    if min_nb is None:
        min_nb = number
        max_nb = number
    else:
        if min_nb > number:
            min_nb = number
        elif max_nb < number :
            max_nb = number
answer = str(min_nb)+"\n"+str(max_nb)
# print answer
print(answer)