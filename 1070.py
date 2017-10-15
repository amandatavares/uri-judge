X = int(input(""))

if (X%2==0):
    impar = X + 1
    for i in range(6):
        print(impar + i*2)
else:
    for i in range(6):
        print(X + i*2)
