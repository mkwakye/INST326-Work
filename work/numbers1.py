x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def is_divisible(num):
    if num % 5 == 0 or num % 3 == 0:
        return True
    else:
        return num

y = []

for num in x:
    y.append(is_divisible(num))

print(y)