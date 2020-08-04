a = int(input("全班有幾人?"))
list_score = []
name = []
for i in range(a):
    name_input = input("請輸入你的名字:")
    score = int(input("請輸入成績:"))
    list_score.append(score)
    name.append(name_input)
    #if score not in list_score:
     #   list_score.append(score)

sum_score = sum(list_score)

print("全班平均:",sum_score/a)
h = 0
#for n in  list_score:
for n in range(a):
    if list_score[n]>h:
       h = list_score[n]
       high_name = name[n]

print("最高分為:",h,high_name)
c = 100
#for n in  list_score:
for n in range(a):
    if list_score[n]<c:#n<c:
       c = list_score[n]
       low_name = name[n]

print("最低分為:",c)