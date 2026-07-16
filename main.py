for i in range(1,11):
    print(i)
for i in range(1,11):
    print(f"{i} ning kvadrati: {i**2}")
    son = int(input("Son kiriting: "))
    for i in range(1, 11):
        print(f"{son} x {i} = {son * i}")
        for i in range(2, 101, 2):
            print(i)
            for i in range(1, 100, 2):
                print(i)
                yigindi =0
for i in range(1, 21):
    yigindi += i
print("Yig'indi:", yigindi)
kopaytma = 1
for i in range(1, 11):
    kopaytma *= i
print("Ko'paytma:", kopaytma)
n = int(input("Nechta son kiritasiz? "))