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
yigindi = 0

for i in range(n):
    son = float(input(f"{i+1}-sonni kiriting: "))
    yigindi += son

orta_qiymat = yigindi / n
print("O'rtacha qiymat:", orta_qiymat)
for i in range(10, 0, -1):
    print(i)
    for i in range(10, 0, -1):
        print(i)
        kvadratlar = []
        for i in range(1, 21):
            kvadratlar.append(i ** 2)
        print("Kvadratlar ro'yxati:", kvadratlar)
        for i in range(1, 11):
            print(i * 2)
            soz = input("So'z kiriting: ")
            for harf in soz:
                print(harf)
                for i in range(1, 11):
                    print(f"{i} ning kubi: {i ** 3}")
                    for i in range(5, 101, 5):
                        print(i)
                        kvadratlar_yigindisi = 0
                        for i in range(1, 11):
                            kvadratlar_yigindisi += i ** 2
                        print("Kvadratlar yig'indisi:", kvadratlar_yigindisi)
                        n = int(input("n ni kiriting: "))
juft_sonlar = []
for i in range(2, n + 1, 2):
    juft_sonlar.append(i)
print("Juft sonlar ro'yxati:", juft_sonlar)
ismlar = []
for i in range(5):
    ism = input(f"{i+1}-ismni kiriting: ")
    ismlar.append(ism)

print("\nKiritilgan ismlar:")
for ism in ismlar:
    print(ism)
    import random

    tasodifiy_sonlar = []
    for _ in range(10):
        # 1 dan 100 gacha bo'lgan tasodifiy son qo'shadi
        tasodifiy_sonlar.append(random.randint(1, 100))

    print("Yaratilgan sonlar:", tasodifiy_sonlar)

    # Maksimal qiymatni topish
    max_qiymat = tasodifiy_sonlar[0]
    for son in tasodifiy_sonlar:
        if son > max_qiymat:
            max_qiymat = son

    print("Maksimal qiymat:", max_qiymat)
    karrali_7 = []
    for i in range(7, 51, 7):
        karrali_7.append(i)
    print("7 ga karrali sonlar:", karrali_7)