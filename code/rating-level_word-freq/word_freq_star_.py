import xlrd

# file_pth = 'D:/Users/leetu/Documents/_documents/sec_courses/mcm/mcm2020/code/src/origin_tables/hair_dryer.xlsx'
# file_pth = 'D:/Users/leetu/Documents/_documents/sec_courses/mcm/mcm2020/code/src/origin_tables/microwave.xlsx'
file_pth = 'D:/Users/leetu/Documents/_documents/sec_courses/mcm/mcm2020/code/src/origin_tables/pacifier.xlsx'

workbook = xlrd.open_workbook(file_pth)
sheet = workbook.sheet_by_index(0)
# print(sheet.nrows)

star_1 = []
star_2 = []
star_3 = []
star_4 = []
star_5 = []
for row in range(1, sheet.nrows):
    values = []
    row_value = sheet.row_values(row)
#     index of H col is 7
    values.append(str(row_value[12]) + str(row_value[13])) # index of title col is 12
#     values.append(row_value[13]) # index of content col is 13
    rating_star = int(row_value[7])
    print(str(row) + ' -> ' + str(row_value[7]))
#     print(row_value[7])
    if rating_star == 1:
        star_1.append(values)
#         print('tag_' + str(row))
    elif rating_star == 2:
        star_2.append(values)
#         print('tag_' + str(row))
    elif rating_star == 3:
        star_3.append(values)
#         print('tag_' + str(row))
    elif rating_star == 4:
        star_4.append(values)
#         print('tag_' + str(row))
    elif rating_star == 5:
        star_5.append(values)
#         print('tag_' + str(row))

# print(str(len(star_1)) + ' - ' + str(len(star_1[0])))

# print(len(star_1))
# print(len(star_1[0]))
# print(star_1[0])
# print(len(star_2))
# print(len(star_3))
# print(len(star_4))
# print(len(star_5))
# print(sheet.nrows)

# text_star_ is text of specific rating level
text_tmp = [x[0] for x in star_1]
text_star_1 = ' '.join(text_tmp)
text_tmp = [x[0] for x in star_2]
text_star_2 = ' '.join(text_tmp)
text_tmp = [x[0] for x in star_3]
text_star_3 = ' '.join(text_tmp)
text_tmp = [x[0] for x in star_4]
text_star_4 = ' '.join(text_tmp)
text_tmp = [x[0] for x in star_5]
text_star_5 = ' '.join(text_tmp)

def get_text(text):
    text = text.lower()
    for i in '!@#$%^&*()_¯+-;:`~\'"<>=./?,':
        text = text.replace(i,' ')
    return text.split()

text = []
text.append(get_text(text_star_1))
text.append(get_text(text_star_2))
text.append(get_text(text_star_3))
text.append(get_text(text_star_4))
text.append(get_text(text_star_5))

import xlwt
workbook = xlwt.Workbook()
for sheet in range(len(text)):
    count = {}
    for word in text[sheet]:
        count[word] = count.get(word, 0) + 1
    iteams = list(count.items())
    sheet_ = workbook.add_sheet(str(sheet), cell_overwrite_ok=True)
    for word in range(len(iteams)):
        sheet_.write(word, 0, iteams[word][0])
        sheet_.write(word, 1, iteams[word][1])

file_name = 'word_freq_star_.xls'
workbook.save(file_name)