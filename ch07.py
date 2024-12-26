# List，列表，一個集合，可以擁有不同的型號

a = [1, 7, 3, 5, 4]
b = ['c', 1, 3]
print(type(a))

# len 取得型別的長度，並用 for 列出內容
for i in range(len(a)):
    print("{}:{}".format(i, a[i]))

for item in a:
    print(item)

# Slice 切片 [start:end:step]
# 取出全部資料
print(a[:])

# 取出第 1個至第3 個的內容 list[0:3]
print(a[0:3])

# 取出第 1個至第 5個內容，中間間隔 1個
print(a[0:5:2])

# 取出最後一個
print(a[-1])

# 取出最後三個
print(a[-3:])

#針對列表做排列
sorted_a = sorted(a)
print(sorted_a)

#取出最大和最小值
print("{} {}".format(min(a), max(a)))

#取出列表第n元素
print(sorted_a[3])

#刪除列表第n個元素
sorted_a.remove(3)
print(sorted_a)

#確認某元素是否在在列表中
print(3 in sorted_a)
print(5 in sorted_a)

#新增元素至列表中
sorted_a.append(10)
print(sorted_a)

#反轉列表元素
sorted_a.reverse()
print(sorted_a)

#計算某元素出現的次數
b = [1, 3, 4, 3, 5, 8, 7, 3, 4, 10]
print(b.count(3))

#找出符合元素的第一個位置
print(b.index(4))

#移除最後一個元素
b.pop()
print(b)

#在特定位置插入元素
b.insert(3, 10)
print(b)

#在列素最後方加入一排元素
b.extend([1, 2, 3])
print(b)


