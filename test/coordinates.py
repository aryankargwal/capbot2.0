import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [10, -10], columns=["lat", "lon"]
)
df.to_csv("file1.csv")
