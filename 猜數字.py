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
"""

import random
num = random.randint(1,100)
while True:
    r=int (input("請輸入1-100:"))
    if num==r:
        print("猜對了")
        break
    else:
        print("猜錯了")
    print(num)
    
    




