from pvlib.tools import _golden_sect_DataFrame
import pandas as pd

def func(df, key):
    return df[key] * 2

params = pd.DataFrame({'x': [1, 2, 3]})
lower = pd.Series([1, 2, 3])
upper = pd.Series([1, 2, 3])

try:
    result, x = _golden_sect_DataFrame(params, lower, upper, func)
    print("Function executed successfully.")
except ValueError as e:
    print(f"Caught expected exception: {e}")
