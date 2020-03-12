import xlrd
file_pth = 'D:/Users/leetu/Documents/_documents/sec_courses/mcm/mcm2020/code/src/hair_dryer.xlsx'
data = xlrd.open_workbook(file_pth)
table = data.sheet_by_name('hair_dryer')

row_s = 2 - 1
row_e = 11471
col_s = 13 - 1 # form M col
col_e = 15 # end O col

list_values = []
for r in range(row_s, row_e):
    values = []
    row = table.row_values(r)
    for c in range(col_s, col_e):
        values.append(row[c])
    list_values.append(values)
    
# print(type(list_values[1][2]))

# print(list_values[1][0] + '\n')
# print(list_values[1][1] + '\n')
# print(list_values[1][2] + '\n')

