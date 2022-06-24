def solution(line1, line2):
    origin2 = line2
    len1, len2  = len(line1), len(line2)
    answer = -1
    count = 0
    #공백 0
    #최대 공백 개수
    rang =0
    x =0
    while rang < len1:
      x +=1
      rang = len2 + (len2-1)*x
    print(x)
    print(rang)
    for i in range(x):

        origin2 = list(origin2)
        line2 = ('.'*i).join(origin2)
        print(i,line2)
        for j in range(len1-len(line2)+1):

            temp1 = line1
            temp2 = '.'*(j)+ line2 + '.'*(len1 - len(line2)-j)
            print(i ,j, temp2)

            for k in range(len1):
                temp2 = list(temp2)
                temp1 = list(temp1)
                if temp2[k] == '.':
                    temp1[k] = '.'

            if temp1 == temp2:
                print(temp1, temp2)
                count +=1

    answer = count
    return answer

solution('abbbcbbb','bbb')