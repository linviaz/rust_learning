# coding=utf-8

instreak = input()

instreak_ls = instreak.split()

current_streak = 0
longest = 0

for item in instreak_ls:
    if item == 'Y':
        current_streak += 1
        if longest<current_streak:
            longest = current_streak
    elif item == 'N':
        current_streak = 0

print('longest streak: ', longest)
