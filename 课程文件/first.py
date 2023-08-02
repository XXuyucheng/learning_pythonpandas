import pandas as pd
# a1 = pd.Series([],index=[],name='ID')
# a2 = pd.Series(['book1','book2','book3'],index=['1','2','3'],name='name')
# a3 = pd.Series([],index=[],name='instore')
# a4 = pd.Series([],index=[],name='data')
# df = pd.DataFrame({a1.name:a1,a2.name:a2,a3.name:a3,a4.name:a4})
# 方法1
# a1 = pd.Series([1,2,3],index=['1','2','3'],name='A')
# a2 = pd.Series([11,22,33],index=['1','2','3'],name='B')
# a3 = pd.Series([111,222,333],index=['2','3','4'],name='C')
# df = pd.DataFrame({a1.name:a1,a2.name:a2,a3.name:a3})
a1 = pd.Series([1,2,3],index=['1','2','3'],name='ID')
a2 = pd.Series(['book1','book2','book3'],index=['1','2','3'],name='name')
a3 = pd.Series([],index=[],name='listprice')
a4 = pd.Series([],index=[],name='dicount')
a5 = pd.Series([],index=[],name='price')
a6 = pd.Series([],index=[],name='time')
df = pd.DataFrame({a1.name:a1,
                   a2.name:a2,
                   a3.name:a3,
                   a4.name:a4,
                   a5.name:a5,
                   a6.name:a6,})
df = df.set_index('ID')
print(df)
df.to_excel('C:/Users/子耀/Desktop/books.xlsx')
print('done!')
# 方法2 注意直接用字典生成表格（datafram时每个键值对的长度必须保持一致）
# data = {'ID': ['1','2','3','4'],
#         'name': ['book1', 'book2', 'book3', 'book4'],
#         'listprice': ['', '', '', ''],
#         'discount': ['', '', '', ''],
#         'price': ['', '', '', '']}
# df = pd.DataFrame(data)
# df.set_index('ID', inplace=True)
# print(df)
# df.to_excel('C:/Users/子耀/Desktop/books.xlsx')
# print('done!')
