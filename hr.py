coefficients = list(map(int,input().split()))
discriminant= coefficients[1]**2 - ( 4*coefficients[0]*coefficients[2])
if discriminant >= 0 :
    x_1 = (-(coefficients[1]) + discriminant**0.5)/(2*coefficients[0])
    x_2 = (-(coefficients[1]) - discriminant**0.5)/(2*coefficients[0])

    print(x_1,x_2)

else:
    print("Решений нет")



