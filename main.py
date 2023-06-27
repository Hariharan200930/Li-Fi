fil = open(r"E:\abd.txt","r")
str = " "
i=0
f=0
while(1):

    c = fil.read(1)
    #print(c)
    if not c:
        break
    #print(c)
    if c=='1':
        f=1
    if(f==1 and i==5):
        str = str+ " "+c
        #print(i)
        i=1
    elif(f==1):
        str += c
        i = i + 1
        #print(i)


    #str+=c
#print(str)
x = str.split()




print(x)
fil.close()
def conv(y):
    if y=='00000':
        return ' '
    if y=='00001':
        return 'b'
    if y=='00010':
        return 'c'
    if y=='00011':
        return 'd'
    if y=='00100':
        return 'e'
    if y=='00101':
        return 'f'
    if y=='00110':
        return 'g'
    if y=='00111':
        return 'h'
    if y=='01000':
        return 'i'
    if y=='01001':
        return 'j'
    if y=='01010':
        return 'k'
    if y=='01011':
        return 'l'
    if y=='01100':
        return 'm'
    if y=='01101':
        return 'n'
    if y=='01110':
        return 'o'
    if y=='01111':
        return 'p'
    if y=='10000':
        return 'q'
    if y=='10001':
        return 'r'
    if y=='10010':
        return 's'
    if y=='10011':
        return 't'
    if y=='10100':
        return 'u'
    if y=='10101':
        return 'v'
    if y=='10110':
        return 'w'
    if y=='10111':
        return 'y'
    if y=='11000':
        return 'y'
    if y=='11001':
        return 'z'
    if y=='11010':
        return 'a'
    if y=='11111':
       return ' '
    if y=='11011':
        f=0
        return ' '



for i in x:
    print(conv(i),end='')

#print('\n')



