#string=str(input())
#i=0
#sec=0
#for i in range(len(string)):
#    if string[i] == " ":
#        num=1
#    if 'A'<=string[i] and string[i]<='C':
#        num=2
#    if 'D'<=string[i] and string[i]<='F':
#        num=3
#    if 'G'<=string[i] and string[i]<='I':
#        num=4
#    if 'J'<=string[i] and string[i]<='L':
#        num=5
#    if 'M'<=string[i] and string[i]<='O':
#        num=6
#    if 'P'<=string[i] and string[i]<='S':
#        num=7
#    if 'T'<=string[i] and string[i]<='V':
#        num=8
#    if 'W'<=string[i] and string[i]<='Z':
#        num=9
#    if string[i]=='OPERATOR':
#        num=0
#    sec+=num+1
#print(sec)

# 우정아
word = input()

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
for i in range(len(word)):
    for j in dial:
        if word[i] in j:#범위 내 있으면. 
            time += dial.index(j)+3#인덱스 + 1 + 2(num+2초니까.)
print(time)