#bubble sort

import power_curve

def bubble_sort_desc(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):

            # Vergleich nach "Leistung"
            if data[j]["Leistung"] < data[j + 1]["Leistung"]:
                
                # Tauschen
                data[j], data[j + 1] = data[j + 1], data[j]

    return data
