#####https://wikidocs.net/160686

import pandas as pd

data = [1000, 2000, 3000]
s = pd.Series(data)
print(s.index)
print(s.index.to_list())