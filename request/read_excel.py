import xlrd
import xlwt
from xlutils3.copy import copy

data = xlrd.open_workbook('../test.xls')
table = data.sheets()[0]

# 行数
nrows = table.nrows
print(nrows)

# 该行全部数据
row = table.row_values(rowx=0, start_colx=0)
print(row)

#列数
ncols = table.ncols
print(ncols)

# 该列数据
col = table.col_values(colx=0, start_rowx=0)
print(col)

# 操作单元格
cell = table.cell_value(rowx=0, colx=1)
print(cell)

# 复制表重新写入
new = copy(data)
newwb = new.get_sheet(0)
newwb.write(3, 0, "星穹铁道")
new.save("../tests.xls")

# 设计表
workbook = xlwt.Workbook(encoding="ascii")
worksheet = workbook.add_sheet("my sheet")