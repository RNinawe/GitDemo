list = [1,2,3,4,5,1,2]


for i in list:
    flag = 0
    cnt = 0
    for j in list:
        if i == j:
            cnt = cnt + 1
            #print("i-", i,"j-",j)
            #print("cnt-",cnt)
            if cnt > 1:
                flag = 1
    if flag == 0:
        print(i)