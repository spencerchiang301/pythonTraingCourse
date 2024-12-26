#tuple 元組，(a, b)
#元組裡的元素不可改變

t1 = (1, 2, 3)
#t1[0] = 3   #會得到錯誤
t1 = (4, 6, 7) #可以重新指派
print(t1)

# len 傳回元組的長度
print(len(t1))

# 用加號連接新的元組
t2 = t1 + (8, 9)
print(t2)

#可以 for 廻圈列出元組數據
for item in t2:
    print(item)

#Slice 使用切片語法取得元組數據
print(t2[1:3])

print(t2[:2])

print(t2[3])

# 用max 和 min 取出最大和最小值
print("最大值為：{}".format(max(t2)))
print("最小值為：{}".format(min(t2)))
