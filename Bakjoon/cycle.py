num=list(input())
if len(num) == 1:
    num.insert(0, '0') #insert 중요. 밀어내고 대입하는 함수. 

input_num=int(num[0])*10+int(num[1])
cycle=0
while(True):
    num_list=num
    first_num=(int(num[0])+int(num[1]))%10
    second_num=int(num[1])
    new_num=second_num*10+first_num
    cycle+=1
    num[0]=second_num
    num[1]=first_num
    if(new_num==input_num):
        break
print(cycle)