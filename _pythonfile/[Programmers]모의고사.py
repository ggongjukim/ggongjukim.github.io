one = '12345' * (10000 // 5)
two = '21232425' * (10000 // 8)
three = '3311224455' * (10000 // 10)
count = [0, 0, 0]

def solution(preanswer):
  answer =[]
  for i in preanswer:
    answer.append(str(i))
  answer = answer+ ['0'] * (10000 - len(preanswer))

  print(answer)
  answerstr = ''.join(answer)

  for i in range(40):
    if one[i] == answerstr[i]:
      count[0] += 1
    if two[i] == answerstr[i]:
      count[1] += 1
    if three[i] == answerstr[i]:
      count[2] += 1

  result = []
  for i in range(len(count)):
    if max(count) == count[i]:
      result.append(i + 1)

  print(result)
  return result

solution([1,2,3,4,5])
