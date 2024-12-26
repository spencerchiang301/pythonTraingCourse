# 檔案處理 File
# 使用 w，寫入內容至檔案裡，它會覆蓋原檔案，假如檔案存在
# 使用 a，寫入內容至檔案裡，它會加入內容原檔案，假如檔案存在
# 使用 r，取出檔案的內容


with open('test.txt', 'w') as fp:
    fp.write('Hello World')

with open('test2.txt', 'a') as fp:
    fp.write('Hello World')

with open('test2.txt', 'r') as fp:
    for line in fp.readlines():
        print(line)


# 取得當前目錄
import os
print(os.getcwd())

# 列出當前目錄下所有檔案和目錄
import os
print(os.listdir())

# 列出當前目錄下所有資料夾
folder = []
files = []
for item in os.scandir():
    if item.is_dir():
        folder.append(item.name)
    else:
        files.append(item.name)
print(folder)
print(files)



