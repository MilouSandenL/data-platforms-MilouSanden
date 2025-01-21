import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_path = Path(__file__).parent / "athlete_events.csv"
df = pd.read_csv(data_path)

print(df.head())

# Rita en enkel graf
df['Age'].hist()
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig(Path(__file__).parent / 'age_distribution.png')

