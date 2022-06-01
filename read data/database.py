import xlrd
data = xlrd.open_workbook("../test.xls")
table = data.sheets()[0]
nrows = table.nrows
print(nrows)
ncols = table.ncols
print(ncols)
keys = table.row_values(0)
print(keys)
site = []
for i in range(1, nrows):
    #获取行数对应全部数据
    data = table.row_values(i)
    apo_dict = dict(zip(keys, data))
    site.append(apo_dict)
print(site)
for t in range(nrows-1):
    faith = site[t]["名称"]
    print(faith)

