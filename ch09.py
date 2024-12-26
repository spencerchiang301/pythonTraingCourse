#dict 字典
#由 key 和 value 組成，沒有順序, 值可包含任何種類數據
a = dict(name = 'Zara', age = 7, phone = '0911222333', sex= 'female')

#取出數據，dict[key]
print("a['name'] : ", a['name'])

#取出全部數據的key
print("a.keys() : ", a.keys())

#取出全部數據的values
print("a.values() : ", a.values())

#可以用 for 廻圈和 items 取出全部的 key, value
for k, v in a.items():
    print(k, v)

#新增或修改一組數據, dict[key] = value，若原有key 存在，修改它。key 不存在，則新增它。
a['address'] = 'Kampung Jakarta'
print(a)

a['age'] = 12
print(a)

#刪除某一key, del dict[key]
del a['age']
print(a)

#查詢某一 key 是否存在字典中
if 'address' in a:
    print("address is exist")
else:
    print("address is not exist")

#查詢某一 value 是否存在字典中
if 'Zara' in a.values():
    print("Zara is exist")
else:
    print("Zara is not exist")

#從一組 seq 裡創建dict, 不指定預設值為 None
seq = ('python','java','rust')
language1  = dict.fromkeys(seq)
print(language1)

language2 = dict.fromkeys(seq, 'programing')
print(language2)

#將 dict1 更新至 dict2 裡
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict2.update(dict1)
print(dict2)
