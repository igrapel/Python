
#Euclidean Algorithm to find greatest common factor
def gcd(a, b):
    while(True):
        temp = a%b 
        if (temp == 0): 
            return b 
        a = b; 
        b = temp; 


#Create public encryption keys
#Formula: Encryption ^ public exponent key % public modulus key

def public_keys_generator(prime1, prime2):
    public_modulus_key = prime1*prime2
    
    #Euler's Totient
    phi = (prime1 - 1) * (prime2 -1)
    
    possible_keys = []
    for num in range(2, phi):
        factor = gcd(num, phi)
        if(factor==1):
            possible_keys.append(num)
            
    keys= dict();
    keys['public_modulus'] = public_modulus_key
    keys['public_exponent'] = possible_keys
    
    return keys

print(public_keys_generator(5, 11))
