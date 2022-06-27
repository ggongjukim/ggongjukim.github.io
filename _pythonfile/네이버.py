#한글보드에 특정한 단어를 넣어 글자 사이 거리비교
# 위 보드에 있는 글자 찾아 가로+세로
# 거리 총합과 글자 글자 사이 계산한 거리개수 리턴
# 글자 거리 : 가로 +세로
# 토토 거리값 0 거리개수 +=1
# 없는 글자 거리값 20 횟수 +=1
boa = ["가호저론남드부이프설","알크청울키초트을배주","개캠산대단지역구너양", "라로권교마쿼파송차타",
         "코불레뉴 서한산리개","터강봄토캠상호론운삼", "보람이경아두프바트정", "스웨어쿼일소라가나도",
         "판자비우사거왕태요품", "안배차캐민광재봇북하"]
board =[]
for i in boa:
    board.append(list(i))
# print(board)
ray = []
result =[]

def solution(word):
    answer = [0,0]
    word = list(word)
    for i in word:
        print("i",i)
        count = 0
        temp =[]
        for j in range(10):
            if i in board[j]:
                count += 1
                temp.append([board[j].index(i),j])
                # print("있음",temp)


        if count != 0:
            if count == 1:
                # print("temp",temp)
                ray.append(temp[0])
            else:
                temp2=[]
                for i in temp:
                    print("i!",i)
                    temp2.append(abs(ray[-1][0] -i[0])+ abs(ray[-1][1] - i[1]))
                # print("temp2",min(temp2))
                # print("짧은거",temp[temp2.index(min(temp2))])
                ray.append(temp[temp2.index(min(temp2))])
        # else :
        #     ray.append('*')

            print("ray",ray)
    for i in range(1,len(ray)):
        print("거리",abs(ray[i][0]-ray[i-1][0]) + abs(ray[i][1]-ray[i-1][1]))
        answer[0] += abs(ray[i][0]-ray[i-1][0]) + abs(ray[i][1]-ray[i-1][1])
        result.append(abs(ray[i][0]-ray[i-1][0]) + abs(ray[i][1]-ray[i-1][1]))
    print("result",result)
    answer[1] = len(result)
    # answer.append(len(result))
    return answer