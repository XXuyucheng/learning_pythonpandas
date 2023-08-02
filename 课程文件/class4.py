import pandas as pd
books = pd.read_excel('C:/Users/子耀/Desktop/books.xlsx',
                      skiprows=2,#跳过前两行
                      usecols="C:H",#只有使用从第几列到第几列：usecols="C"
                      index_col=None)#暂时不设索引列
# print(books['ID'])
# print (type[books['ID']])
# books['ID'].at[0] = 100 # 可以通过at函数给一个特定位置设置一个值
# print(books['ID'])
for i in books.index:
    books['ID'].at[i] = i + 1
    
print(books)