import xlrd

# 不同文件需修改下面一行
# file_pth = 'D:/Users/leetu/Documents/_documents/sec_courses/mcm/mcm2020/code/src/hair_dryer.xlsx'
# file_pth = 'D:/Users/leetu/Documents/_documents/sec_courses/mcm/mcm2020/code/src/microwave.xlsx'
# file_pth = 'D:/Users/leetu/Documents/_documents/sec_courses/mcm/mcm2020/code/src/pacifier.xlsx'
# 不同文件需修改下面一行
# sheet_name = 'hair_dryer'
# sheet_name = 'microwave'
# sheet_name = 'pacifier'
data = xlrd.open_workbook(file_pth)
table = data.sheet_by_name(sheet_name)

row_s = 2 - 1 # 内容从第二行开始
row_e = table.nrows # 表格结束的行
col_s = 13 - 1 # reviews title 从M列开始
col_e = 15 # 日期在O列结束

list_values = []
for r in range(row_s, row_e):
    values = []
    row = table.row_values(r)
    for c in range(col_s, col_e):
        values.append(str(row[c]))
    list_values.append(values)
    
# print(list_values[1][1])
# print(list_values[1][1])
# print(list_values[1][0] + list_values[1][1])

# print(len(list_values))

import re

for r in range(len(list_values)):
    for c in range(2):
        list_values[r][c] = list_values[r][c].lower()
        list_values[r][c] = re.sub(r"[^a-zA-Z0-9]", " ", list_values[r][c])

# print(list_values[1][1])

from textblob import TextBlob
import xlsxwriter
workbook = xlsxwriter.Workbook('./review_ana.xlsx')
# 不同文件需修改下面一行
# worksheet = workbook.add_worksheet(u'dryer')
# worksheet = workbook.add_worksheet(u'microwave')
# worksheet = workbook.add_worksheet(u'pacifier')

for r in range(len(list_values)):
    title = list_values[r][0]
    content = list_values[r][1]
    title_blob = TextBlob(title)
    content_blob = TextBlob(content)
#     积极消极
    title_result_p = title_blob.sentiment.polarity
    content_result_p = content_blob.sentiment.polarity
#     主观客观
    title_result_s = title_blob.sentiment.subjectivity
    content_result_s = content_blob.sentiment.subjectivity
    worksheet.write(r, 0, title)
    worksheet.write(r, 1, content)
    worksheet.write(r, 2, title_result_p)
    worksheet.write(r, 3, content_result_p)
    worksheet.write(r, 4, title_result_s)
    worksheet.write(r, 5, content_result_s)
#     print(str(r) + '\t' + '->' + "title: " + str(title_result) + "cotent:" + str(content_result) + '\n')

workbook.close()

