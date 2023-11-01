import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import DataFrame, Series

sns.set()

data = {
    "salary": [12000, 12000, 12000, 12000, 12000, 12000, 12000, 12000, 12000],
    "yearAwards": [40000, 41000, 42000, 40000, 41000, 42000, 40000, 41000, 42000],
    "property": [
        "merge",
        "merge",
        "merge",
        "sep",
        "sep",
        "sep",
        "opti",
        "opti",
        "opti",
    ],
    "tax": [1, 2, 3, 4, 5, 6, 7, 8, 9],
}
# data = {

# }
df = DataFrame(data)
print(df)
fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
# sns.stripplot(x=df.sg, y=df.hwy, jitter=0.25, size=8, ax=ax, linewidth=0.5)
sns.swarmplot(
    x="yearAwards", y="tax", data=df, hue="property", dodge=False, palette="husl"
)
plt.savefig("1.png")
