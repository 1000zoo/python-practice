#####https://wikidocs.net/160686

import pandas as pd

data = [1000, 2000, 3000]
s = pd.Series(data)
s.index = ["메로나", "구구콘", "하겐다즈"]
print(s)

rank = [4, 3, 5, 1, 2]
index = ["메로나", "구구콘", "하겐다즈", "쌍쌍바", "셀렉션"]
s2 = pd.Series(rank, index)
print(s2)

new_index = ["메로나", "구구콘", "보석바", "쌍쌍바", "와일드바디"]
s3 = s2.reindex(new_index, fill_value=0)
print(s3)