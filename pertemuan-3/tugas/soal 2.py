## SOAL 2
## Menentukan suatu bilangan prima atau tidak

n = int(input("masukkan bilangan : "))

if n <= 1 :
    prima = False
elif n == 2 :
    prima = True
else:
    prima = True


for i in range(2,n):
    if n % i == 0:
        prima = False
        break
    else:
        prima = True

print(f"{n} = {prima} prima")
    




