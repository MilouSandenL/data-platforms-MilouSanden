import pandas as pd
import sys

print("\n\n")
print(f"{sys.version =}")

data = {
    "Name": ["Erik", "Anna", "Johan", "Lisa", "Oskar"],
    "Age": [28, 34, 40, 25, 50],
    "City": ["Stockholm", "Göteborg", "Malmö", "Uppsala", "Lund"],
    "Salary_sek": [45000, 32000, 20000, 25000, 30000]
}

df = pd.DataFrame(data)

print(df)


