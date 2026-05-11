#power curve
import pandas as pd

def getData():
    
    df = pd.read_csv("activity.csv")

    print(df)
    return df

