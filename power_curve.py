#power curve
import matplotlib.pyplot as plt
import power_curve
import sort
import load_data

def getFigure(data):

    power_values = []

    for row in data:
        power_values.append(row["PowerOriginal"])

    plt.plot(power_values)
    plt.xlabel("Zeit")
    plt.ylabel("Power")
    plt.title("Leistungskurve")

    plt.savefig("figures/Leistungskurve.png")

    plt.show()
    


def Leistungskurve():
    data = load_data.getData()
    data_list = data.to_dict("records")

    data_sort = sort.bubble_sort_desc(data_list)
    #print(data_sort[:10])
    power_curve.getFigure(data_sort)


Leistungskurve()