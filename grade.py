r=int (input("請輸入成績:"))
if r>=90:
    print("分數等極為A")
elif r>=80:
    print("分數等極為B")
elif r>=70:
    print("分數等極為C")
elif r>=60:
    print("分數等極為D")
else:
    print("分數等極為E")
    
    
    
r=int (input("請輸入成績1:"))
s=int (input("請輸入成績2:"))
if r>=90 and s>=90 or r>=100 and s>=90 or r>=90 and s>=100:
    print("有獎品")
elif r>=90 and s<90 or r<=90 and s>90 or r>=80 and s>=80:
    print("再加油")
elif r<=60 and s<=60:
    print("要處罰")
else:
    print("分數過低")

