import numpy as np

import audio_mod
import audio_mod as am
file = open(r"E:\abd.txt","r")
list1 = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',#27 (0-26)
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',' ','R','S','T','U','V','W','X','Y','Z',#27 (27-53)
         '0','1','2','3','4','5','6','7','8','9',#10 (54-63)
         '`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+',#16 (64-79)
         ',','.',':',';','"','[',']','{','}','|']#10 (80-89)
stri = ""
final = ""
num_str = ""
print_str = ""

flag = 0
flag2 = 0
flag3 = 0
flag4 = 0
# flag5 = 0
i =0

freqz_siz = ""
freqz_lis = ""
freqz_siz_lis = []

freq_lis_final_sending_str = ""
freq_lis_final_sending_lst = []

while(1):
    ch = file.read(1)

    if not ch:
        print("reading...")
        break
    if ch=='1':
        flag=1
    if(flag==1 and i==4):
        stri = stri+ " "+ch
        i=1
    elif(flag==1):
        stri+=ch
        i = i+1


split_char = stri.split()
print((split_char))
file.close()

def converter(values):
    st = " "
    val = 0
    dic = {0:4,1:2,2:2,3:1}
    for k in range(len(values)):

        if values[k] == '1':
            val+=dic[k]
        else:
            val+=0
    #print(val)
    return val



m=0
for i in split_char:
    #converter(i)

    val = str(converter(i))
    if m<2:
        num_str = num_str + val
        m=m+1
    else:
        num_str = num_str+" "+val
        m=1


#print(num_str)

# def callingk():
#     sizes = ""
#     for i in split_char:
#         ho = str(converter(i))
#         sizes = sizes+ " " + ho
#     print(sizes)

def sending_freq(list3):
    tone = audio_mod.ToneGenerator()
    freq = list3
    freq2 = []
    mellody = []
    for i in freq:
        j=int(i)
        freq2.append(j)
    #print(freq2)
    for k in range(len(freq2)):
        mellody += list(tone.render(0.1,freq2[k],"saw"))
    audio_mod.ToneGenerator.write_file(np.array(mellody))
    print("uploaded audio!")

b = num_str.split()
print("converted string:", b,"\n")


for v in range(len(b)):#98...size of frequencies...97....frequencies
    val = int(b[v])
    val1 = int(val/10)
    val2 = int(val%10)
    if val1 != 0 and flag2!=1 and flag3!=1:
        #print(list1[val])  #use val and val1 key for calling
        if val == 98:
            flag2 = 1
        # elif val == 44:
        #     flag5 = 1
        else:
            print_str += list1[val]




    elif val1 ==0 and flag2!=1:
        #print(list1[val2])
        print_str += list1[val2]


    elif flag2==1:
        # sz1 = int(val / 10)
        # sz2 = int(val % 10)
        if val != 97 and flag3!=1:
            freqz_siz = freqz_siz+str(val1)+str(val2)
            freqz_siz_lis = list(freqz_siz)
        else:
            flag3 = 1
            flag2 = 0

    elif flag3==1:
        freqz_lis = freqz_lis + str(val1) + str(val2)



print("freq sizes",freqz_siz_lis)
#print(len(freqz_siz_lis))
print("freq list",list(freqz_lis))
#print(freq_lis_final_sending_str)
print("\nsender:",print_str)


if flag3==1 and flag4==0:
    k = 0
    # freqz_lis = freqz_lis + str(val1) + str(val2)
    for i in range(len(freqz_siz_lis)):
        m1 = freqz_siz_lis[i]
        #print(i)
        #print(m1)
        #print(freq_lis_final_sending_str)
        freq_lis_final_sending_lst = list(freq_lis_final_sending_str.split())
        print(freq_lis_final_sending_lst)
        sending_freq(freq_lis_final_sending_lst)

        for j in list(freqz_lis):
            if k<int(m1):
                freq_lis_final_sending_str = freq_lis_final_sending_str + j
                k += 1
            else:
                k = 0
                freq_lis_final_sending_str = freq_lis_final_sending_str + " " + j

        if(i==len(freqz_siz_lis)-1):
            flag4 = 1
            #print(flag4)


# if flag5 == 1:
#     file = open(r"E:\abd.txt","r+")
#     file.truncate(0)
#     file.close()







    #final +=list1[converter(i)]

#print("SENDER:",final)


