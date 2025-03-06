import pandas as pd
import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
CSV = DIR_CUR / "adult.csv"

df = pd.read_csv(CSV)
df['education_first_word'] = df['education'].str.split().str[0]

print(df[['education', 'education_first_word']])