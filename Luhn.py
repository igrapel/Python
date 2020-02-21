
while True:
    CC = (input("What is your credit card number?"))
    try:
       val = int(CC)
       break
    except:
        CC = (input("What is your credit card number?"))

digit_length = len(CC)

#Amex case
if (digit_length == 15) and (CC[0]== '3' and CC[1]=='4' or CC[1] == '7'):
    a=CC[13]
    b=CC[11]
    c=CC[9] 
    d=CC[7]
    e=CC[5]
    f=CC[3]
    g=CC[1]
        
    Digits = [a,b,c,d,e,f,g]
    Digits = [int(i) for i in Digits]
    Digits2=[i*2 for i in Digits]
    the_sum = sum(int(char) for n in Digits2 for char in str(n))
        
    amex_sum = sum(int(i) for i in CC[::2])
        
    luhn=(amex_sum+the_sum)
        
    if luhn%10 == 0:
        print("AMEX")
        
    else:
        print("INVALID")

#MasterCard      
elif (digit_length == 16) and (CC[0]== '5') and (CC[1]=='1' or CC[1] == '2' or CC[1]=='3' or CC[1] == '4' or CC[5]):
    a=CC[14]
    b=CC[12]
    c=CC[10] 
    d=CC[8]
    e=CC[6]
    f=CC[4]
    g=CC[2]
    h=CC[0]
        
    Digits = [a,b,c,d,e,f,g,h]
    Digits = [int(i) for i in Digits]
    Digits2=[i*2 for i in Digits]
    the_sumMC = sum(int(char) for n in Digits2 for char in str(n))
    
    MC_sum = sum(int(i) for i in CC[1::2])
        
    luhn=(MC_sum+the_sumMC)
        
    if luhn%10 == 0:
        print("MASTER CARD")
        
    else:
        print("INVALID")
        
#Visa Case       
elif (digit_length == 16) and (CC[0]== '4'):
    a=CC[14]
    b=CC[12]
    c=CC[10] 
    d=CC[8]
    e=CC[6]
    f=CC[4]
    g=CC[2]
    h=CC[0]
        
    Digits = [a,b,c,d,e,f,g,h]
    Digits = [int(i) for i in Digits]
    Digits2=[i*2 for i in Digits]
    the_sumVisa = sum(int(char) for n in Digits2 for char in str(n))
    
    the_sumVisa2 = sum(int(i) for i in CC[1::2])
    luhn=the_sumVisa2+the_sumVisa
        
    if luhn%10 == 0:
        print("VISA")
        
    else:
        print("INVALID")

#Visa Case         
elif digit_length == 13 and CC[0]== '4':
    a=CC[11]
    b=CC[9] 
    c=CC[7]
    d=CC[5]
    e=CC[3]
    f=CC[1]
        
    Digits = [a,b,c,d,e,f]
    Digits = [int(i) for i in Digits]
    Digits2=[i*2 for i in Digits]
    the_sum = sum(int(char) for n in Digits2 for char in str(n))
        
    visa_sum = sum(int(i) for i in CC[::2])
    luhn = (the_sum+visa_sum)    
    if (luhn)%10 == 0:
        print("VISA")
        
    else:
        print("INVALID")
        
else:
    print("INVALID")
