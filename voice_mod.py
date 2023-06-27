#import color_detection
import pyttsx3
import goto_py

#color_detection()

fil = open(r"E:\abd.txt","r")
str = ""
i=0
f=0
p=0

def play(txt):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 150)
    print(" ")
    print(txt)
    engine.say(txt)
    print(" ")
    engine.runAndWait()


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
    elif y=='00001':
        return 'b'
    elif y=='00010':
        return 'c'
    elif y=='00011':
        return 'd'
    elif y=='00100':
        return 'e'
    elif y=='00101':
        return 'f'
    elif y=='00110':
        return 'g'
    elif y=='00111':
        return 'h'
    elif y=='01000':
        return 'i'
    elif y=='01001':
        return 'j'
    elif y=='01010':
        return 'k'
    elif y=='01011':
        return 'l'
    elif y=='01100':
        return 'm'
    elif y=='01101':
        return 'n'
    elif y=='01110':
        return 'o'
    elif y=='01111':
        return 'p'
    elif y=='10000':
        return 'q'
    elif y=='10001':
        return 'r'
    elif y=='10010':
        return 's'
    elif y=='10011':
        return 't'
    elif y=='10100':
        return 'u'
    elif y=='10101':
        return 'v'
    elif y=='10110':
        return 'w'
    elif y=='10111':
        return 'y'
    elif y=='11000':
        return 'y'
    elif y=='11001':
        return 'z'
    elif y=='11010':
        return 'a'
    elif y=='11111':
        return ' '
    elif y=='11011':
        return ' '


txt = ""
for i in x:
    #print(conv(i),end='')
    txt += conv(i)
print(txt)
yup =txt.split()
for i in yup:
    if i=="end":
        p=1
        #txt.removesuffix("end")
        print(p)


if p==1:
    def calplay():
        play(txt.removesuffix("end"))
        p=0
    calplay()

#print('\n')



