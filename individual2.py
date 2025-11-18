k = input("Введите k от 1 до 180: ")

pair = (k+1) // 2
number = 9 + pair
digit = (number // 10) * ((k+1)%2) + (number%10) * (k%2)

print("Номер пары цифр:", pair)
print("Двузначное число:", number)
print("K-я цифра:", digit)