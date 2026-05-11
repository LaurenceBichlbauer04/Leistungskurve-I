#power curve
import pandas as pd
import matplotlib.pyplot as plt
import sort

def getData():
    
    df = pd.read_csv("activity.csv")

    print(df)
    return df

def getFigure(Data):
    plt.plot(Data)
