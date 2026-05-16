import power_curve
import sort

def Leistungskurve():
    data = power_curve.getData()
    data_list = data.to_dict("records")

    data_sort = sort.bubble_sort_desc(data_list)
    #print(data_sort[:10])
    power_curve.getFigure(data_sort)


Leistungskurve()