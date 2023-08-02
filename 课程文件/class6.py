# 在pandas中进行数字填充
import pandas as pd
books = pd.read_excel('C:/Users/子耀/Desktop/books.xlsx')
books = books.set_index('ID')
