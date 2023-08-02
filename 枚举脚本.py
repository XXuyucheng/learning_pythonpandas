import pandas as pd
from itertools import combinations

def create_combinations(words):
    combinations_list = []
    for r in range(1, len(words)+1):
        combs = combinations(words, r)
        combinations_list.extend(combs)

    return combinations_list

def main():
    input_words = input("请输入词语，以空格分隔：")
    words_list = input_words.split()
    combinations_list = create_combinations(words_list)

    df = pd.DataFrame(combinations_list, columns=[f"Word{i}" for i in range(1, len(words_list)+1)])
    df.index = df.index + 1  # Adding 1 to index to make it start from 1
    print(df)

if __name__ == "__main__":
    main()
#枚举所有可能