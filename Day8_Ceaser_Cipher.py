def encrypt(text,shift):
    final=[]
    resultant=""
    for i in range(0,len(text)):
        final.append(' ')
        if text[i] in alphabet:

            pos=(ord(text[i])+shift)%123
            if ((pos>=97) & (pos<=122)):
                pos=pos
            else:
                pos=pos+97
            final[i]=chr(pos)
        else:
            final[i]=text[i]

        
    for j in final:
        resultant+=j


    print(resultant)


def decrypt(text,shift):
    final=[]
    resultant=""
    for i in range(0,len(text)):
        final.append(' ')
        if text[i] in alphabet:
            
            pos=(ord(text[i])-shift)
            if ((pos>=97) & (pos<=122)):
                pos=pos
            else:
                pos=pos+26

            final[i]=chr(pos)
        else:
            final[i]=text[i]
        
    for j in final:
        resultant+=j

    print(resultant)


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z']


choice="yes"

while (choice=="yes"):
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("enter the text:\n")
    shift=int(input("enter the shift number:\n"))
    if (direction=='encode'):
        encrypt(text,shift)
    elif (direction=="decode"):
        decrypt(text,shift)
    choice=input("Enter your choice 'yes' to continue and 'no' to exit:\n")


