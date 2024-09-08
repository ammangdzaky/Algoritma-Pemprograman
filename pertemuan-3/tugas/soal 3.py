



n = int(input("Masukkan bilangan : "))

prima =[]

for i in range(2,n+1):

    for no in range(2,i):
        if i % no == 0:
            break
    
    else:
        prima.append(i)

print(f"Bilangan prima dari 0-{n} = {prima}")

    
    



    

    

        

        
    