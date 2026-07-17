for i in range(1, 11):
    print(i)
    for i in range(1, 11):
        print(i, "->", i ** 2)
    son = int(input("Son kiriting: "))

    for i in range(1, 11):
        print(f"{son} x {i} = {son * i}")
    for i in range(2, 101, 2):
        print(i)
        for i in range(1, 101, 2):
            print(i)
            for i in range(1, 101, 2):
                print(i)
                for i in range(1, 101):
                    if i % 2 != 0:
                        print(i)
                        print(i)
                        yigindi = 0

for i in range(1, 21):
    yigindi += i

print("Yig'indi =", yigindi)
kopaytma = 1

for i in range(1, 11):
    kopaytma *= i

print("Ko'paytma =", kopaytma)
n = int(input("Nechta son kiritasiz? "))

yigindi = 0

for i in range(n):
    son = float(input("Son kiriting: "))
    yigindi += son

ortacha = yigindi / n
print("O'rtacha qiymat:", ortacha)
for i in range(10, 0, -1):
    for i in range(1, 51):
        if i % 3 == 0:
            print(i)