print("*********************************")
print("*********歡迎來到團隊隊餐廳*******")
print("*********************************")
print("*********************************")
print("************以下是菜單************")


while True:
    print("A.漢堡 Hamburger==>$50")
    print("B.")
    print("C.")
    print("D.")
    print("E.")
    print("F.")
    print("G.")
    print("H.")
    print("I.")
    print("J.")
    
    
    print("要結帳請按10")
    sel = input("請輸入菜單選項:  ")
    if sel=="10":
        break
    
    elif sel=="A": 
        dic = input("請輸入數量: ")
        print("點了漢堡")
        print("1. 1個")
        print("2. 2個")
        print("3. 3個")
        print("4. 4個")
        print("5. 5個")
        print("6. 6個")
        print("7. 7個")
        print("8. 8個")
        print("9. 9個")
        print("10. 10個")
        food="漢堡 Hamburger"
        if dic=="1":
            print("1個",food*1)
        elif dic=="2":
            print("2個",food)
        elif dic=="3":
            print("3個",food)
        elif dic=="4":
            print("4個",food)  
        elif dic=="5":
            print("5個",food)
        elif dic=="6":
            print("6個",food)
        elif dic=="7":
            print("7個",food)
        elif dic=="8":
            print("8個",food)
        elif dic=="9":
            print("9個",food)
        elif dic=="10":
            print("10個",food)








'''
import os.path

if not os.path.isfile("mydictionary.txt"):
    fo = open("mydictionary.txt","w")
    print("new file")
else:
    fo = open("mydictionary.txt","r")
    print("old file")

for row in fo.readlines():
    data = row.split(":")

    key = data[0]
    value = data[1]
    value = value.strip()

    dic[key]=value
print(dic)

fo.close()


while True:
    print("1.建立字彙")
    print("2.列印全部資料")
    print("3.英翻中")
    print("4.中翻英")
    print("5.學習測驗")
    print("6.離開系統")
    sel = input("請輸入功能選項:  ")
    if sel=="1":
        en = input("輸入英文單字:")
        coc = input("輸入中文解釋:")
        dic[en]=coc

        fo = open("mydictionary.txt","w")
        for k,v in dic.items():
            fo.write(k)
            fo.write(":")
            fo.write(v)  
            fo.write("\n")
        fo.close()

    elif sel=="2":
        for k,v in dic.items():
            print(k,":",v)
    elif sel=="3":
        search = input("搜尋英文:")
        print(dic[search])
    elif sel=="4":
        s = input("搜尋中文:")
        for k,v in dic.items():
            if s==v:
                print(k)
    elif sel=="5":
        score=0
        for k,v in dic.items():
           print(v,":")
           ans = input("請輸入你的答案:")
           if ans==k:
               print("恭喜答對")
               score = score +1
        print("你的分數:",score)

    elif sel =="6":
        break
    '''