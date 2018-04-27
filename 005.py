i = 1  
for j in (range(1, 21)):  
    if i % j > 0:
        for k in range(1, 21):
            if (i * k) % j == 0:
                i *= k
                break
print(i)  
