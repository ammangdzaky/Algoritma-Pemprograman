## GANJIL GENAP

n = int(input(f"Masukkan nilai n untuk melihat angka ganjil dan\ngenap  dari 0-n : "))

ganjil = []
genap = []

for i in range(0,n+1):
    
    if i % 2 == 1:
        ganjil.append(i)
    else:
        genap.append(i)
        
print(f"ganjil = {ganjil}")
print(f"genap = {genap}")


        

