# 代码缺陷: 当计算 neg-content 的时候, 在前期的算法设计有一定的不足, 需通过修改 pos1 代码段弥补, 并取消 pos2 注释
# 当计算 mid 时, 需注释 pos1 和 pos2 代码段
# 当计算 其他部分 时, 需取消注释 pos1 和 pos2
# 修改下面一行,以达到特定需求
# fold_pth = 'D:/Users/leetu/Documents/_documents/cloudDrive/nutstore/workspace/代码/reviews_pos_neg_rat/data/hairDryer'
# fold_pth = 'D:/Users/leetu/Documents/_documents/cloudDrive/nutstore/workspace/代码/reviews_pos_neg_rat/data/microwave'
# fold_pth = 'D:/Users/leetu/Documents/_documents/cloudDrive/nutstore/workspace/代码/reviews_pos_neg_rat/data/pacifier'
# 修改下面一行,以达到特定需求
# file_name = fold_pth + '/pos.xlsx'
# file_name = fold_pth + '/neg.xlsx'
# file_name = fold_pth + '/mid.xlsx'

# print(fileName)

import xlrd

work_book = xlrd.open_workbook(file_name)
# 修改下面一行,以达到特定需求
# sheet = work_book.sheet_by_name('title')
# sheet = work_book.sheet_by_name('content')
rows_num = sheet.nrows
list_values = []
for r in range(rows_num):
    values = []
    row = sheet.row_values(r)
    values.append(str(row[1]))
# pos2_s
#     values.append(int(row[2]))
# pos2_e
    list_values.append(values)
    
# print(str(len(list_values)) + '\n')
# print(str(len(list_values[0])) + '\n')
# print(list_values[0][0] + '\n')
# print(str(list_values[0][1]) + '\n')
# print(str(type(list_values[0][0])) + str(type(list_values[0][1])))

# pos1_s
# for r in range(rows_num):
#     if list_values[r][1] > 1:
#         for i in range(list_values[r][1] - 1):
#             list_values.append(list_values[r])
            
# for r in range(rows_num):
#     if list_values[r][1] == 0:
#         del list_values[r]
# pos1_e
        
# print(str(len(list_values)) + '\n')
# print(list_values[-2][1])

text_tmp = [x[0] for x in list_values]
# print(text[1])

text = ' '.join(text_tmp)
# print(type(text))

# 写入文件
with open("./new.txt", "w", encoding='utf-8') as f:
        f.write(str(text))
        f.close()