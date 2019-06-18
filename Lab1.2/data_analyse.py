from matplotlib import pyplot
from openpyxl import load_workbook


def getvalue(x): return x.value


wb = load_workbook('C:\\Users\\pucher\\Documents\\Seafile\\p4ne_training\\data_analysis_lab.xlsx')

sheet = wb['Data']
# sheet['A'][1:]

result_x = map(getvalue, sheet['A'][1:])
list_x = list(result_x)

result_y1 = map(getvalue, sheet['C'][1:])
list_y1 = list(result_y1)

result_y2 = map(getvalue, sheet['D'][1:])
list_y2 = list(result_y2)

pyplot.plot(list_x, list_y1, label="Метка1")
pyplot.plot(list_x, list_y2, label="Метка2")
pyplot.legend(loc='upper left')
pyplot.show()
