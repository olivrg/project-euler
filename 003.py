the_number = 600851475143  
prime = 2

while prime * prime < the_number:  
    while not the_number % prime:
        the_number //= prime
    prime += 1

print (the_number) 
