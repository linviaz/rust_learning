instreat = input()

instreak_ls = instreak.split()

count_y = 0
count_n = 0

for i in list(instreak_ls):
    if i =='Y':
        count_y += 1
    elif i == 'N':
        count_x += 1
    else:
        print('exceptional case')

