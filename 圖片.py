file = open("image.jpg","rb")#rb.讀取圖片的二進位
img = file.read()
print(img)
file.close()

copy = open("copy.jpg","wb")
copy.write(img)
copy.close()