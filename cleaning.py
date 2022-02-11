import pandas as pd

def read_and_clean_results():
    df = pd.read_csv("results.csv")
    df["date"] = df["date"].str.replace("-","/")
    df.dropna(inplace = True)
    df.to_csv(r"C:\Users\Public\results_clean.csv",index = False)
read_and_clean_results()


def read_and_clean_shootouts():
    df = pd.read_csv("shootouts.csv")
    df.dropna(inplace = True)
    df.to_csv(r"C:\Users\Public\shootouts_clean.csv",index = False)
read_and_clean_shootouts()