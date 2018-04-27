i = 100  
p = []

while i <= 999:  
    for j in range(i, 1000):
        number = i * j
        var = str(number)
        if var == var[::-1]:
            p.append(int(var))

    i += 1

print(max(p)) 
