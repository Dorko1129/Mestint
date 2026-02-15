szam = int(input("Adj meg egy egész számot: "))

print("Az osztók:")
for i in range(1, szam + 1):
    if szam % i == 0:
        print(i)
