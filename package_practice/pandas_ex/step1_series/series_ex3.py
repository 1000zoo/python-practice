#####https://wikidocs.net/160685

import pandas as pd

data = ["high", "low", "start", "end"]
s = pd.Series(data)
print(s)

mixed_data = ["samsung", 68000]
mixed_series = pd.Series(mixed_data)
print(mixed_series)