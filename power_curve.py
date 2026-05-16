#power curve
import pandas as pd
import matplotlib.pyplot as plt


def getData():
    
    df = pd.read_csv("activity.csv")

    #print(df)
    return df

def getFigure(data):

    power_values = []

    for row in data:
        power_values.append(row["PowerOriginal"])

    plt.plot(power_values)
    plt.xlabel("Zeit")
    plt.ylabel("Power")
    plt.title("Leistungskurve")


    plt.show()