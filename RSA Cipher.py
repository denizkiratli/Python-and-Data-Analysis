#A program for ISE426 Assignment-1 by Deniz Kıratlı

def encrypt():
    e = int(input("Enter your public key's e: "))
    n = int(input("Enter your public key's n: "))
    st = input("Your text: ") #the string variable
    
    as_st = [] #the converted string to ascii list(int)
    for ch in st:
        as_st.append(ord(ch))
    #print(as_st)
    #encryption
    enc_st = [] #encrypted string character list(hex)
    for m in as_st:
        c = (m**e) % n
        enc_st.append(hex(c).replace("0x","0"))
    print("The encrypted text: " + enc_st)

def decrypt():
    d = int(input("Enter your private key's d: "))
    n = int(input("Enter your private key's n: "))
    e_st = input("Your encrypted text: ") #the encrypted-string variable

    #splitting the string into 4 characters list
    e_li = [] #the list of every char in encrypted-string
    i = 0
    j = 4
    while(j <= len(e_st)):
        e_li.append(e_st[i:j])
        i = i+4
        j = j+4
    #print(e_li)

    i_st = [] #the converted list string to integer 
    for char in e_li:
        i_st.append(int(char,16))
    #print(i_st)
    #decryption
    dec_li = []
    for c in i_st:
        m = (c**d) % n
        dec_li.append(chr(m))
    #print(dec_li)
    dec_st = ''.join(dec_li)
    print("The decrypted text: " + dec_st)

def main():
    
    #Taking two prime numbers (p,q) and checking whether they are prime number.
    flag = 0
    while flag == 0:
        p = int(input("Give p: "))
        if p > 1:
            if p == 2:
                flag = 1
            for i in range(2,p):
                if (p % i) != 0:
                    flag = 1
                else:
                    print ("The given number is not a prime number.")
                    break
        else:
            print ("A prime number should greater than 1.")
    
    flag = 0
    while flag == 0:
        q = int(input("Give q: "))
        if q > 1:
            if p == 2:
                flag = 1
            for i in range(2,q):
                if (q % i) != 0:
                    flag = 1
                else:
                    print ("The given number is not a prime number.")
                    break
        else:
            print ("A prime number should greater than 1.")

    #Calculating n, z, e, d
    n = int(p*q)
    z = int((p-1)*(q-1))

    e = int(input("Give an e that e<z, prime to z: "))

    for d in range(1,z):
        if (((e*d) % z) == 1):
            break
    
    #Taking public and private keys
    print("Your public key is: (" + str(e) + "," + str(n) + "), (e,n)")
    print("Your private key is: (" + str(d) + "," + str(n) + "), (d,n)")

    cho = input("To encrypt press 'e' or to decrypt press 'd': ")
    if cho == 'e':
        encrypt()
    elif cho == 'd':
        decrypt()


if __name__ == '__main__':
    main()