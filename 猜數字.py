"""
if True:
     print('A')
else:
     print('B')
     print('C') 
     
if True:
     print('A')
else:
     print('B')
print('C')

if False:
     print('A')
else:
     print('B')
     print('C')

if False:
     print('A')
else:
     print('B')
print('C')
import random
num = random.randint(1,100)
while True:
    r=int (input("請輸入1-100:"))
    if num==r:
        print("猜對了")
        break
    else:
        print("猜錯了")
    #print(num)
"""


    
import random
a = 1
b = 100
num = random.randint(a,b)
while True:
    print("目前範圍%d-%d"%(a,b))
    r =  int(input('輸入數字:'))
    if r<a or r>b:
        print("請重新輸入數字")
    elif r>num:
        b = r
    elif r<num:
        a = r
    elif r==num:
        print("加分")
        break
    
    




