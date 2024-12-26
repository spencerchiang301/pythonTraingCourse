# set 集合，和 列表 List 很類似，但不允許有重覆的值

s = set([1, 2, 3, 3, 3, 2])
print(s)

# 新增元素用 add
s.add(9)
s.add(4)
s.add(8)
s.add(10)

# 移除元素 remove
s.remove(10)
print(s)

# 排列元素
sorted_s = sorted(s)
print(sorted_s)

# 列出所有的元素
for item in s:
    print(item, end='\t')

print()
# 列出集合的 長度，最大值，最小值和總和
print(len(s))
print(max(s))
print(min(s))
print(sum(s))

# 集合的特色，聯集，交集，差集和對稱差集
setA = {1, 6, 8, 10, 20}
setB = {1, 3, 7, 8, 10}

#聯集 A B 集合中所有項目
print(setA.union(setB))
print(setA | setB)

#交集 A B 集合中的共有項目
print(setA.intersection(setB))
print(setA & setB)

#差集 A 集合扣掉 AB集合中的共同項目
print(setA.difference(setB))
print(setA - setB)

#對稱差集, A B 集合中獨有項目
print(setA.symmetric_difference(setB))
print(setA ^ setB)

#子集合和超集合
#子集合 subset：若 A 集合的所有項目是 B 集合的部分集合, 則稱 A 為 B 的子集合
#超集合 superset： 若 A 集合的所有項目是 B 集合的部分集合, 則稱 B 為 A 的超集合

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(setA.issubset(setB))
print(setB.issuperset(setA))

# 判斷兩個集合是否相等 ==
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 4, 5}
print(setA == setB)