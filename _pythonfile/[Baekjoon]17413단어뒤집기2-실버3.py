#문자열 S 뒤집기
#문자열 S 알파벳 소문자, 숫자 공백, 특수 문자로만 이루어져있다
#문자열의 시작과 끝은 공백이 아니다
# > < 이 문자열에 있으면 번갈아 등장하며 <이 먼저 등장한다 두 문자의 개수는 같아
# 태그는 <로 시작해서 >로 끝나는 길이가 3이상인 부분 문자열이고  <와 > 사이에는 알파벳 소문자와 공백만 있다
# 단어는 알파벳과 숫자로 이루어진 부분 문자열이고 두 단어는 공백하나로 구분한다
#태그는 단어가 아니며 태그와 단어 사이에는 공백이 없다

# 입력

# 출력
# 입력의 문자열 S의 단어를 뒤집어 출력

# 발상
# 먼저 태그와 단어를 분리 해야함
import sys
s = list(input())
# print(s)
new =[]
word = []
isTag = False

for k,i in enumerate(s) :
  # print("k i ", k, i)
  if isTag == False and i == ' ':
    if len(word)!=0:
      # print("단어붙이기", word)
      new.append(''.join(word[:]))
      word.clear()
    new.append(' ')


  if i == '<':
    temp =[]
    isTag = True
    if len(word)!=0:
      # print("단어붙이기", word)
      new.append(''.join(word[:]))
      word.clear()


  if isTag == True:
    temp.append(i)

  if i == '>':
    new.append(''.join(temp))
    isTag = False

    continue

  if isTag == False and i != ' ':
    # print("word", i)
    word.append(i)

# print(new)

for i in new:
  if '<' not in i:
    print(i[::-1],end='')
  else:
    print(i,end='')
