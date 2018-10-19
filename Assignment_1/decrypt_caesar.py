from collections import defaultdict

freq=defaultdict(lambda: 0)

with open('caesar_cipher_text','r') as f:
    #count frequency of each letter
    for line in f:
        words=line.split()
        for w in words:
            for c in w:
                if c.isalpha():
                    freq[c.lower()]+=1 
    
    l=sorted(freq.items(),key=lambda x : x[1],reverse=True) #sort the frequency table to get letter with highest frequency

    shift=ord(l[0][0])-ord('e') #calculate shift by comparing most frequent letter with 'e'.
    f.seek(0,0)
    print("KEY :",chr(shift%26+97),'\n')
    
    print("PLAINTEXT : \n")
    for line in f:
        for c in line:
            if c.isalpha():
                print(chr((ord(c.lower())-97-shift)%26+97),end='') #shift the letters back to get the plaintext
            else:
                print(c,end='')
    print()
    f.close()